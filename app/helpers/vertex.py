import math
from PyQt5.QtCore import *

class Vertex():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toQPoint(self):
        return QPoint(self.x, self.y)

    def calculateDistance(self, vertex):
        return math.sqrt((self.x - vertex.x) ** 2 + (self.y - vertex.y) ** 2)
