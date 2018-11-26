from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *

class Item(QPushButton):

    def __init__(self, width, height, onClick, icon=None):
        super().__init__()

        self.w = width
        self.h = height
        self.pen = QPen()
        self.pen.setWidth(5)
        self.pen.setCapStyle(Qt.RoundCap)
        self.initUI()
        self.onClick = onClick
        self.clicked.connect(self.onClickEvent)

        if icon is not None:
            self.setIcon(icon)

    def initUI(self):
        self.setGeometry(0, 0, self.w, self.h)
        self.setMinimumSize(self.w, self.h)
        self.setIconSize(QSize(self.w, self.h))
        self.setStyleSheet("border:5px solid rgb(200,209,222); padding: 10px;")


    def setDefaultStyle(self):
        self.setStyleSheet("border:5px solid rgb(200,209,222); padding: 10px;")

    def onClickEvent(self):
        self.onClick()
        self.setStyleSheet("border:5px solid rgb(0,255,0); padding: 10px;")

    def paintEvent(self, e):
        QPushButton.paintEvent(self, e)
        qp = QPainter()
        qp.begin(self)
        qp.setPen(self.pen)
       # qp.drawRect(5, 5, self.w - 10, self.h - 10)
        qp.end()

