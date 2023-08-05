import struct
import time
import serial
import socket
import busio
import digitalio
import board
from adafruit_mcp230xx.mcp23017 import MCP23017
from adafruit_pn532.spi import PN532_SPI
import base64
import threading
from io import BytesIO
from digitalio import DigitalInOut
from Locker_Project import CMD_ScanInput, CMD_Thread, CMD_Process, Func, Locker, adafruit_fingerprint
#import blynklib

# Blynk_Auth= 'sUo9-hDo-8_PfJjt6UCBb4J8Pt_mWVec'
# blynk= blynklib.Blynk(Blynk_Auth)
# WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"


host=''
Port=3003
threamain=[]
lstID=[]
lstLocker={}
tinhieuchot=False

lst=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
lstouputtemp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lstinputtemp = [7, 6, 5, 4, 3, 2, 1, 0, 11, 10, 9, 8, 15, 14, 13, 12]
lstInput1=[]
lstInput2=[]
lstOutput1=[]
lstOutput2=[]
i2c=busio.I2C(board.SCL,board.SDA)

spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.CE0)
reset_pin = DigitalInOut(board.CE1)
pn532 = PN532_SPI(spi, cs_pin, reset=reset_pin,debug=False)

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
exit_event=threading.Event()

Danhsachtu=[] # chứa và quản lý danh sách tủ
uart = serial.Serial("/dev/ttyS0", baudrate=528000, timeout=1)#489600  528000
try:
    finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)
except Exception as e:
    print('Khoi tao Van Tay bị Lỗi',str(e))
    finger=None
def Connect_Device():
    try:
        lstI2C=i2c.scan()
        print(lstI2C)
        if len(pn532.firmware_version)!=4:
            raise RuntimeError('Loi Ket Noi Dau Doc The Tu')
        if(len(lstI2C)!=4):
            raise  RuntimeError('Loi Ket noi Board inout')
        pn532.SAM_configuration()
        mcpOutput1 = MCP23017(i2c, 0x21)
        mcpInput1 = MCP23017(i2c, 0x26)

        mcpOutput2 = MCP23017(i2c, 0x27)  # board 2 cuar Mr Hai
        mcpInput2 = MCP23017(i2c, 0x20)    # board 2 cuar Mr Hai
        # mcpOutput2 = MCP23017(i2c, 0x20)
        # mcpInput2 = MCP23017(i2c, 0x27)

        KhaiBaoInput(mcpInput1,mcpInput2)
        KhaiBaoOutput(mcpOutput1,mcpOutput2)

        if len(lstI2C)!=4:
            raise RuntimeError('Loi ket noi I2C')
        if finger.read_templates() != adafruit_fingerprint.OK:
            raise RuntimeError("Failed to read templates")
        #print("Fingerprint templates: ", finger.templates)
        if finger.count_templates() != adafruit_fingerprint.OK:
            raise RuntimeError("Failed to read templates")
        #print("Number of templates found: ", finger.template_count)
        if finger.read_sysparam() != adafruit_fingerprint.OK:
            raise RuntimeError("Failed to get system parameters")
    except Exception as e:
        print('Error: ',str(e))

def KhaiBaoInput(mcpInput1,mcpInput2):
    for i in lstinputtemp:
        pin = mcpInput1.get_pin(i)
        pin.direction = digitalio.Direction.INPUT
        pin.pull = digitalio.Pull.UP
        lstInput1.append(pin)
        pin1 = mcpInput2.get_pin(i)
        pin1.direction = digitalio.Direction.INPUT
        pin1.pull = digitalio.Pull.UP
        lstInput2.append(pin1)
        pass
    pass
def KhaiBaoOutput(mcpOutput1,mcpOutput2):
    for i in lstouputtemp:
        pin1 = mcpOutput1.get_pin(i)
        pin1.switch_to_output(value=False)
        lstOutput1.append(pin1)
        pin2 = mcpOutput2.get_pin(i)
        pin2.switch_to_output(value=False)
        lstOutput2.append(pin2)
        pass
    pass
def Get_Finger_Image(signak=True):
    """Scan fingerprint then save image to filename."""
    times=time.time()
    check=False
    try:
        while ((time.time()-times<=5) and signak==True):
            i = finger.get_image()
            if i == adafruit_fingerprint.OK:
                check=True
                break
            if i == adafruit_fingerprint.NOFINGER:
                print(".", end="", flush=True)
            elif i == adafruit_fingerprint.IMAGEFAIL:
                print("Imaging error")
                return False
            else:
                print("Other error")
                return False
        if check==False:
            return False
        # let PIL take care of the image headers and file structure
        from PIL import Image  # pylint: disable=import-outside-toplevel
        img= Image.new("L", (256, 288), "white")#256, 288
        pixeldata = img.load()
        mask = 0b00001111
        result = finger.get_fpdata(sensorbuffer="image")
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
        img.save(buffer,format="PNG") #Enregistre l'image dans le buffer
        myimage = buffer.getvalue()
        return base64.b64encode(myimage).decode('utf-8')
    except Exception as e:
        print('Loi Doc Van Tay',str(e))
        # sensor_reset()
        return False
    pass
def get_default_gateway_linux():
    """Read the default gateway directly from /proc."""
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                # If not default route or not RTF_GATEWAY, skip it
                continue
            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

# while 1:
#     object=get_default_gateway_linux()
#     print(object)
#     time.sleep(5)
def Check_Connected(lstthreadstop):

    pass



version='0.6.3'
def Run():
    global lstLocker
    try:
        Connect_Device()
        check=False
        while check!=True:
            lstip= Func.get_default_gateway_linux()
            print(lstip)
            for i in lstip:
                host=i
                try:
                    sock.connect((host, Port))
                    print('tim ra host!!!!!!!!!!!!!!!!!!',host)

                    try:
                        threadmain = '<id>121</id><type>socket</type><data>main</data>'
                        threadmain = threadmain.encode('utf-8')
                        size1 = len(threadmain)
                        sock.sendall(size1.to_bytes(4,byteorder='big'))
                        sock.sendall(threadmain)
                        time.sleep(0.1)

                        chuoi1 = '<id>12121</id><type>message</type><data>0.7.9</data>'
                        chuoi1 = chuoi1.encode('utf-8')
                        size2 = len(chuoi1)
                        sock.sendall(size2.to_bytes(4,byteorder='big'))
                        sock.sendall(chuoi1)
                        time.sleep(0.1)

                        chuoi2 = '<id>1212</id><type>getdata</type><data>statusdoor</data>'
                        chuoi2 = chuoi2.encode('utf-8')
                        size2 = len(chuoi2)
                        sock.sendall(size2.to_bytes(4, byteorder='big'))
                        sock.sendall(chuoi2)

                        msg = sock.recv(1024)
                        dta = msg.decode('utf-8')
                        id = dta.split(';')[0]
                        ref = dta.split(';')[1].split('\n')[0].split('/')
                        if id == '1212':
                            lstLocker = Func.Convert1(ref)
                            print(lstLocker)
                        sock.close()
                        print('Goi version Ok')
                        check=True
                    except Exception as e:
                        print(str(e))
                        break
                    break
                except Exception as e:
                    sock.close()
                    print(str(e))
            time.sleep(1)
        time.sleep(1)
        condition=threading.Condition()
        lstLock=threading.Lock()
        fingerT=CMD_Process.CMD_Process(finger=finger,pn532=pn532, Cmd=lstID,condition=condition,
                                        lst_input=lstLocker,lstLock=lstLock,
                                        exitEvent=exit_event,input1=lstInput1,
                                        input2=lstInput2,output1=lstOutput1,output2=lstOutput2,
                                        tinhieuchot=tinhieuchot,host=host,Port=Port,uart=uart)
        threamain.append(fingerT)
        # scan = CMD_ScanInput.ScanInput(lstinput=lstLocker, lstlock=lstLock,
        #                                lstID=lst,exitEvent=exit_event,
        #                                input1=lstInput1,input2=lstInput2,
        #                                output1=lstOutput1,output2=lstOutput2)
        # threamain.append(scan)
        producer = CMD_Thread.Producer(Cmd=lstID, condition=condition, host=host, Port=Port, exitEvent=exit_event,lstthreadStop=threamain)
        threamain.append(producer)

        for t in threamain:
            t.start()
        # while 1:
        #     for t in threamain:
        #         if
        # while 1:
        #     if Func.is_connected():
        #         blynk.run()
        #     else:
        #         time.sleep(5)

        #exit_event.set()
        # while 1:
        #     time.sleep(2)
        #     print('Exit',exit_event.is_set())

    except Exception as e:
        print('Connect Mysql Error:',str(e))

try:
    if __name__ == '__main__':
        Run()
except Exception as e:
    print(str(e))