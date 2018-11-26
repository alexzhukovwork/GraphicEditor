from factories.tool_factory import ToolFactory
from factories.pen_factory import PenFactory

class PaintSettings:
    primitiveId = ToolFactory.CIRCLE
    penId = PenFactory.SIMPLE_PEN

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
