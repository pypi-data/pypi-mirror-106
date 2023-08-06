import base64
import socket
import threading
import time
from io import BytesIO
from Locker_Project import Func
from Locker_Project import adafruit_fingerprint
from PIL import Image


class MyTask_Finger(threading.Thread):
    status = True
    signal = True

    def __init__(self, finger, mes,
                 namefileImg, lstInput, lstLock,
                 TypeReader, host, Port, input1, input2,
                 output1, output2, uart, main):
        threading.Thread.__init__(self)
        self.uart = uart
        self.finger = finger
        self.namefileImg = namefileImg
        self.mes = mes
        self.lstInput = lstInput
        self.listLock = lstLock
        self.TypeRead = TypeReader
        self.host = host
        self.Port = Port
        self._input1 = input1
        self._input2 = input2
        self._output1 = output1
        self._output2 = output2
        self.processMain = main

    @property
    def Exit(self):
        return self.signal

    @Exit.setter
    def Exit(self, signal):
        self.signal = signal

    @property
    def Finger(self):
        return self.finger

    @Finger.setter
    def Finger(self, finger):
        self.finger = finger

    @property
    def Uart(self):
        return self.uart

    @Uart.setter
    def Uart(self, uart):
        self.uart = uart

    def Get_Finger_Image(self):
        times = time.time()
        check = False
        try:
            while time.time() - times <= 30:  # Ham kich hoat cam bien van tay
                if self.signal: # đoạn này để thoát while thôi, chứ còn đoạn lệnh dưới while nữa
                    if not self.processMain.vantaydangdoc:
                        self.processMain.vantaydangdoc = True
                        i = self.finger.get_image()
                        self.processMain.vantaydangdoc = False
                        if i == adafruit_fingerprint.OK:
                            self.processMain.vantaydangdoc = True # Truongf hợp này là trường hợp đèn sáng và có người đưa vân tay vào
                            # đống đó nằm đây
                            self.processMain.VanTayDangDayDuLieu = True # ngăn chặn việc vân tay đang đẩy dữ liệu lên và có 1 thread mới tới đọc cảm biến vân tay
                            img = Image.new("L", (256, 288), "white")  # 256, 288
                            pixeldata = img.load()
                            mask = 0b00001111
                            result = self.finger.get_fpdata(sensorbuffer="image") # đoạn này bắt đầu đẩy dữ liệu tù cảm biến vân tay lên cho con Rasp pi Zero
                            self.processMain.vantaydangdoc = False
                            self.processMain.VanTayDangDayDuLieu = False

                            x = 0
                            y = 0
                            for i in range(len(result)):
                                pixeldata[x, y] = (int(result[i]) >> 4) * 17
                                x += 1
                                pixeldata[x, y] = (int(result[i]) & mask) * 17
                                if x == 255:
                                    x = 0
                                    y += 1
                                else:
                                    x += 1
                            buffer = BytesIO()
                            img.save(buffer, format="PNG")  # Enregistre l'image dans le buffer
                            myimage = buffer.getvalue()
                            check = True
                            return base64.b64encode(myimage).decode('utf-8')
                            # break
                        if i == adafruit_fingerprint.NOFINGER:
                            print(".", end="", flush=True)
                            self.processMain.vantaydangdoc = False
                            self.processMain.VanTayDangDayDuLieu = False
                        time.sleep(0.2)
                else:
                    check = False
                    self.processMain.vantaydangdoc = False
                    self.processMain.VanTayDangDayDuLieu = False
                    break
            #  ạn này nếu có ai đó nahasn vân tay khi đèn sáng, thì nó chạy vào đây. Nó đọc vân tay mất gần 2s

            if not check:
                self.processMain.vantaydangdoc = False
                self.processMain.VanTayDangDayDuLieu = False
            # else:
            #     self.processMain.VanTayDangDayDuLieu = True # ngăn chặn việc vân tay đang đẩy dữ liệu lên và có 1 thread mới tới đọc cảm biến vân tay
            #     img = Image.new("L", (256, 288), "white")  # 256, 288
            #     pixeldata = img.load()
            #     mask = 0b00001111
            #     result = self.finger.get_fpdata(sensorbuffer="image") # đoạn này bắt đầu đẩy dữ liệu tù cảm biến vân tay lên cho con Rasp pi Zero
            #     x = 0
            #     y = 0
            #     for i in range(len(result)):
            #         pixeldata[x, y] = (int(result[i]) >> 4) * 17
            #         x += 1
            #         pixeldata[x, y] = (int(result[i]) & mask) * 17
            #         if x == 255:
            #             x = 0
            #             y += 1
            #         else:
            #             x += 1
            #     buffer = BytesIO()
            #     img.save(buffer, format="PNG")  # Enregistre l'image dans le buffer
            #     myimage = buffer.getvalue()
            #     self.processMain.vantaydangdoc = False
            #     self.processMain.VanTayDangDayDuLieu = False
            #     return base64.b64encode(myimage).decode('utf-8')
        except Exception as e:
            print('Loi Van Tay 1', str(e))
            self.processMain.vantaydangdoc = False
            self.processMain.VanTayDangDayDuLieu = False
            return False

    def run(self):
        print('Kiem chung du lieu', self.mes)
        if len(self.mes) == 2:
            id, value1 = [i for i in self.mes]
            if self.TypeRead == 'FDK':
                msg = self.Get_Finger_Image()
                if not msg:
                    print('Khong co van Tay')
                    self.processMain.vantaydangdoc = False
                    self.processMain.ClearThread()
                    return False
                dta1 = Func.TaiCauTruc(id, value1.split('\n')[0], msg)
                dta2 = bytes(dta1, 'utf-8')
                size = len(dta2)
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
                    sck.connect((self.host, self.Port))
                    sck.sendall(size.to_bytes(4, byteorder='big'))
                    sck.sendall(dta2)
                    sck.close()
                    del msg, dta1
                self.processMain.vantaydangdoc = False
                self.processMain.ClearThread()
                return True
                pass
            if self.TypeRead == 'Fopen':
                valueFinger = self.Get_Finger_Image()
                if not valueFinger:
                    self.processMain.vantaydangdoc = False
                    self.processMain.ClearThread()
                    return False
                try:
                    dta1 = bytes(Func.TaiCauTruc(id, 'Fopen', valueFinger), 'utf-8')
                    size = len(dta1)
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                        sock.connect((self.host, self.Port))
                        sock.sendall(size.to_bytes(4, byteorder='big'))
                        sock.sendall(dta1)
                        del dta1
                        sock.close()
                    self.processMain.vantaydangdoc = False
                    self.processMain.ClearThread()
                except Exception as e:
                    self.processMain.vantaydangdoc = False
                    self.processMain.ClearThread()
                    print("MyTask_Finger:", str(e))

        if len(self.mes) == 3:
            id, typevalue, value = [i for i in self.mes]
            if self.TypeRead == 'Fused':
                valueFinger = self.Get_Finger_Image()
                if not valueFinger:
                    self.processMain.vantaydangdoc = False
                    self.processMain.ClearThread()
                    return False
                try:
                    dta1 = bytes(Func.TaiCauTruc(id, 'Fused', valueFinger), 'utf-8')
                    size = len(dta1)
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock1:
                        sock1.connect((self.host, self.Port))
                        sock1.sendall(size.to_bytes(4, byteorder='big'))
                        sock1.sendall(dta1)
                        del dta1
                        sock1.close()
                    self.processMain.vantaydangdoc = False
                    self.processMain.ClearThread()
                except Exception as e:
                    self.processMain.vantaydangdoc = False
                    self.processMain.ClearThread()
                    print("MyTask_Finger:", str(e))

    def __del__(self):
        print(self.name, 'thread myTag_Finger bi Xoa')
