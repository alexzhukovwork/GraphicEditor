from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtCore import Qt

"""
Static class for creating pen:
    Thin pen,
    Width pen
"""
class PenFactory:
    SIMPLE_PEN = 10
    WIDTH_PEN = 11

    @staticmethod
    def createPen(id):
        if id == PenFactory.SIMPLE_PEN:
            pen = PenFactory.__createSimplePen()
        elif id == PenFactory.WIDTH_PEN:
            pen = PenFactory.__createWidthPen()

        return pen


    @staticmethod
    def __createSimplePen():
        pen = QPen()
        pen.setWidth(1)
        return pen

    @staticmethod
    def __createWidthPen():
        pen = QPen()
        pen.setWidth(5)
        pen.setCapStyle(Qt.RoundCap)
        return pen

