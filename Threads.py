import sys,cv2,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt,QDateTime,qDebug
from PyQt5.QtGui import  QPixmap, QImage
import detect as dt
import numpy as np
import json


sleep_time = 0.01
freq = 50

class Thread1(QThread):  # 采用线程来播放视频
    flag = True
    changePixmap = pyqtSignal(QtGui.QImage)
    changeList = pyqtSignal(str)
    changeNum = pyqtSignal(int)
    add_img = pyqtSignal(bytes)
    add_res = pyqtSignal(str)
    videoN = ''
    people_num = 0
    people_limit = 100
    def run(self):
        #print(Thread.videoN)
        cap = cv2.VideoCapture(Thread1.videoN)
        qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        #counter = 0
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 60]
        count = 0
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            name_part = 0
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # cv2.imwrite(os.curdir()+'/out/'+videoName+'_'+str(name_part)+'.jpg', rgbImage)
                time2 = QDateTime.currentDateTimeUtc().toString()
                # print(np.array(rgbImage).shape)
                #print(np.array(rgbImage).shape)
                #self.changeList.emit(mes)
                # convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                #                                  QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                # p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                if count % freq == 0:
                    Thread1.people_num =dt.detect_img(rgbImage)
                    self.judge_num()
                    self.changeNum.emit(Thread1.people_num)

                    # 将检测结果打包放入 结果池中
                    detect_res = {}
                    detect_res['video_idx'] = "video1"
                    detect_res['time'] = time2
                    detect_res['people_num'] = Thread1.people_num
                    detect_res_str = json.dumps(detect_res)
                    self.add_res.emit(detect_res_str)

                    # 将图片压缩后放入 图片池中
                    # encode_img = cv2.imencode('jpg',rgbImage,[int(cv2.IMWRITE_JPEG_QUALITY), 60])
                    # frame = cv2.flip(frame, 1)
                    result, imencode = cv2.imencode('.jpg', frame, encode_param)
                    imencode = np.array(imencode)

                    # img_bytes = imencode.tobytes()
                    img_str = imencode.tostring()
                    # print("in thread:"+str(len(img_bytes))+"  shape:"+str(rgbImage.shape)+" dtype:"+str(rgbImage.dtype)+"\n")
                    # print(img_str)
                    self.add_img.emit(img_str)
                    # self.add_img.emit(img_bytes)
                    # img_str = rgbImage.tolist                用tolist 太慢了!!!






                put_text = "people:"+str(Thread1.people_num)
                img_with_num = cv2.putText(rgbImage,put_text,(350,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
                img_convertToQtFormat = QtGui.QImage(img_with_num.data, img_with_num.shape[1], img_with_num.shape[0],
                                                 QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                p_with_num = img_convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p_with_num)



                time.sleep(sleep_time)  # 控制视频播放的速度
                name_part += 1
                count = (count + 1) %freq
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
    add_img = pyqtSignal(bytes)
    add_res = pyqtSignal(str)
    videoN = ''
    people_num = 0
    people_limit = 100

    def run(self):
        # print(Thread.videoN)
        cap = cv2.VideoCapture(Thread2.videoN)
        qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        # counter = 0
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 60]
        count = 0
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            name_part = 0
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # cv2.imwrite(os.curdir()+'/out/'+videoName+'_'+str(name_part)+'.jpg', rgbImage)
                time2 = QDateTime.currentDateTimeUtc().toString()
                mes = time2 + str(np.array(rgbImage).shape)
                # self.changeList.emit(mes)
                # convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                #                                  QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                # p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                if count % freq == 0:
                    Thread2.people_num = dt.detect_img(rgbImage)
                    self.judge_num()
                    self.changeNum.emit(Thread2.people_num)
                    # 组合检测结果并用json打包后放入结果池中
                    detect_res = {}
                    detect_res['video_idx'] = "video2"
                    detect_res['time'] = time2
                    detect_res['people_num'] = Thread2.people_num
                    detect_res_str = json.dumps(detect_res)
                    self.add_res.emit(detect_res_str)

                    # 压缩图片,并将图片放入图片池中,以字节流的形式保存
                    result, imencode = cv2.imencode('.jpg', frame, encode_param)

                    imencode = np.array(imencode)
                    img_str = imencode.tostring()
                    self.add_img.emit(img_str)






                put_text = "people:" + str(Thread2.people_num)
                img_with_num = cv2.putText(rgbImage, put_text, (350, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
                img_convertToQtFormat = QtGui.QImage(img_with_num.data, img_with_num.shape[1], img_with_num.shape[0],
                                                     QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                p_with_num = img_convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p_with_num)

                #更新主界面的图片显示
                self.changePixmap.emit(p_with_num)






                time.sleep(sleep_time)  # 控制视频播放的速度
                count = (count + 1) % freq
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
    add_img = pyqtSignal(bytes)
    add_res = pyqtSignal(str)
    videoN = ''
    people_num = 0
    people_limit = 100

    def run(self):
        # print(Thread.videoN)
        cap = cv2.VideoCapture(Thread3.videoN)
        qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        # counter = 0
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 60]
        count = 0
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
                # convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                #                                  QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                # p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                if count % freq == 0:

                    Thread3.people_num = dt.detect_img(rgbImage)
                    self.changeNum.emit(Thread3.people_num)
                    self.judge_num()
                    # 组合检测结果并用json打包后放入结果池中
                    detect_res = {}
                    detect_res['video_idx'] = "video3"
                    detect_res['time'] = time2
                    detect_res['people_num'] = Thread3.people_num
                    detect_res_str = json.dumps(detect_res)
                    self.add_res.emit(detect_res_str)

                    # 压缩图片,并将图片放入图片池中,以字节流的形式保存
                    result, imencode = cv2.imencode('.jpg', frame, encode_param)

                    imencode = np.array(imencode)
                    img_str = imencode.tostring()
                    self.add_img.emit(img_str)

                put_text = "people:" + str(Thread3.people_num)
                img_with_num = cv2.putText(rgbImage, put_text, (350, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
                img_convertToQtFormat = QtGui.QImage(img_with_num.data, img_with_num.shape[1], img_with_num.shape[0],
                                                     QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                p_with_num = img_convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)


                # 更新主界面的图片显示
                self.changePixmap.emit(p_with_num)



                time.sleep(sleep_time)  # 控制视频播放的速度
                name_part += 1
                count = (count + 1) % freq
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
    people_limit = 100
    add_img = pyqtSignal(bytes)
    add_res = pyqtSignal(str)
    def run(self):
        # print(Thread.videoN)
        cap = cv2.VideoCapture(Thread4.videoN)
        qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        # counter = 0
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 60]
        count = 0
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
                # convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                #                                  QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                # p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                if count % freq == 0:

                    Thread4.people_num = dt.detect_img(rgbImage)
                    self.changeNum.emit(Thread4.people_num)
                    self.judge_num()
                    # 组合检测结果并用json打包后放入结果池中
                    detect_res = {}
                    detect_res['video_idx'] = "video4"
                    detect_res['time'] = time2
                    detect_res['people_num'] = Thread4.people_num
                    detect_res_str = json.dumps(detect_res)
                    self.add_res.emit(detect_res_str)

                    # 压缩图片,并将图片放入图片池中,以字节流的形式保存
                    result, imencode = cv2.imencode('.jpg', frame, encode_param)

                    imencode = np.array(imencode)
                    img_str = imencode.tostring()
                    self.add_img.emit(img_str)

                put_text = "people:" + str(Thread4.people_num)
                img_with_num = cv2.putText(rgbImage, put_text, (350, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
                img_convertToQtFormat = QtGui.QImage(img_with_num.data, img_with_num.shape[1], img_with_num.shape[0],
                                                     QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                p_with_num = img_convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)


                # 更新主界面的图片显示
                self.changePixmap.emit(p_with_num)



                time.sleep(sleep_time)  # 控制视频播放的速度
                name_part += 1
                count = (count + 1) % freq
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
