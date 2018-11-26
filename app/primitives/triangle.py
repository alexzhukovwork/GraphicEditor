from primitives.primitive import Primitive
from helpers.vertex import Vertex
from PyQt5.QtGui import *


class Triangle(Primitive):
    def __init__(self, position, color, qPen):
        Primitive.__init__(self, position, 3, color, qPen)
        self.secondPoint = position
        self.thirdPoint = position

    def draw(self, canvas):
        self.qPen.setColor(self.color)
        canvas.setPen(self.qPen)
        canvas.drawPolygon(QPolygon([
            self.position.toQPoint(),
            self.secondPoint.toQPoint(),
            self.thirdPoint.toQPoint()]))

    def change(self, p):
        if self.clickCount == 1:
            self.secondPoint = p
        elif self.clickCount == 2:
            self.thirdPoint = p

