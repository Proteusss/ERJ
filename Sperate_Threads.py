import sys,cv2,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt,QDateTime,qDebug
from PyQt5.QtGui import  QPixmap, QImage
import detect as dt
import numpy as np
import json


sleep_time = 0.025
freq = 50


class videoUIThread(QThread):
    changePixmap = pyqtSignal(QtGui.QImage)
    changeList = pyqtSignal(str)
    changeNum = pyqtSignal(int)
    detectImg = pyqtSignal(np.ndarray)
    flag = True
    videoN = ''
    #people_num = 0
    #people_limit = 100


    def run(self):
        cap = cv2.VideoCapture(self.videoN)
        qDebug('Worker.on_timeout get called from: %s' % hex(int(QThread.currentThreadId())))
        count = 0
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            name_part = 0
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if count % freq == 0:
                    self.detectImg.emit(np.array(rgbImage))
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                                  QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

                time.sleep(sleep_time)
                count = (count + 1) % freq
            else:
                break
    def setVideoName(self, vName):
        self.videoN = vName

    # def setPeopleLimit(self, limit):
    #     self.people_limit = limit

class videoDetectThread(QThread):
    changeNum = pyqtSignal(int)
    people_num = 0
    people_limit = 100
    add_img = pyqtSignal(bytes)
    add_res = pyqtSignal(str)
    set_num = pyqtSignal(int)
    time2 = QDateTime.currentDateTimeUtc().toString()
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 60]
    video_idx = " "
    def setPeopleLimit(self, limit):
        self.people_limit = limit

    def setVideoInd(self,vidx):
        self.video_idx = vidx

    def detectFun(self,image_data):

        self.people_num = dt.detect_img(image_data)
        #Thread4.people_num = dt.detect_img(rgbImage)
        self.changeNum.emit(self.people_num)
        self.set_num.emit(self.people_num)
        #self.judge_num()
        # 组合检测结果并用json打包后放入结果池中
        detect_res = {}
        detect_res['video_idx'] = self.video_idx
        detect_res['time'] = self.time2
        detect_res['people_num'] = self.people_num
        detect_res_str = json.dumps(detect_res)
        self.add_res.emit(detect_res_str)

        # 压缩图片,并将图片放入图片池中,以字节流的形式保存
        result, imencode = cv2.imencode('.jpg', image_data, self.encode_param)

        imencode = np.array(imencode)
        img_str = imencode.tostring()
        self.add_img.emit(img_str)