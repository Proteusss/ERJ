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



videoN = ""

class mywindow(QMainWindow,Ui_MainWindow): #这个窗口继承了用QtDesignner 绘制的窗口

    video1_limit = -5
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.video1_num = -1
        self.video2_num = -1
        self.video3_num = -1
        self.video4_num = -1


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





    def setList(self, tp):
        self.alertlistView.addItem(str(tp))
        print(mywindow.video1_limit)

    def set_video1_limit(self):


        mywindow.video1_limit = int(self.video1_lineEdit.text())
        self.setList(mywindow.video1_limit)



    def set_video2_limit(self):
        video2_limit = int(self.video2_lineEdit.text())
        self.setList(video2_limit)
    def set_video3_limit(self):
        video3_limit = int(self.video3_lineEdit.text())
        self.setList(video3_limit)
    def set_video4_limit(self):
        video4_limit = int(self.video4_lineEdit.text())
        self.setList(video4_limit)






    def videoprocessing(self):
        print("gogo1")
        global videoName
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        print("got videoName here:",videoName)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
    def video2processing(self):
        print("gogo")

        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        th2 =  Thread(self)
        th2.changePixmap.connect(self.setImage2)
        th2.start()

    def video3processing(self):
        print("gogo")

        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        th3 =  Thread(self)
        th3.changePixmap.connect(self.setImage3)
        th3.start()

    def video4processing(self):
        print("gogo")

        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        th4 =  Thread(self)
        th4.changePixmap.connect(self.setImage4)
        th4.start()



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
                print(mywindow.video1_limit)
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