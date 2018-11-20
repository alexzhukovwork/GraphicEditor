from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
import sys

from helpers.vertex import Vertex
from field import Field
from primitives.circle import Circle
from primitives.rectangle import Rectangle
from primitives.triangle import Triangle

def exceptHook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.field = Field()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Brushes')
        self.setMouseTracking(True)

        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.field.draw(qp)
        qp.end()

    def mouseMoveEvent(self, e):
        self.field.onMove(Vertex(e.x(), e.y()))
        self.paintEvent(e)
        self.update()

    def mousePressEvent(self, e):
        if self.field.canCreate():
            self.field.addObject(Triangle(Vertex(e.x(), e.y())))

        self.field.onClick(Vertex(e.x(), e.y()))


if __name__ == '__main__':
    sys.excepthook = exceptHook
    app = QApplication(sys.argv)
    ex = Example()
    ex.showMaximized()
    sys.exit(app.exec_())
