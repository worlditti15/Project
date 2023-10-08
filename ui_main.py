
from tkinter import filedialog
from PyQt5.QtCore import QCoreApplication, QRect
from PyQt5.QtWidgets import QFrame, QWidget

from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
import pygame

#from custom_action import close_app
#import UI's
from ui_loading_screen import Ui_SplashScreen
#from ui_main import *
import os
from pygame import *
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from main_elements import *
from custom_action import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PyQt5.QtCore import QDir


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'davinci_homeiJtBAr.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QTabWidget, QWidget)
import main_elements

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1539, 840)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(0, 0, 1920, 1080))
        self.main_frame.setStyleSheet(u"QFrame#main_frame{\n"
"		\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	\n"
"}\n"
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.controls_frame = QFrame(self.main_frame)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setGeometry(QRect(0, 759, 1540, 80))
        self.controls_frame.setMinimumSize(QSize(980, 80))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        self.controls_frame.setFont(font)
        self.controls_frame.setStyleSheet(u"QFrame#controls_frame{\n"
"	\n"
"	background-color: rgba(0, 0, 0,0.6);\n"
"	border-top-left-radius:0px;\n"
"	border-top-right-radius:0px;\n"
"	\n"
"\n"
"    \n"
"	\n"
"\n"
"}")
        self.controls_frame.setFrameShape(QFrame.StyledPanel)
        self.controls_frame.setFrameShadow(QFrame.Raised)
        self.controls_frame.setLineWidth(3)
        self.playbutton = QPushButton(self.controls_frame)
        self.playbutton.setObjectName(u"playbutton")
        self.playbutton.setGeometry(QRect(734, 0, 72, 72))
        font1 = QFont()
        font1.setStyleStrategy(QFont.NoAntialias)
        self.playbutton.setFont(font1)
        self.playbutton.setCursor(QCursor(Qt.ArrowCursor))
        self.playbutton.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/pause-button.png", QSize(), QIcon.Active, QIcon.On)
        self.playbutton.setIcon(icon)
        self.playbutton.setIconSize(QSize(32, 32))
        self.playbutton.setAutoRepeatDelay(0)
        self.playbutton.setAutoRepeatInterval(0)
        self.playbutton.setAutoDefault(False)
        self.playbutton.setFlat(True)
        self.forwardbutton = QPushButton(self.controls_frame)
        self.forwardbutton.setObjectName(u"forwardbutton")
        self.forwardbutton.setGeometry(QRect(806, 0, 72, 72))
        self.forwardbutton.setFont(font1)
        self.forwardbutton.setLayoutDirection(Qt.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u":/icons/forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.forwardbutton.setIcon(icon1)
        self.forwardbutton.setIconSize(QSize(32, 32))
        self.forwardbutton.setCheckable(False)
        self.forwardbutton.setAutoRepeatDelay(0)
        self.forwardbutton.setAutoRepeatInterval(0)
        self.forwardbutton.setAutoDefault(False)
        self.forwardbutton.setFlat(True)
        self.backbutton = QPushButton(self.controls_frame)
        self.backbutton.setObjectName(u"backbutton")
        self.backbutton.setGeometry(QRect(662, 0, 72, 72))
        self.backbutton.setFont(font1)
        self.backbutton.setLayoutDirection(Qt.LeftToRight)
        self.backbutton.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/fast-backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backbutton.setIcon(icon2)
        self.backbutton.setIconSize(QSize(32, 32))
        self.backbutton.setAutoRepeatDelay(0)
        self.backbutton.setAutoRepeatInterval(0)
        self.backbutton.setFlat(True)
        self.horizontalSlider = QSlider(self.controls_frame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(1280, 30, 160, 18))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.open_musicdiag = QPushButton(self.controls_frame)
        self.open_musicdiag.setObjectName(u"open_musicdiag")
        self.open_musicdiag.setGeometry(QRect(290, 30, 91, 22))
        font2 = QFont()
        font2.setFamilies([u"Inter Black"])
        self.open_musicdiag.setFont(font2)
        self.song_label = QLabel(self.controls_frame)
        self.song_label.setObjectName(u"song_label")
        self.song_label.setGeometry(QRect(70, 0, 211, 31))
        self.tab_frame = QFrame(self.main_frame)
        self.tab_frame.setObjectName(u"tab_frame")
        self.tab_frame.setGeometry(QRect(0, 65, 1540, 691))
        self.tab_frame.setStyleSheet(u"QFrame#tab_frame{\n"
"\n"
"border-radius:5px\n"
"}")
        self.tab_frame.setFrameShape(QFrame.StyledPanel)
        self.tab_frame.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.tab_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, -2, 1540, 691))
        font3 = QFont()
        font3.setFamilies([u"Inter Black"])
        font3.setBold(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.tabWidget.setFont(font3)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QWidget\n"
"\n"
"{background:transparent}\n"
"\n"
" QTabWidget::pane{border: 0px;\n"
"border-color:red;\n"
"\n"
"background-color: transparent;} \n"
"\n"
"QTabBar::tab {background-color: transparent;color: #ccc;width: 50px;height:48px;font-size:24px} \n"
"\n"
"QTabBar::tab:hover{background-color:#ddd; color: white;}  \n"
"   \n"
"QTabBar::tab:selected{background-color: #363535; color: #008BEA;}\n"
"\n"
"\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(32, 32))
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.home_tab = QWidget()
        self.home_tab.setObjectName(u"home_tab")
        self.home_tab_frame = QFrame(self.home_tab)
        self.home_tab_frame.setObjectName(u"home_tab_frame")
        self.home_tab_frame.setGeometry(QRect(3, -1, 1481, 691))
        self.home_tab_frame.setStyleSheet(u"QFrame#home_tab_frame{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius:3px\n"
"\n"
"}")
        self.home_tab_frame.setFrameShape(QFrame.StyledPanel)
        self.home_tab_frame.setFrameShadow(QFrame.Raised)
        self.label_frame = QFrame(self.home_tab_frame)
        self.label_frame.setObjectName(u"label_frame")
        self.label_frame.setGeometry(QRect(50, 1, 120, 80))
        self.label_frame.setStyleSheet(u"")
        self.label_frame.setFrameShape(QFrame.StyledPanel)
        self.label_frame.setFrameShadow(QFrame.Raised)
        self.top_label = QLabel(self.label_frame)
        self.top_label.setObjectName(u"top_label")
        self.top_label.setGeometry(QRect(10, 1, 101, 31))
        font4 = QFont()
        font4.setFamilies([u"Inter Black"])
        font4.setPointSize(24)
        font4.setBold(False)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.top_label.setFont(font4)
        icon3 = QIcon()
        icon3.addFile(u":/icons/home1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.home_tab, icon3, "")
        self.playlist_tab = QWidget()
        self.playlist_tab.setObjectName(u"playlist_tab")
        self.playlist_frame = QFrame(self.playlist_tab)
        self.playlist_frame.setObjectName(u"playlist_frame")
        self.playlist_frame.setGeometry(QRect(-1, -1, 1461, 691))
        self.playlist_frame.setStyleSheet(u"QFrame#playlist_frame{\n"
"	background-color: rgba(0, 0, 0,1);\n"
"}")
        self.playlist_frame.setFrameShape(QFrame.StyledPanel)
        self.playlist_frame.setFrameShadow(QFrame.Raised)
        self.label_frame_2 = QFrame(self.playlist_frame)
        self.label_frame_2.setObjectName(u"label_frame_2")
        self.label_frame_2.setGeometry(QRect(50, 1, 151, 80))
        self.label_frame_2.setStyleSheet(u"")
        self.label_frame_2.setFrameShape(QFrame.StyledPanel)
        self.label_frame_2.setFrameShadow(QFrame.Raised)
        self.top_label_2 = QLabel(self.label_frame_2)
        self.top_label_2.setObjectName(u"top_label_2")
        self.top_label_2.setGeometry(QRect(10, 1, 141, 41))
        self.top_label_2.setFont(font4)
        self.m_list = QListWidget(self.playlist_frame)
        self.m_list.setObjectName(u"m_list")
        self.m_list.setGeometry(QRect(60, 91, 1391, 571))
        self.m_list.setStyleSheet(u"QListWidget#m_list{\n"
"	\n"
"\n"
"font: 9pt \"Inter\";\n"
"opacity=0.9\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color:white;\n"
"    background-color:transparent;\n"
"}")
        self.comboBox = QComboBox(self.playlist_frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(57, 60, 421, 22))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"\n"
"QComboBox#comboBox{\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px\n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/carousel1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.playlist_tab, icon4, "")
        self.minimize_button = QPushButton(self.main_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(1440, 10, 30, 30))
        icon5 = QIcon()
        icon5.addFile(u":/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon5)
        self.minimize_button.setIconSize(QSize(20, 20))
        self.minimize_button.setFlat(True)
        self.close_button = QPushButton(self.main_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(1490, 10, 30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon6)
        self.close_button.setIconSize(QSize(20, 20))
        self.close_button.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.playbutton.setDefault(False)
        self.forwardbutton.setDefault(False)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.playbutton.setToolTip(QCoreApplication.translate("MainWindow", u"Play/Pause", None))
#endif // QT_CONFIG(tooltip)
        self.playbutton.setText("")
#if QT_CONFIG(tooltip)
        self.forwardbutton.setToolTip(QCoreApplication.translate("MainWindow", u"Next", None))
#endif // QT_CONFIG(tooltip)
        self.forwardbutton.setText("")
#if QT_CONFIG(tooltip)
        self.backbutton.setToolTip(QCoreApplication.translate("MainWindow", u"Previous", None))
#endif // QT_CONFIG(tooltip)
        self.backbutton.setText("")
        self.open_musicdiag.setText(QCoreApplication.translate("MainWindow", u"Open Music", None))
        self.song_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">song_level</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Browse songs</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.top_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Home</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.top_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Playlist</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All Songs", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Rock", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pop", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electronic Dance", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Soundtracks", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.playlist_tab), QCoreApplication.translate("MainWindow", u"Playlist", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.playlist_tab), QCoreApplication.translate("MainWindow", u"Browse Songs", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.minimize_button.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize app", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_button.setText("")
#if QT_CONFIG(tooltip)
        self.close_button.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_button.setText("")
    # retranslateUi


















