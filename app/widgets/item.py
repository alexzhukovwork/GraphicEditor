from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *

class Item(QPushButton):

    def __init__(self, width, height, onClick, icon=None):
        super().__init__()

        self.w = width
        self.h = height
        self.__initUI()
        self.onClick = onClick
        self.clicked.connect(self.onClickEvent)

        if icon is not None:
            self.setIcon(icon)

    def __initUI(self):
        self.setGeometry(0, 0, self.w, self.h)
        self.setMinimumSize(self.w, self.h)
        self.setMaximumSize(self.w, self.h)
        self.setIconSize(QSize(self.w / 2, self.h / 2))
        self.__setStyle()

    def __setStyle(self):
        self.setStyleSheet("border:5px solid rgb(200,209,222); padding: 10px;")

    def setDefaultStyle(self):
        self.setStyleSheet("border:5px solid rgb(200,209,222); padding: 10px;")

    def onClickEvent(self):
        self.onClick()
        self.setStyleSheet("border:5px solid rgb(0,255,0); padding: 10px;")


