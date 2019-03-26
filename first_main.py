import sys,cv2,time
from first_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QWidget,QMainWindow ,QGraphicsScene
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt,QDateTime
from PyQt5.QtGui import  QPixmap, QImage
from PyQt5.QtWidgets import QPushButton,QLabel
import numpy as np
import qdarkstyle
import string

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

    def setList(self, tp):
        self.alertlistView.addItem(str(tp))

    def videoprocessing(self):
        print("gogo")

        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mp4;;*.avi;;All Files (*)")
        # cap = cv2.VideoCapture(str(videoName))
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.changeList.connect(self.setList)
        th.start()


class Thread(QThread):  # 采用线程来播放视频

    changePixmap = pyqtSignal(QtGui.QImage)
    changeList = pyqtSignal(str)

    def run(self):
        cap = cv2.VideoCapture(videoName)

        print(videoName)
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                time2 = QDateTime.currentDateTimeUtc().toString()
                # print(np.array(rgbImage).shape)
                mes = time2 + str(np.array(rgbImage).shape)
                self.changeList.emit(mes)
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                                 QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                time.sleep(0.01)  # 控制视频播放的速度
            else:
                break


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    window = mywindow()
    window.setWindowState(QtCore.Qt.WindowMaximized)
    window.show()
    sys.exit(app.exec_())