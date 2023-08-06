import socket
import threading
import time
from Locker_Project import Func


class MyTask_Tag(threading.Thread):
    signal = True
    def __init__(self, mes, lstInput, lstLock, TypeReader, host, Port, input1, input2, output1, output2, Pn532, main):
        threading.Thread.__init__(self)
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
        self._Reader = Pn532
        self.processMain = main

    def run(self):
        valueTag = ''
        print('Check nhan thong tin the tu',self.mes)
        if len(self.mes) == 2:
            id, value1 = [i for i in self.mes]
            lmg = 0
            times = time.time()
            check = False
            if self.TypeRead == 'Copen\n':
                try:
                    while time.time() - times <= 30:
                        if self.signal:
                            uid = self._Reader.read_passive_target(timeout=0.5)
                            if uid is not None:
                                valueTag = ''.join([hex(i) for i in uid])
                                print(valueTag)
                                check = True
                                lmg = 2
                                break
                            self._Reader.power_down()
                        else:
                            check = False
                            break
                    if check:
                        if lmg == 2 and valueTag != '':
                            try:
                                dta1 = bytes(Func.TaiCauTruc(id, 'Copen', valueTag), 'utf-8')
                                size = len(dta1)
                                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                                    sock.connect((self.host, self.Port))
                                    sock.sendall(size.to_bytes(4, byteorder='big'))
                                    sock.sendall(dta1)
                                    sock.close()
                                    del dta1

                            except Exception as e:
                                sock.close()

                                print("MyTask_Tag:", str(e))
                except Exception as e:
                    print("MyTask_Tag:", str(e))

        if len(self.mes) == 3:
            id, typevalue, value = [i for i in self.mes]
            lmg = 0
            times = time.time()
            check = False
            if self.TypeRead == 'Cused':
                try:
                    while time.time() - times <= 30:
                        if self.signal:
                            uid = self._Reader.read_passive_target(timeout=0.5)
                            if uid is not None:
                                valueTag = ''.join([hex(i) for i in uid])
                                print(valueTag)
                                check = True

                                lmg = 2
                                break
                            self._Reader.power_down()
                        else:
                            check = False
                            break
                        pass
                    if check:
                        if lmg == 2 and valueTag != '':
                            try:
                                dta1 = bytes(Func.TaiCauTruc(id, typevalue, valueTag), 'utf-8')
                                size = len(dta1)
                                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock11:
                                    sock11.connect((self.host, self.Port))
                                    sock11.sendall(size.to_bytes(4, byteorder='big'))
                                    sock11.sendall(dta1)
                                    del dta1
                                    sock11.close()
                                # self.processMain.Thetudangdoc = False
                            except Exception as e:
                                sock11.close()
                                # self.processMain.Thetudangdoc = False
                                print("MyTask_Tag1:", str(e))
                except Exception as e:
                    print("MyTask_Tag2:", str(e))
                    # self.processMain.ClearThread()
                    # self.processMain.Thetudangdoc = False

                    # self._blynk.notify("MyTask_Tag2: " + str(e))

    def __del__(self):
        print(self.name, ' Đã bị xóa')
