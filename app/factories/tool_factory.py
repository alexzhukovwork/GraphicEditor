from primitives.circle import Circle
from primitives.rectangle import Rectangle
from primitives.triangle import Triangle
from primitives.pen import Pen
from primitives.line import Line
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

""" 
Static class for creating different tool or primitives:
    Circle,
    Rectangle,
    Triangle,
    Pen,
    Line,
    Eraser
"""
class ToolFactory:
    CIRCLE = 1
    RECTANGLE = 2
    TRIANGLE = 3
    PEN = 4
    LINE = 5
    ERASER = 6

    @staticmethod
    def createPrimitive(id, p, color, qPen, qBrush):
        return {
            ToolFactory.CIRCLE: Circle(p,  color, qPen, qBrush),
            ToolFactory.RECTANGLE: Rectangle(p, color, qPen, qBrush),
            ToolFactory.TRIANGLE: Triangle(p, color, qPen, qBrush),
            ToolFactory.PEN: Pen(p, color, qPen, qBrush),
            ToolFactory.LINE: Line(p, color, qPen, qBrush),
            ToolFactory.ERASER: Pen(p, Qt.white, qPen, qBrush)
        }[id]


