import sys,cv2,time
from first_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QWidget,QMainWindow ,QGraphicsScene
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt,QDateTime,qDebug
from PyQt5.QtGui import  QPixmap, QImage
from PyQt5.QtWidgets import QPushButton,QLabel
import numpy as np
import qdarkstyle
import string
import os


class mywindow(QMainWindow,Ui_MainWindow): #这个窗口继承了用QtDesignner 绘制的窗口

    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    def setImage(self, image):
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(image))
        #self.video1_graphicsView.fitInView(scene)
        self.video1_graphicsView.setScene(scene)
        #setPixmap(QPixmap.fromImage(image))

    def setImage2(self, image):
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(image))
        #self.video1_graphicsView.fitInView(scene)
        self.video2_graphicsView.setScene(scene)
        #setPixmap(QPixmap.fromImage(image))
    def setImage3(self, image):
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(image))
        #self.video1_graphicsView.fitInView(scene)
        self.video3_graphicsView.setScene(scene)
        #setPixmap(QPixmap.fromImage(image))
    def setImage4(self, image):
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(image))
        #self.video1_graphicsView.fitInView(scene)
        self.video4_graphicsView.setScene(scene)
        #setPixmap(QPixmap.fromImage(image))

    def setList(self, tp):
        self.alertlistView.addItem(str(tp))

    def videoprocessing(self):
        print("gogo")

        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        # cap = cv2.VideoCapture(str(videoName))
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        #th.changeList.connect(self.setList)
        th.start()
    def video2processing(self):
        print("gogo")

        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        # cap = cv2.VideoCapture(str(videoName))
        th2 = Thread(self)
        th2.changePixmap.connect(self.setImage2)
        #th2.changeList.connect(self.setList)
        th2.start()

    def video3processing(self):
        print("gogo")

        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        # cap = cv2.VideoCapture(str(videoName))
        th3 = Thread(self)
        th3.changePixmap.connect(self.setImage3)
        #th3.changeList.connect(self.setList)
        th3.start()

    def video4processing(self):
        print("gogo")

        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        # cap = cv2.VideoCapture(str(videoName))
        th4 = Thread(self)
        th4.changePixmap.connect(self.setImage4)
        #th4.changeList.connect(self.setList)
        th4.start()

class Thread(QThread):  # 采用线程来播放视频

    changePixmap = pyqtSignal(QtGui.QImage)
    changeList = pyqtSignal(str)

    def run(self):
        cap = cv2.VideoCapture(videoName)
        qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        print(videoName)
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
            else:
                break


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    qDebug('From main thread: %s' % hex(int(QThread.currentThreadId())))

    window = mywindow()
    window.setWindowState(QtCore.Qt.WindowMaximized)
    window.show()
    sys.exit(app.exec_())