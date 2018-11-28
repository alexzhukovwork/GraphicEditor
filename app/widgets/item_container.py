from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *

class ItemContainer(QFrame):

    def __init__(self, width, height):
        super().__init__()

        self.w = width
        self.h = height
        self.initUI()

    def setWidgets(self, layout, widgets):
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        for w in widgets:
            layout.addWidget(w)

        self.setLayout(layout)

    def initUI(self):
        self.setStyleSheet("background-color: rgb(235, 236, 237); ")
        self.setGeometry(0, 0, self.w, self.h)
