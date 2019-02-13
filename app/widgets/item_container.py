from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
from eye_tracker.mouse_emulator import MouseEmulator


"""Class provides layout for tool items on panel"""
class ItemContainer(QFrame):

    def __init__(self, width, height, mainWindow):
        super().__init__()
        self.w = width
        self.h = height
        self.initUI()
        self.mainWindow = mainWindow

    def setWidgets(self, layout, widgets):
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        for w in widgets:
            layout.addWidget(w)

        self.setLayout(layout)

    def initUI(self):
        self.setMouseTracking(True)
        self.setStyleSheet("background-color: rgb(235, 236, 237); ")
        self.setGeometry(0, 0, self.w, self.h)

    def mouseClick(self):
        self.mainWindow.setupCursor()

    def mouseMoveEvent(self, e):
        MouseEmulator.mouseMoveEvent(e, self.mainWindow)

