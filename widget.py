
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_loading_screen import Ui_SplashScreen

import sys

class Widget(QWidget,Ui_SplashScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Data")
        