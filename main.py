import sys,cv2,time
from threading import Thread, Lock
from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QWidget,QMainWindow ,QGraphicsScene
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt,QDateTime,qDebug
from PyQt5.QtGui import  QPixmap, QImage
import qdarkstyle
import Threads as th
import numpy as np
from multiprocessing import  Pipe, Process
from Config import Config
import socket
#import matplotlib.pyplot as plt
import json

videoName = ''

class mywindow(QMainWindow,Ui_MainWindow): #这个窗口继承了用QtDesignner 绘制的窗口

    # video1_limit = 100
    # video2_limit = 100
    # video3_limit = 100
    # video4_limit = 100
    def __init__(self):

        super(mywindow,self).__init__()
        self.video1_limit = 100
        self.video2_limit = 100
        self.video3_limit = 100
        self.video4_limit = 100

        self.video1_current_num = -1
        self.video2_current_num = -1
        self.video3_current_num = -1
        self.video4_current_num = -1

        self.img_pipe_send ,self.img_pipe_recv= Pipe()
        self.res_pipe_send, self.res_pipe_recv =Pipe()

        self.img_pool = []
        self.res_pool = []
        self.setupUi(self)
        self.init_img_client()
        # img_client_th = Thread(target=self.sendimg)
        # img_client_th.start()
        img_client_p = Process(target=self.sendimg,args=(self.img_pipe_recv,))
        img_client_p.start()

        self.init_res_client()
        # res_client_th = Thread(target=self.sendres)
        # res_client_th.start()
        res_client_p = Process(target=self.sendres,args=(self.res_pipe_recv,))
        res_client_p.start()

    #---------------程序消息通知
    def setList(self, tp):
        self.alertlistView.addItem(str(tp))
        #print(mywindow.video1_limit)

    def updateNum(self):
        self.numlistView.setMo

#---------------更新图片的槽函数
    def setImage(self, image):
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(image))
        self.video1_graphicsView.setScene(scene)

    def setImage2(self, image):
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(image))
        self.video2_graphicsView.setScene(scene)

    def setImage3(self, image):
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(image))
        self.video3_graphicsView.setScene(scene)

    def setImage4(self, image):
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(image))
        self.video4_graphicsView.setScene(scene)


#---------------设置阈值的槽函数
    def set_video1_limit(self):
        self.video1_limit = int(self.video1_lineEdit.text())
        self.setList(self.video1_limit)
    def set_video2_limit(self):
        self.video2_limit = int(self.video2_lineEdit.text())
        self.setList(self.video2_limit)
    def set_video3_limit(self):
        self.video3_limit = int(self.video3_lineEdit.text())
        self.setList(self.video3_limit)
    def set_video4_limit(self):
        self.video4_limit = int(self.video4_lineEdit.text())
        self.setList(self.video4_limit)


    #----------实时改变人数
    def change_video1_num(self,num):
        self.video1_current_num = num
    def change_video2_num(self,num):
        self.video2_current_num = num
    def change_video3_num(self,num):
        self.video3_current_num = num
    def change_video4_num(self,num):
        self.video4_current_num = num



    def add_img(self,img):
        #self.img_pool.append(img)
        self.img_pipe_send.send_bytes(img)

    def add_res(self,res):
        #self.res_pool.append(res)
        self.res_pipe_send.send(res)

#-----------------开始检测的槽函数
    def video1processing(self):
        #print("gogo1")
        global videoName
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        #print("got videoName here:",videoName)
        th1= th.Thread1(self)
        th1.setVideoName(videoName)
        th1.setPeopleLimit(self.video1_limit)
        th1.changePixmap.connect(self.setImage)
        th1.changeList.connect(self.setList)
        th1.changeNum.connect(self.change_video1_num)
        th1.add_img.connect(self.add_img)
        th1.add_res.connect(self.add_res)

        th1.start()
    def video2processing(self):
        #print("gogo")

        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        th2 =  th.Thread2(self)
        th2.setVideoName(videoName)
        th2.setPeopleLimit(self.video2_limit)
        th2.changePixmap.connect(self.setImage2)
        th2.changeList.connect(self.setList)
        th2.changeNum.connect(self.change_video2_num)
        th2.add_img.connect(self.add_img)
        th2.add_res.connect(self.add_res)
        th2.start()

    def video3processing(self):
        #print("gogo")

        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        th3 = th.Thread3(self)
        th3.setVideoName(videoName)
        th3.setPeopleLimit(self.video3_limit)
        th3.changePixmap.connect(self.setImage3)
        th3.changeList.connect(self.setList)
        th3.changeNum.connect(self.change_video3_num)
        th3.add_img.connect(self.add_img)
        th3.add_res.connect(self.add_res)
        th3.start()

    def video4processing(self):
        #print("gogo")

        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        th4 = th.Thread4(self)
        th4.setVideoName(videoName)
        th4.setPeopleLimit(self.video4_limit)
        th4.changePixmap.connect(self.setImage4)
        th4.changeList.connect(self.setList)
        th4.changeNum.connect(self.change_video4_num)
        th4.add_img.connect(self.add_img)
        th4.add_res.connect(self.add_res)
        th4.start()



    #初始化 图像传输连接  UDP连接
    def init_img_client(self):


        # init config
        self.config = Config()
        host = self.config.get("server", "host")
        port = self.config.get("server", "img_port")
        self.img_address = (host, int(port))

        # init connection
        try:
            self.img_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)             #UDP 方式
            self.img_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # self.sock.bind(self.address)
        except socket.error as msg:
            print(msg)
            sys.exit(1)
    #为图像传输线程编写执行函数
    def sendimg(self,pipe):

        img_sock = self.img_sock
        img_address = self.img_address
        running = True
        cnt = 0
        img_sock.connect(img_address)
        qDebug('sendimg Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        while running:
            frame = pipe.recv_bytes(46081)
            img_sock.sendto(frame,img_address)

            # while len(self.img_pool) > 0:
            #     frame = self.img_pool.pop(0)   # frame ------> bytes
            #     print("send img")
            #     img_sock.sendto(frame,img_address)
            #

                # 还原图片
                # frame_array = np.frombuffer(frame, dtype=np.uint8)
                # img = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)
                # print(img.shape)

    #初始化传输测试结果传输连接   TCP 连接
    def init_res_client(self):
        self.config = Config()
        host = self.config.get("server", "host")
        port = self.config.get("server", "res_port")
        self.res_address = (host, int(port))
        print(self.res_address)

        # init connection
        try:
            self.res_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP 方式

            # self.sock.bind(self.address)
        except socket.error as msg:
            print(msg)
            sys.exit(1)


    def sendres(self,pipe):

        res_sock = self.res_sock
        res_address = self.res_address
        running = True
        cnt = 0
        res_sock.connect(res_address)
        qDebug('sendres Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        while running:

            # while len(self.res_pool) > 0:
            #     print("have something")
            #     res = self.res_pool.pop(0)
            #     b_res = bytes(res,encoding="utf-8")
            #     print("send res")
            #     res_sock.send(b_res)
            res = pipe.recv()
            b_res = bytes(res, encoding="utf-8")
            #print("send res")
            res_sock.send(b_res)








if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    qDebug('From main thread: %s' % hex(int(QThread.currentThreadId())))

    window = mywindow()
    #conn = window.child_conn
    #NetPro = Process(target=NetProcess,args=(conn,))
    window.setWindowState(QtCore.Qt.WindowMaximized)
    window.show()




    sys.exit(app.exec_())




'''



    class Thread(QThread):  # 采用线程来播放视频

        changePixmap = pyqtSignal(QtGui.QImage)
        changeList = pyqtSignal(str)

        def run(self):
            cap = cv2.VideoCapture(videoName)
            qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
            while (cap.isOpened() == True):
                ret, frame = cap.read()
                name_part = 0
                if ret:
                    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    #cv2.imwrite(os.curdir()+'/out/'+videoName+'_'+str(name_part)+'.jpg', rgbImage)
                    time2 = QDateTime.currentDateTimeUtc().toString()
                    # print(np.array(rgbImage).shape)
                    mes = time2 + str(np.array(rgbImage).shape)
                    self.changeList.emit(mes)
                    convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                                     QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                    p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.changePixmap.emit(p)
                    time.sleep(0.014)  # 控制视频播放的速度
                    name_part += 1
                    print(videoName)
                else:
                    break
'''