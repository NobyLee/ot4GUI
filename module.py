'''
    这是主文件
    实现4台无线ot以及imu的同时操控
'''


from PySide2.QtWidgets import QMainWindow, QApplication,QDialog
from PySide2.QtCore import QRunnable, QThreadPool, QThread, Signal, Slot,QTimer
from PySide2.QtGui import QPixmap
from PySide2 import QtCore
from PySide2.QtGui import QImageReader
import pyqtgraph as pg
pg.setConfigOption('background', 'w')
import time
import binascii
import datetime
from struct import *
from ot4_ui import Ui_MainWindow
from jumpEMG import Ui_Dialog
# from utils import *
import sys
import os
import socket
import numpy as np

from multiprocessing.dummy import Pool as ThreadPool
import scipy.signal as sciSignal



# 这两行标定ot的ip地址
ipPref = '192.168.3.'
subIP = ['4', '6', '7', '9']
ipList = {ipPref + subIP[0]: 0, ipPref + subIP[1]: 1, ipPref + subIP[2]: 2, ipPref + subIP[3]: 3}
ConvFact = 4.8 / 65536

plotSec = 0.6
plotPts = int(plotSec * 2000)
plotFrame = plotPts * 68



class DataRecever(QThread):
    receive = Signal(dict)

    def __init__(self, coon):
        super(DataRecever, self).__init__()
        self.coon = coon
        self.readFlag = True
        # self.drawing_count = 0  # 统计读数据次数
        # self.drawing_all = 30  # 每读drawing_all次画一次图
        # self.writing_count = 0
        # self.writing_all = 300
        # self.threadpool = QThreadPool()  # 线程池
        # print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())  # 输出最大线程数

    def run(self):
        bag_len = plotFrame * 2
        EMGdata = np.zeros(int(plotFrame))
        # bag_len = 5643
        # sign_head = 'aa998877665544332211'
        remain_data = bytes()
        # EMG_data = np.zeros((64, 20*self.drawing_all))
        # IMU_GroData = np.zeros((3, 20*self.drawing_all))
        # IMU_AccData = np.zeros((3, 20*self.drawing_all))
        # data_to_save = bytes()
        # timestamp = ''
        starttime = datetime.datetime.now()
        while self.readFlag:
            print("开始收数据")
            # EMG_data_tmp = np.zeros((64, 20))
            # IMU_GroData_tmp = np.zeros((3, 20))
            # IMU_AccData_tmp = np.zeros((3, 20))
            # total_data = remain_data
            total_data = remain_data
            while True:
                temp = self.coon.recv(1440)
                # print(len(temp))
                total_data += temp
                if len(total_data) > bag_len:
                    break
            data = total_data[:bag_len]
            remain_data = total_data[bag_len:]
            # data = np.array(bytearray(data))
            print('testtttttttttt')
            # print(data.shape)
            # print(len(data))
            for i in range(plotFrame):
                EMGdata[i] = data[i*2]*256 + data[i*2+1]
            tranferData = np.reshape(EMGdata,(plotPts, 68))
            tranferData = np.transpose(tranferData)
            tranferData = tranferData*ConvFact
            self.receive.emit({"data": tranferData})
            print("结束收数据")
        self.coon.close()
        print("关闭收数据连接")

class ChildWindow(QDialog, Ui_Dialog):
    subClose = Signal()

    def __init__(self, *args, obj=None, **kwargs):
        super(ChildWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # self.EMGlabel.setText("EMG module " + str(kwargs['moduleID']) + " Signal")

        self.EMG = pg.GraphicsLayoutWidget()
        self.p = self.EMG.addPlot()
        self.EMGLayout.addWidget(self.EMG)

        self.AUX = pg.GraphicsLayoutWidget()
        self.AUXp = self.AUX.addPlot()
        self.AUXLayout.addWidget(self.AUX)


        nChan = 64  # 64肌电通道 + 2辅助通道
        self.high = nChan
        self.low = 0
        self.step = 1
        self.p.setRange(yRange=[self.low-self.step, self.high+self.step], padding=0)
        # self.p.setRange(xRange=[0, nPoints], padding=0)
        self.act = np.zeros((64, 20000))
        self.t = np.zeros(20000)
        self.EMGline = [None] * 64
        for k in range(64):
            self.EMGline[k] = self.p.plot(self.t, self.act[k, :], pen=(0, 0, 255))
        # print(type(self.EMGline[-1]))
        self.plusButton.pressed.connect(self.range_plus)
        self.minusButton.pressed.connect(self.range_minus)

        nAUXChan = 2  # 64肌电通道 + 2辅助通道
        self.AUXhigh = nAUXChan
        self.AUXlow = 0
        self.AUXstep = 1
        self.AUXp.setRange(yRange=[self.AUXlow - self.AUXstep, self.AUXhigh + self.AUXstep], padding=0)
        # self.p.setRange(xRange=[0, nPoints], padding=0)
        self.AUXact = np.zeros((2, 20000))
        self.AUXline = [None] * 2

        self.AUXline[0] = self.AUXp.plot(self.t, self.AUXact[0, :], pen=(255, 0, 0))
        self.AUXline[1] = self.AUXp.plot(self.t, self.AUXact[1, :], pen=(0, 0, 255))

        # print(type(self.EMGline[-1]))
        self.plusAUXButton.pressed.connect(self.AUXrange_plus)
        self.minusAUXButton.pressed.connect(self.AUXrange_minus)




        print("初始化完成")

    def range_plus(self):
        self.high = self.high / 2
        self.low = self.low / 2
        self.step = self.step/2
        self.p.setRange(yRange=[self.low-self.step, self.high+self.step])


    def range_minus(self):
        self.high = self.high * 2
        self.low = self.low * 2
        self.step = self.step * 2
        self.p.setRange(yRange=[self.low-self.step, self.high+self.step])


    def AUXrange_plus(self):
        self.AUXhigh = self.AUXhigh / 10
        self.AUXlow = self.AUXlow / 10
        self.AUXstep = self.AUXstep/10
        self.AUXp.setRange(yRange=[self.AUXlow-self.AUXstep, self.AUXhigh+self.AUXstep])


    def AUXrange_minus(self):
        self.AUXhigh = self.AUXhigh * 10
        self.AUXlow = self.AUXlow * 10
        self.AUXstep = self.AUXstep * 10
        self.AUXp.setRange(yRange=[self.AUXlow-self.AUXstep, self.AUXhigh+self.AUXstep])


    def closeEvent(self, event) -> None:
        self.subClose.emit()




class DataPlotter(QThread):
    # receive = Signal(dict)

    def __init__(self, id):
        super(DataPlotter, self).__init__()
        self.t = np.zeros(20000)
        self.act = np.zeros((64, 20000))
        self.AUXact = np.zeros((2, 20000))

        self.childWindow = ChildWindow()
        self.childWindow.EMGlabel.setText("EMG module " + str(id) + " Signal")

    def run(self):
        self.childWindow.exec_()


    def update_data(self, s):

        EMG = s["data"]
        EMGdata = np.array(EMG)
        print("开始画图")
        self.plot_data(EMGdata)
        print("结束画图")

    def plot_data(self, EMG):
        BAG = plotPts
        tmp_t = np.linspace(self.t[-1] + plotSec - (20000-1)*0.0005, self.t[-1]+plotSec, 20000)#设置时间轴
        self.t = tmp_t

        #刷新buffer
        tmp_act = np.zeros((64, 20000))
        tmp_act[:, -BAG:] = EMG[:64,:]
        tmp_act[:, 0:-BAG] = self.act[:, BAG:]
        self.act = tmp_act

        tmp_AUXact = np.zeros((2, 20000))
        tmp_AUXact[0, -BAG:] = EMG[-3,:]
        tmp_AUXact[1, -BAG:] = EMG[-1, :]
        tmp_AUXact[:, 0:-BAG] = self.AUXact[:, BAG:]
        self.AUXact = tmp_AUXact


        # if self.window_len == '0.1s':
        #     wl = 100
        # elif self.window_len == '1s':
        #     wl = 1000
        # else:
        #     wl = 10000
        wl = 10000

        #并行画图
        t_plot = self.t[-wl:]
        act_plot = tmp_act[:, -wl:]+np.arange(64).reshape(64,1) * self.childWindow.step
        pool = ThreadPool()
        pool.map(lambda x: x[0].setData(t_plot, x[1]), zip(self.childWindow.EMGline, act_plot))
        pool.close()
        pool.join()

        AUXact_plot = tmp_AUXact[:, -wl:] + np.arange(2).reshape(2, 1) * self.childWindow.AUXstep
        self.childWindow.AUXline[0].setData(t_plot,AUXact_plot[0])
        self.childWindow.AUXline[1].setData(t_plot, AUXact_plot[1])







class SocketServer():

    ipPref = '192.168.3.'
    ipList = {ipPref+'4':0, ipPref+'6':1,ipPref+'7':2,ipPref+'9':3}

    # The first command byte
    GETSET = 0  # 0是set 1是get
    FSAMP1 = 0b10   # 采样率2k
    NCH = 0b11      # 62+2+2通道
    MODE = 0        # 模式为0：多极电极

    cmd1 = GETSET*0b10000000 + FSAMP1*0b100000 + NCH*0b1000 + MODE*0b1      # 这里是命令字节1，*后面的数字用于向左移位相应的比特数
    print(cmd1)
    # The second command byte
    HRES = 0        # 0：分辨率=16 bit
    HPF = 1         # HPF=1：使用高通滤波
    EXT = 0         # EXT=0：标准输入范围
    TRIG = 0        # TRIG=0：通过GO/STOP来控制开始结束使用TCP传输信号
    REC = 0         # TRIG=11的时候才会生效，表示开始或者结束SD卡记录
    GO = 1
    STOP = 0
    cmd2 = HRES*0b10000000 + HPF*0b1000000 + EXT*0b10000 + TRIG*0b100 + REC*0b10 + GO*0b1
    cmd3 = HRES*0b10000000 + HPF*0b1000000 + EXT*0b10000 + TRIG*0b100 + REC*0b10 + STOP*0b1
    # visualize command
    cmdVO = pack('2B', cmd1, cmd2)
    # stop visualizing
    cmdVF = pack('2B', cmd1, cmd3)

    REC = 1             # REC=1：SD卡开始记录数据
    TRIG = 0b11         # TRIG=11：SD卡记录数据
    cmd4 = HRES*0b10000000 + HPF*0b1000000 + EXT*0b10000 + TRIG*0b100 + REC*0b10 + STOP*0b0
    REC = 0             # REC=0：SD卡结束记录数据
    cmd5 = HRES*0b10000000 + HPF*0b1000000 + EXT*0b10000 + TRIG*0b100 + REC*0b10 + STOP*0b0
    # recording command
    cmdRO = pack('2B', cmd1, cmd4)
    # stop recording command
    cmdRF = pack('2B', cmd1, cmd5)

    # Time Bytes


    ##print(cmd)

    # module1中调用：
    # SocketServer(1,fuc = self.updateMStatus, filename = self.name) # set the number of EMG modules
    def __init__(self, *args, **kwargs):
        self.s = socket.socket()         # 创建 socket 对象
        self.host = socket.gethostname() # 获取本地主机名
        self.port = 45454
        print('主机名:',self.host)# 设置端口
        self.s.bind((self.host, self.port))        # 绑定端口
        self.s.listen(5)                 # 等待客户端连接
        self.num = args[0]
        self.ploti = 1              # 当前画图的模块序号
        self.accList = []
        self.list2Accept = []
        self.clientList = []
        self.f = kwargs['fuc']      # module中传入的函数名是切换LED图片的状态
        self.fileName= kwargs['filename']
        self.time  = pack('2B', 4,176) # first byte: 256 seconds,  second Byte: 1 second

    def __del__(self):
        print("End Socket.")
        self.s.close()

    def setFileName(self, name):
        self.fileName = name
        print('set file name: ', self.fileName)

    def startVisualizing(self):
        global emgReadSign
        emgReadSign = True
        self.sendCommand(self.cmdVO, 1)             #发送命令的函数



    def startRecording(self):
        self.sendCommand(self.cmdRO, 1)

    def stopRecording(self):
        self.sendCommand(self.cmdRF, 0)
        self.clientList.clear()
        print("End EMG recording.")


    def stopVisualizing(self):
        self.stopRecording()

        # self.sendCommand(self.cmdVF, 0)
        self.clientList.clear()     # 这里估计是错的，所以可视化出错了，不了解，去验证一下
        print("End visualizing.")


    def setRecordTime(self, t):
        self.time = pack('2B', t[0], t[1])

    def setAcceptDevices(self, list2accpet):
        self.list2Accept.clear()
        for i in list2accpet:
            self.list2Accept.append(self.ipPref + i)
        print("set list2accept:")
        print(self.list2Accept)

    def sendCommand(self, cmdB, state = 1):     # state: with timestamp or not
        while True:
            if (len(self.accList)==len(self.list2Accept)):
                self.accList.clear()
                break
            print("ready to accept ip")
            self.s.settimeout(10)
            c,addr = self.s.accept()     # 建立客户端连接
            ip = addr[0]
            print('accept ip:',ip)
            if ip in self.list2Accept:
                if (ip not in self.accList):
                    ModleSig = (self.ipList[ip] + 65).to_bytes(1,byteorder = 'little')  # 根据IP地址转换为A/B/C/D
                    print ('连接地址：', ip)
                    print("length of client: %d" % len(self.clientList))
                    self.clientList.append(c)
                    if state == 1:
                        fileNameCode = self.fileName.encode()       # 4个字节，4个字母
                        #timeStamp = self.getTimeStampBytes()
                        cmd = cmdB + self.time + fileNameCode + ModleSig
                    else:
                        cmd = cmdB
                    self.accList.append(ip)
                    self.f(ip, state)
                    c.send(cmd)

                else:
                    print('address already exists:', ip)
            else:
                c.close()                # 关闭连接

    # def readData(self,i, cList):
    #     T = emgModuleLoaderT(cList[i-1])
    #     T.start()

    def stopReading(self):
        global emgReadSign
        emgReadSign = False
        self.clientList.clear()
        print("End EMG wireless reading.")



    def getTimeStampBytes(self):
        localtime = time.localtime()

        y = localtime[0]-1980
        m = localtime[1]
        d = localtime[2]
        h = localtime[3]
        m = localtime[4]
        s = localtime[5]

        r1 = (y<<1) + (m>>7)
        r2 = ((m&7)<<5) + d
        r3 = (h<<3) + ((m&56)>>3)
        r4 = ((m&7)<<5) + s

        r = pack('4B', r1,r2,r3,r4)
        return r






class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, app, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("HD sEMG")

        self.app = app  #不知道是个啥
        self.imuPort = 'null'   #imu的端口号
        self.label.setText("File Name (4 alphabetic characters).")
        self.lcdNumber.display(123456)
        self.N = 16 #这是个啥
        self.btn5Status = 0 #btn5又是什么，大概是apply按钮，用来设置文件名的


        self.moduleList = [self.label_4,self.label_6, self.label_8,self.label_10]   # 就是gui上显示的4个模块名的label对象
        for i in self.moduleList:
            i.setPixmap(QPixmap('off.jpg')) #设置4个LED灯全暗


        defaultFileNamePrfx = 'AAAA'    #默认文件名是AAAA
        self.name = defaultFileNamePrfx
        # Start button
        self.startButton.setCheckable(True)
        self.startButton.clicked.connect(self.startButton_clicked)

        # Stop button
        self.endButton.setCheckable(True)
        self.endButton.setDisabled(True)
        self.endButton.clicked.connect(self.endButton_clicked)

        # Apply button
        self.applyButton.setCheckable(True)
        self.applyButton.clicked.connect(self.applyButton_clicked)

        # Set button
        self.setButton.setCheckable(True)
        self.setButton.clicked.connect(self.setButton_clicked)

        # Display button
        self.displayButton.setCheckable(True)
        self.displayButton.clicked.connect(self.displayButton_clicked)

        # checkBox
        self.lcdNumber.display(0)   #计时器默认为0

        # Line Edit

        # Recording Time    #这一段没看懂
        self.time = [4, 176]
        self.sckServer = SocketServer(1,fuc = self.updateMStatus, filename = self.name) # set the number of EMG modules
        self.sckServer.setRecordTime(self.time)
        print(ipList)

    def startButton_clicked(self):  #start按钮
        self.counter = 0        #从0开始计时
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timer_behave)       #1s跳变一次计时器
        # self.imu()  #没看懂，大概是控制imu的行为
        # self.sckServer.setAcceptDevices([subIP[2]])
        self.sckServer.setAcceptDevices(subIP)
        self.sckServer.startRecording()     #开始记录
        self.timer.start()      #开始计时器
        #self.imuThread.join()
        self.startButton.setDisabled(True)
        self.endButton.setDisabled(False)
        self.displayButton.setDisabled(True)

    def endButton_clicked(self):  # end按钮
        self.sckServer.stopRecording()      #结束记录
        self.timer.stop()       #结束计时
        # self.imuT.imu.Stop()        #结束imu线程？
        print('Stop recording.')
        self.startButton.setDisabled(False)
        self.endButton.setDisabled(True)
        self.displayButton.setDisabled(False)


    def applyButton_clicked(self):  # apply按钮：更改文件名
        name = self.filenameEdit.text()
        # 文件名必须是字母且长度为4
        if name.isalpha() & (len(name)==4):
            self.name = name
            self.sckServer.setFileName(name)    # 发送更改文件名的指令
        else:
            print('Invalid name format. Please change another file name.')

    def setButton_clicked(self):  # set按钮：设置imu端口号
        com = self.portEdit.text()
        self.imuPort = com

    def displayButton_clicked(self):  # display/stop d~按钮：展示/停止展示信号
        if(self.btn5Status == 0):
            id = self.displayModuleEdit.text()     # dispaly按钮上方的输入框，用于输入要展示的module序号
            id = int(id)
            if id in [1,2,3,4]:
                self.sckServer.setAcceptDevices([subIP[id-1]])       # 设置要接收的ip地址
                self.sckServer.startVisualizing()           # 开始肌电信号可视化

                self.plotter = DataPlotter(id)
                self.receiver = DataRecever(self.sckServer.clientList[self.sckServer.ploti - 1])

                self.receiver.receive.connect(self.plotter.update_data)
                self.plotter.childWindow.subClose.connect(self.displayButton.click)

                self.plotter.start()
                self.receiver.start()

                # emgPlotter.VisualOn = True      # 应该是可视化的某个flag
                # self.WinD = emgPlotter.emgPlotter(self.app)     # 应该是展示信号的子窗口
                # self.WinD.start()
                self.displayButton.setText('Stop displaying')    # 把display文字改成stop display
                self.btn5Status = 1     # 把展示状态设置为1
                self.startButton.setDisabled(True)

            else:
                print("invalid module number (please enter value:1~4)")
        else:
            self.receiver.readFlag = False
            self.receiver.quit()
            self.sckServer.stopVisualizing()    # 停止可视化
            self.btn5Status = 0     #  把展示状态设置为1
            self.displayButton.setText('Display')    # 把stop display文字改成display
            # emgPlotter.VisualOn = False     # ```把绘图线程的flag设置为False```
            self.startButton.setDisabled(False)  # pushButton: start按钮



    def apply_fileName(self,s):     # 应用文件名？
        print(s)

    def timer_behave(self):     # 计时器跳变1s一次
        self.counter += 1
        self.lcdNumber.display(self.counter)
        if self.counter == self.time[0]*256 + self.time[1]: # 超时就自动点击end？
            self.endButton_clicked()

    def updateMStatus(self, ip, state):     # 应该是切换LED灯的状态
        print(ip)
        if ip in ipList:
            if state == 1:
                styleText = u"background-color: green;"
            elif state == 0:
                styleText = u"background-color: red;"
            self.moduleList[ipList[ip]].setStyleSheet(styleText)     # ipList是一个字典，moduleList是图像框的列表，这里应该是控制某个图像亮灯或者灭灯
            self.app.processEvents()    # 让界面可以及时更新
        else:
            print('ip status wasn\'t updated.')

    def imu(self):  # 设置imu端口，开启imu线程
        # self.imuT = imuThread.imuThread(self.name+'1', self.imuPort)
        # self.imuT.start()
        pass

if __name__=='__main__':
    QImageReader.supportedImageFormats()
    app = QApplication(sys.argv)
    app.addLibraryPath(os.path.join(os.path.dirname(QtCore.__file__),"plugins"))
    window = MainWindow(app)
    window.show()
    app.exec_()
