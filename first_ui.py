# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 316)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_V_and_M = QtWidgets.QGridLayout()


        self.videoWidget = QtWidgets.QWidget(self.centralwidget)
        #self.videoWidget.setGeometry(QtCore.QRect(0, 0, 481, 201))
        self.videoWidget.setObjectName("videoWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.videoWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")


        #UI for video4
        self.video4_widget = QtWidgets.QWidget(self.videoWidget)
        self.video4_widget.setObjectName("video4_widget")
        self.video4_PushButton = QtWidgets.QPushButton(self.video4_widget)
       # self.video4_PushButton.setGeometry(QtCore.QRect(10, 70, 20, 20))
        self.video4_PushButton.setStyleSheet("border-image: url(:/icon/open.png);background: transparent;\n"
"")
        self.video4_PushButton.setText("")
        self.video4_PushButton.setObjectName("video4_PushButton")
        self.video4_lineEdit = QtWidgets.QLineEdit(self.video4_widget)
       # self.video4_lineEdit.setGeometry(QtCore.QRect(110, 70, 41, 20))
        self.video4_lineEdit.setObjectName("video4_lineEdit")
        self.video4_SetButton = QtWidgets.QPushButton(self.video4_widget)
        #self.video4_SetButton.setGeometry(QtCore.QRect(160, 69, 21, 21))
        self.video4_SetButton.setStyleSheet("border-image: url(:/icon/set.png);background: transparent;")
        self.video4_SetButton.setText("")
        self.video4_SetButton.setObjectName("video4_SetButton")
        self.video4_graphicsView = QtWidgets.QGraphicsView(self.video4_widget)
       # self.video4_graphicsView.setGeometry(QtCore.QRect(0, 0, 201, 71))
        self.video4_graphicsView.setObjectName("video4_graphicsView")
        self.gridLayout.addWidget(self.video4_widget, 1, 1, 1, 1)
        self.gridLayout_video4 = QtWidgets.QGridLayout()
        self.gridLayout_video4.addWidget(self.video4_graphicsView,0,0,9,30)
        self.gridLayout_video4.addWidget(self.video4_PushButton,9,0,1,1)
        self.gridLayout_video4.addWidget(self.video4_lineEdit,9,20,1,4)
        self.gridLayout_video4.addWidget(self.video4_SetButton,9,26,1,1)
        self.video4_widget.setLayout(self.gridLayout_video4)



        # UI for Video1
        self.video1_widget = QtWidgets.QWidget(self.videoWidget)
        self.video1_widget.setObjectName("video1_widget")
        self.video1_PushButton = QtWidgets.QPushButton(self.video1_widget)
        self.video1_PushButton.setGeometry(QtCore.QRect(10, 70, 20, 20))
        self.video1_PushButton.setStyleSheet("border-image: url(:/icon/open.png);background: transparent;\n"
"")
        self.video1_PushButton.setText("")
        self.video1_PushButton.setObjectName("video1_PushButton")
        self.video1_PushButton.clicked.connect(MainWindow.videoprocessing)
        self.video1_lineEdit = QtWidgets.QLineEdit(self.video1_widget)
        #self.video1_lineEdit.setGeometry(QtCore.QRect(110, 70, 41, 20))
        self.video1_lineEdit.setObjectName("video1_lineEdit")
        self.video1_SetButton = QtWidgets.QPushButton(self.video1_widget)
        #self.video1_SetButton.setGeometry(QtCore.QRect(160, 69, 21, 21))
        self.video1_SetButton.setStyleSheet("border-image: url(:/icon/set.png);background: transparent;")
        self.video1_SetButton.setText("")
        self.video1_SetButton.setObjectName("video1_SetButton")
        self.video1_graphicsView = QtWidgets.QGraphicsView(self.video1_widget)
       # self.video1_graphicsView.setGeometry(QtCore.QRect(0, 0, 201, 71))
        self.video1_graphicsView.setObjectName("video1_graphicsView")
        self.gridLayout.addWidget(self.video1_widget, 0, 0, 1, 1)
        self.gridLayout_video1 = QtWidgets.QGridLayout()
        self.gridLayout_video1.addWidget(self.video1_graphicsView, 0, 0, 9, 30)
        self.gridLayout_video1.addWidget(self.video1_PushButton, 9, 0, 1, 1)
        self.gridLayout_video1.addWidget(self.video1_lineEdit, 9, 20, 1, 4)
        self.gridLayout_video1.addWidget(self.video1_SetButton, 9, 26, 1, 1)
        self.video1_widget.setLayout(self.gridLayout_video1)




        #UI for video2
        self.video2_widget = QtWidgets.QWidget(self.videoWidget)
        self.video2_widget.setObjectName("video2_widget")
        self.video2_PushButton = QtWidgets.QPushButton(self.video2_widget)
       # self.video2_PushButton.setGeometry(QtCore.QRect(10, 70, 20, 20))
        self.video2_PushButton.setStyleSheet("border-image: url(:/icon/open.png);background: transparent;\n"
"")
        self.video2_PushButton.setText("")
        self.video2_PushButton.setObjectName("video2_PushButton")
        self.video2_lineEdit = QtWidgets.QLineEdit(self.video2_widget)
        #self.video2_lineEdit.setGeometry(QtCore.QRect(110, 70, 41, 20))
        self.video2_lineEdit.setObjectName("video2_lineEdit")
        self.video2_SetButton = QtWidgets.QPushButton(self.video2_widget)
        #self.video2_SetButton.setGeometry(QtCore.QRect(160, 69, 21, 21))
        self.video2_SetButton.setStyleSheet("border-image: url(:/icon/set.png);background: transparent;")
        self.video2_SetButton.setText("")
        self.video2_SetButton.setObjectName("video2_SetButton")
        self.video2_graphicsView = QtWidgets.QGraphicsView(self.video2_widget)
       # self.video2_graphicsView.setGeometry(QtCore.QRect(0, 0, 201, 71))
        self.video2_graphicsView.setObjectName("video2_graphicsView")
        self.gridLayout.addWidget(self.video2_widget, 0, 1, 1, 1)
        self.gridLayout_video2 = QtWidgets.QGridLayout()
        self.gridLayout_video2.addWidget(self.video2_graphicsView, 0, 0, 9, 30)
        self.gridLayout_video2.addWidget(self.video2_PushButton, 9, 0, 1, 1)
        self.gridLayout_video2.addWidget(self.video2_lineEdit, 9, 20, 1, 4)
        self.gridLayout_video2.addWidget(self.video2_SetButton, 9, 26, 1, 1)
        self.video2_widget.setLayout(self.gridLayout_video2)






        #UI for video3
        self.video3_widget = QtWidgets.QWidget(self.videoWidget)
        self.video3_widget.setObjectName("video3_widget")
        self.video3_PushButton = QtWidgets.QPushButton(self.video3_widget)
        #self.video3_PushButton.setGeometry(QtCore.QRect(10, 70, 20, 20))
        self.video3_PushButton.setStyleSheet("border-image: url(:/icon/open.png);background: transparent;\n"
"")
        self.video3_PushButton.setText("")
        self.video3_PushButton.setObjectName("video3_PushButton")
        self.video3_lineEdit = QtWidgets.QLineEdit(self.video3_widget)
        #self.video3_lineEdit.setGeometry(QtCore.QRect(110, 70, 41, 20))
        self.video3_lineEdit.setObjectName("video3_lineEdit")
        self.video3_SetButton = QtWidgets.QPushButton(self.video3_widget)
        #self.video3_SetButton.setGeometry(QtCore.QRect(160, 69, 21, 21))
        self.video3_SetButton.setStyleSheet("border-image: url(:/icon/set.png);background: transparent;")
        self.video3_SetButton.setText("")
        self.video3_SetButton.setObjectName("video3_SetButton")
        self.video3_graphicsView = QtWidgets.QGraphicsView(self.video3_widget)
        #self.video3_graphicsView.setGeometry(QtCore.QRect(0, 0, 201, 71))
        self.video3_graphicsView.setObjectName("video3_graphicsView")
        self.gridLayout.addWidget(self.video3_widget, 1, 0, 1, 1)

        self.gridLayout_video3 = QtWidgets.QGridLayout()
        self.gridLayout_video3.addWidget(self.video3_graphicsView, 0, 0, 9, 30)
        self.gridLayout_video3.addWidget(self.video3_PushButton, 9, 0, 1, 1)
        self.gridLayout_video3.addWidget(self.video3_lineEdit, 9, 20, 1, 4)
        self.gridLayout_video3.addWidget(self.video3_SetButton, 9, 26, 1, 1)
        self.video3_widget.setLayout(self.gridLayout_video3)





        self.messageWidget = QtWidgets.QWidget(self.centralwidget)
        #self.messageWidget.setGeometry(QtCore.QRect(0, 210, 471, 61))
        self.messageWidget.setObjectName("messageWidget")
        self.gridLayout_messs = QtWidgets.QGridLayout()

        self.numlistView = QtWidgets.QListView(self.messageWidget)
        self.numlistView.setObjectName("numlistView")
        self.gridLayout_messs.addWidget(self.numlistView, 0, 2, 4, 10)
        self.alertlistView = QtWidgets.QListWidget(self.messageWidget)
        self.alertlistView.setObjectName("alertlistView")

        self.gridLayout_messs.addWidget(self.alertlistView,0, 0, 4, 1 )
        self.messageWidget.setLayout(self.gridLayout_messs)



        #layout for videoWidget and messageWidget
        self.gridLayout_V_and_M.addWidget(self.videoWidget, 0, 0, 500, 50)
        self.gridLayout_V_and_M.addWidget(self.messageWidget,500,0,1,50)
        self.centralwidget.setLayout(self.gridLayout_V_and_M)



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 14))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人流量检测系统(边缘端)"))

import apprcc_rc
