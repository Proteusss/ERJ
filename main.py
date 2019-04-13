import sys,cv2,time
from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QWidget,QMainWindow ,QGraphicsScene
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt,QDateTime,qDebug
from PyQt5.QtGui import  QPixmap, QImage
import qdarkstyle
import Threads as th



videoName = ''

class mywindow(QMainWindow,Ui_MainWindow): #这个窗口继承了用QtDesignner 绘制的窗口

    video1_limit = -100
    video2_limit = -100
    video3_limit = -100
    video4_limit = -100
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)



#---------------程序消息通知
    def setList(self, tp):
        self.alertlistView.addItem(str(tp))
        print(mywindow.video1_limit)


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
        mywindow.video1_limit = int(self.video1_lineEdit.text())
        self.setList(mywindow.video1_limit)
    def set_video2_limit(self):
        mywindow.video2_limit = int(self.video2_lineEdit.text())
        self.setList(mywindow.video2_limit)
    def set_video3_limit(self):
        mywindow.video3_limit = int(self.video3_lineEdit.text())
        self.setList(mywindow.video3_limit)
    def set_video4_limit(self):
        mywindow.video4_limit = int(self.video4_lineEdit.text())
        self.setList(mywindow.video4_limit)





#-----------------开始检测的槽函数
    def video1processing(self):
        print("gogo1")
        global videoName
        videoName, videoType = QFileDialog.getOpenFileName(self,
                                                           "打开视频",
                                                           "",
                                                           # " *.jpg;;*.png;;*.jpeg;;*.bmp")
                                                           " *.mov;;*.mp4;;*.avi;;All Files (*)")
        print("got videoName here:",videoName)
        th1= th.Thread1(self)
        th1.setVideoName(videoName)
        th1.setPeopleLimit(self.video1_limit)
        th1.changePixmap.connect(self.setImage)
        th1.changeList.connect(self.setList)
        th1.start()
    def video2processing(self):
        print("gogo")

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
        th2.start()

    def video3processing(self):
        print("gogo")

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
        th3.start()

    def video4processing(self):
        print("gogo")

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
        th4.start()





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    qDebug('From main thread: %s' % hex(int(QThread.currentThreadId())))

    window = mywindow()

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