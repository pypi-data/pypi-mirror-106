import base64
import socket
import threading
import time
from io import BytesIO
from Locker_Project import Func
from Locker_Project import adafruit_fingerprint
from PIL import Image


class MyTask_Finger(threading.Thread):

    def __init__(self, finger, namefileImg, lstInput, lstLock, host, Port, input1, input2, output1, output2, uart, main):
        threading.Thread.__init__(self)
        self.uart = uart
        self.finger = finger
        self.namefileImg = namefileImg
        self.lstInput = lstInput
        self.listLock = lstLock
        self.host = host
        self.Port = Port
        self._input1 = input1
        self._input2 = input2
        self._output1 = output1
        self._output2 = output2
        self.processMain = main
    signal = True
    mes = None
    TypeRead = None

    def Get_Finger_Image(self):
        times = time.time()
        check = False
        try:
            while time.time() - times <= 30:  # Ham kich hoat cam bien van tay
                if self.signal: # đoạn này để thoát while thôi, chứ còn đoạn lệnh dưới while nữa
                    i = self.finger.get_image()
                    if i == adafruit_fingerprint.OK:
                        img = Image.new("L", (256, 288), "white")  # 256, 288
                        pixeldata = img.load()
                        mask = 0b00001111
                        result = self.finger.get_fpdata(sensorbuffer="image") # đoạn này bắt đầu đẩy dữ liệu tù cảm biến vân tay lên cho con Rasp pi Zero
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
                        return base64.b64encode(myimage).decode('utf-8')
                else:
                    check = False
                    self.processMain.ThreadValue.ThreadName ='th'
                    break
            if not check:
                self.processMain.ThreadValue.ThreadName ='th'
        except Exception as e:
            print('Loi Van Tay 1', str(e))
            self.processMain.ThreadValue.ThreadName ='th'
            return False

    def run(self):
        try:
            dtaimage = self.Get_Finger_Image()
            if dtaimage == None:
                return False
            if len(self.mes) == 2:
                id, value1 = [i for i in self.mes]
                if self.TypeRead == 'FDK\n':
                    dta1 = Func.TaiCauTruc(id, value1.split('\n')[0], dtaimage)
                    dta2 = bytes(dta1, 'utf-8')
                    size = len(dta2)
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
                        sck.connect((self.host, self.Port))
                        sck.sendall(size.to_bytes(4, byteorder='big'))
                        sck.sendall(dta2)
                        sck.close()
                        del dtaimage, dta1
                    self.processMain.ThreadValue.ThreadName ='th'
                    return True
                    pass
                if self.TypeRead == 'Fopen\n':
                    try:
                        dta1 = bytes(Func.TaiCauTruc(id, 'Fopen', dtaimage), 'utf-8')
                        size = len(dta1)
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                            sock.connect((self.host, self.Port))
                            sock.sendall(size.to_bytes(4, byteorder='big'))
                            sock.sendall(dta1)
                            del dta1
                            sock.close()
                        self.processMain.ThreadValue.ThreadName ='th'
                        return True
                    except Exception as e:
                        self.processMain.ThreadValue.ThreadName ='th'
                        print("MyTask_Finger:", str(e))

            if len(self.mes) == 3:
                id, typevalue, value = [i for i in self.mes]
                if self.TypeRead == 'Fused':
                    try:
                        dta1 = bytes(Func.TaiCauTruc(id, 'Fused', dtaimage), 'utf-8')
                        size = len(dta1)
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock1:
                            sock1.connect((self.host, self.Port))
                            sock1.sendall(size.to_bytes(4, byteorder='big'))
                            sock1.sendall(dta1)
                            del dta1
                            sock1.close()
                        self.processMain.ThreadValue.ThreadName ='th'
                        return True
                    except Exception as e:
                        self.processMain.ThreadValue.ThreadName ='th'
                        print("MyTask_Finger:", str(e))
        except Exception as e:
            self.processMain.ThreadValue.ThreadName ='th'
            print('Loi Roi',str(e))
    def __del__(self):
        print(self.name, 'thread myTag_Finger bi Xoa')
