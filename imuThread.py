import threading, imu
'''
    该文件是IMU数据采集的子线程
    
'''
class imuThread(threading.Thread):
    def __init__(self, filename, imuPort):
        threading.Thread.__init__(self)
        self.filename = filename
        self.imu = imu.IMU(filename, imuPort)   #怎么又开一个线程？？？不是线程，只是一个类，封装了一个start方法

    def run(self):
        print("start imu recording.\n")
        self.imu.start()    # 调用上述类的start()方法
        print('end imu recording.\n')
