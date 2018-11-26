from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtCore import Qt

class PenFactory:
    SIMPLE_PEN = 10
    WIDTH_PEN = 11

    def __init__(self):
        self.__createSimplePen()
        self.__createWidthPen()

    def createPen(self, id):
        return {
            PenFactory.SIMPLE_PEN: self.simplePen,
            PenFactory.WIDTH_PEN: self.widthPen,
        }[id]

    def __createSimplePen(self):
        self.simplePen = QPen()
        self.simplePen.setWidth(1)

    def __createWidthPen(self):
        self.widthPen = QPen()
        self.widthPen.setWidth(5)
        self.widthPen.setCapStyle(Qt.RoundCap)

