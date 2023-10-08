# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_loading_screenYaGxER.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QProgressBar,
    QSizePolicy, QWidget)
import images_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(950, 549)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setGeometry(QRect(0, 0, 951, 551))
        self.dropShadowFrame.setMinimumSize(QSize(951, 551))
        self.dropShadowFrame.setMaximumSize(QSize(951, 551))
        self.dropShadowFrame.setAutoFillBackground(True)
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	border-image: url(:/Logo Banner/Users/Lenovo/Pictures/DaVINCI BLUE.png);\n"
"\n"
"background-color: rgba(0, 0, 0, 100);\n"
"border-radius:50px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(350, 360, 261, 24))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200,200,200);\n"
"	border-style:none;\n"
"	border-radius:10px;\n"
"	text-align:center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"\n"
"	border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:0.982955, y2:0.619727, stop:0 rgba(255, 87, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"	\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        #self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.progressBar.setFormat(QCoreApplication.translate("SplashScreen", u"%p%", None))
    # retranslateUi
'''
class LinearProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        #custom properties

        self.value=0
        self.width=261
        self.height=24
        self.progress_width=0
        self.max_value=100
        self.progress_color=0xffa500

        #Text
        self.enable_text=True
        self.font_family="Inter"
        self.font_size=10
        self.suffix="%"
        self.text_color=0xff79c6


        #set value 
        def set_value(self,value):
            self.value=value
            self.repaint()
        
        #BG
        self.enable_bg=True
        self.bg_color=0x44475a

        #set default size without layout
        self.resize(self.width,self.height)

'''

