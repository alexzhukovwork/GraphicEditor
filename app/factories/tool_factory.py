from primitives.circle import Circle
from primitives.rectangle import Rectangle
from primitives.triangle import Triangle
from primitives.pen import Pen
from primitives.line import Line
from PyQt5.QtCore import Qt

class ToolFactory:
    CIRCLE = 1
    RECTANGLE = 2
    TRIANGLE = 3
    PEN = 4
    LINE = 5
    ERASER = 6

    @staticmethod
    def createPrimitive(id, p, color, qPen):
        return {
            ToolFactory.CIRCLE: Circle(p, color, qPen),
            ToolFactory.RECTANGLE: Rectangle(p, color, qPen),
            ToolFactory.TRIANGLE: Triangle(p, color, qPen),
            ToolFactory.PEN: Pen(p, color, qPen),
            ToolFactory.LINE: Line(p, color, qPen),
            ToolFactory.ERASER: Pen(p, Qt.white, qPen)
        }[id]


