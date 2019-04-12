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


class Thread(QThread):  # 采用线程来播放视频

    changePixmap = pyqtSignal(QtGui.QImage)
    changeList = pyqtSignal(str)
    videoN = ''
    def run(self):
        #print(Thread.videoN)
        cap = cv2.VideoCapture(Thread.videoN)
        qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            name_part = 0
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # cv2.imwrite(os.curdir()+'/out/'+videoName+'_'+str(name_part)+'.jpg', rgbImage)
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

    def setVideoName(self,vName):
        Thread.videoN = vName