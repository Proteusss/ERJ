import sys,cv2,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt,QDateTime,qDebug
from PyQt5.QtGui import  QPixmap, QImage
import detect as dt
import numpy as np
from main import mywindow



class Thread1(QThread):  # 采用线程来播放视频
    flag = True
    changePixmap = pyqtSignal(QtGui.QImage)
    changeList = pyqtSignal(str)
    changeNum = pyqtSignal(int)
    videoN = ''
    people_num = 0
    people_limit = -100
    def run(self):
        #print(Thread.videoN)
        cap = cv2.VideoCapture(Thread1.videoN)
        qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        #counter = 0
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            name_part = 0
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # cv2.imwrite(os.curdir()+'/out/'+videoName+'_'+str(name_part)+'.jpg', rgbImage)
                time2 = QDateTime.currentDateTimeUtc().toString()
                # print(np.array(rgbImage).shape)
                mes = time2 + str(np.array(rgbImage).shape)
                #self.changeList.emit(mes)
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                                 QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                Thread1.people_num =dt.detect_img(p)
                self.judge_num()
                self.changePixmap.emit(p)

                time.sleep(0.014)  # 控制视频播放的速度
                name_part += 1
            else:
                break

    def setVideoName(self,vName):
        Thread1.videoN = vName

    def setPeopleLimit(self,limit):
        Thread1.people_limit = limit




    def judge_num(self):
        time2 = QDateTime.currentDateTimeUtc().toString()
        if Thread1.flag == True:
            if Thread1.people_num > Thread1.people_limit:
                mes = time2 +"视频一:"+ str("人数为:%d ,超过阈值:%d,报警信息已发送"%(Thread1.people_num, Thread1.people_limit))
                self.changeList.emit(mes)
                Thread1.flag  = False
            else:
                pass
        else:
            if Thread1.people_num > Thread1.people_limit:
                mes = time2 +"视频一:"+ str("人数为:%d ,超过阈值:%d,报警信息已发送"%(Thread1.people_num, Thread1.people_limit))
                self.changeList.emit(mes)
            else:
                mes = time2 +"视频一:"+ str("人数为:%d ,低于阈值:%d,解除信号已发送"%(Thread1.people_num, Thread1.people_limit))
                self.changeList.emit(mes)
                Thread1.flag = True
                pass


class Thread2(QThread):  # 采用线程来播放视频
    flag = True
    changePixmap = pyqtSignal(QtGui.QImage)
    changeList = pyqtSignal(str)
    changeNum = pyqtSignal(int)
    videoN = ''
    people_num = 0
    people_limit = -100

    def run(self):
        # print(Thread.videoN)
        cap = cv2.VideoCapture(Thread2.videoN)
        qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        # counter = 0
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            name_part = 0
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # cv2.imwrite(os.curdir()+'/out/'+videoName+'_'+str(name_part)+'.jpg', rgbImage)
                time2 = QDateTime.currentDateTimeUtc().toString()
                # print(np.array(rgbImage).shape)
                mes = time2 + str(np.array(rgbImage).shape)
                # self.changeList.emit(mes)
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                                 QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                Thread2.people_num = dt.detect_img(p)
                self.judge_num()
                self.changePixmap.emit(p)

                time.sleep(0.014)  # 控制视频播放的速度
                name_part += 1
            else:
                break

    def setVideoName(self, vName):
        Thread2.videoN = vName

    def setPeopleLimit(self, limit):
        Thread2.people_limit = limit

    def judge_num(self):
        time2 = QDateTime.currentDateTimeUtc().toString()
        if Thread2.flag == True:
            if Thread2.people_num > Thread2.people_limit:
                mes = time2 +"视频二:"+ str("人数为:%d ,超过阈值:%d,报警信息已发送" % (Thread2.people_num, Thread2.people_limit))
                self.changeList.emit(mes)
                Thread2.flag = False
            else:
                pass
        else:
            if Thread2.people_num > Thread2.people_limit:
                mes = time2 +"视频二:"+ str("人数为:%d ,超过阈值:%d,报警信息已发送" % (Thread2.people_num, Thread2.people_limit))
                self.changeList.emit(mes)
            else:
                mes = time2 +"视频二:"+str("人数为:%d ,低于阈值:%d,解除信号已发送" % (Thread2.people_num, Thread2.people_limit))
                self.changeList.emit(mes)
                Thread2.flag = True
                pass

class Thread3(QThread):  # 采用线程来播放视频
    flag = True
    changePixmap = pyqtSignal(QtGui.QImage)
    changeList = pyqtSignal(str)
    changeNum = pyqtSignal(int)
    videoN = ''
    people_num = 0
    people_limit = -100

    def run(self):
        # print(Thread.videoN)
        cap = cv2.VideoCapture(Thread3.videoN)
        qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        # counter = 0
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            name_part = 0
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # cv2.imwrite(os.curdir()+'/out/'+videoName+'_'+str(name_part)+'.jpg', rgbImage)
                time2 = QDateTime.currentDateTimeUtc().toString()
                # print(np.array(rgbImage).shape)
                mes = time2 + str(np.array(rgbImage).shape)
                # self.changeList.emit(mes)
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                                 QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                Thread3.people_num = dt.detect_img(p)
                self.judge_num()
                self.changePixmap.emit(p)

                time.sleep(0.014)  # 控制视频播放的速度
                name_part += 1
            else:
                break

    def setVideoName(self, vName):
        Thread3.videoN = vName

    def setPeopleLimit(self, limit):
        Thread3.people_limit = limit

    def judge_num(self):
        time2 = QDateTime.currentDateTimeUtc().toString()
        if Thread3.flag == True:
            if Thread3.people_num > Thread3.people_limit:
                mes = time2 +"视频三:"+ str("人数为:%d ,超过阈值:%d,报警信息已发送" % (Thread3.people_num, Thread3.people_limit))
                self.changeList.emit(mes)
                Thread3.flag = False
            else:
                pass
        else:
            if Thread3.people_num > Thread3.people_limit:
                mes = time2 +"视频三:"+ str("人数为:%d ,超过阈值:%d,报警信息已发送" % (Thread3.people_num, Thread3.people_limit))
                self.changeList.emit(mes)
            else:
                mes = time2 +"视频三:"+str("人数为:%d ,低于阈值:%d,解除信号已发送" % (Thread3.people_num, Thread3.people_limit))
                self.changeList.emit(mes)
                Thread3.flag = True
                pass

class Thread4(QThread):  # 采用线程来播放视频
    flag = True
    changePixmap = pyqtSignal(QtGui.QImage)
    changeList = pyqtSignal(str)
    changeNum = pyqtSignal(int)
    videoN = ''
    people_num = 0
    people_limit = -100

    def run(self):
        # print(Thread.videoN)
        cap = cv2.VideoCapture(Thread4.videoN)
        qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        # counter = 0
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            name_part = 0
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # cv2.imwrite(os.curdir()+'/out/'+videoName+'_'+str(name_part)+'.jpg', rgbImage)
                time2 = QDateTime.currentDateTimeUtc().toString()
                # print(np.array(rgbImage).shape)
                mes = time2 + str(np.array(rgbImage).shape)
                # self.changeList.emit(mes)
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                                 QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                Thread4.people_num = dt.detect_img(p)
                self.judge_num()
                self.changePixmap.emit(p)

                time.sleep(0.014)  # 控制视频播放的速度
                name_part += 1
            else:
                break

    def setVideoName(self, vName):
        Thread4.videoN = vName

    def setPeopleLimit(self, limit):
        Thread4.people_limit = limit

    def judge_num(self):
        time2 = QDateTime.currentDateTimeUtc().toString()
        if Thread4.flag == True:
            if Thread4.people_num > Thread4.people_limit:
                mes = time2 +"视频四:"+ str("人数为:%d ,超过阈值:%d,报警信息已发送" % (Thread4.people_num, Thread4.people_limit))
                self.changeList.emit(mes)
                Thread4.flag = False
            else:
                pass
        else:
            if Thread4.people_num > Thread4.people_limit:
                mes = time2 +"视频四:"+ str("人数为:%d ,超过阈值:%d,报警信息已发送" % (Thread4.people_num, Thread4.people_limit))
                self.changeList.emit(mes)
            else:
                mes = time2 +"视频四:"+str("人数为:%d ,低于阈值:%d,解除信号已发送" % (Thread4.people_num, Thread4.people_limit))
                self.changeList.emit(mes)
                Thread4.flag = True
                pass


class SendThread(QThread):#采用线程来发送消息

    def run(self):
        pass
