from factories.tool_factory import ToolFactory
from factories.pen_factory import PenFactory
from factories.palette_factory import PaletteFactory
from PyQt5.QtGui import QColor

"""
Static class for management paint settings
    Select primitives,
    Select brush,
    Select color
"""
class PaintSettings:
    primitiveId = ToolFactory.RECTANGLE
    penId = PenFactory.SIMPLE_PEN
    paletteId = PaletteFactory.FIRST
    currentColor = QColor(0, 0, 0)
    currentAlpha = 255

    @staticmethod
    def selectRectangle():
        PaintSettings.primitiveId = ToolFactory.RECTANGLE
        PaintSettings.penId = PenFactory.SIMPLE_PEN

    @staticmethod
    def selectCircle():
        PaintSettings.primitiveId = ToolFactory.CIRCLE
        PaintSettings.penId = PenFactory.SIMPLE_PEN

    @staticmethod
    def selectTriangle():
        PaintSettings.primitiveId = ToolFactory.TRIANGLE
        PaintSettings.penId = PenFactory.SIMPLE_PEN

    @staticmethod
    def selectPen():
        PaintSettings.primitiveId = ToolFactory.PEN
        PaintSettings.penId = PenFactory.SIMPLE_PEN

    @staticmethod
    def selectBrush():
        PaintSettings.primitiveId = ToolFactory.PEN
        PaintSettings.penId = PenFactory.WIDTH_PEN

    @staticmethod
    def selectEraser():
        PaintSettings.primitiveId = ToolFactory.ERASER
        PaintSettings.penId = PenFactory.WIDTH_PEN

    @staticmethod
    def selectLine():
        PaintSettings.primitiveId = ToolFactory.LINE
