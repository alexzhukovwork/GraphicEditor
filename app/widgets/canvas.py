from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
from helpers.vertex import Vertex
from field import Field
from factories.paint_settings import PaintSettings
from factories.pen_factory import PenFactory
from factories.tool_factory import ToolFactory
from eye_tracker.mouse_emulator import MouseEmulator

"""Class provides area for painting"""
class Canvas(QFrame):

    def __init__(self, width, height, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.field = Field()
        self.initUI(width, height)

    def initUI(self, width, height):
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setMouseTracking(True)
        self.setGeometry(0, 0, width, height)
        self.setMinimumSize(width, height - 100)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.field.draw(qp)
        qp.end()

    def mouseMoveEvent(self, e):
        MouseEmulator.mouseMoveEventCanvas(e, self.mainWindow)
        self.field.onMove(Vertex(e.x(), e.y()))
        self.paintEvent(e)
        self.update()

    def mousePressEvent(self, e):

        if self.field.canCreate():
            primitiveId = PaintSettings.primitiveId
            color = PaintSettings.currentColor
            color.setAlpha(PaintSettings.currentAlpha)
            point = Vertex(e.x(), e.y())
            pen = PenFactory.createPen(PaintSettings.penId)
            brush = self._createBrush(e)

            primitive = \
                ToolFactory.createPrimitive(
                    primitiveId,
                    point,
                    color,
                    pen,
                    brush
                )

            self.field.addObject(
                primitive
            )

        self.field.onClick(Vertex(e.x(), e.y()))

    @staticmethod
    def _createBrush(e):
        if e.button() == Qt.LeftButton:
            brush = QBrush()
            brush.setStyle(Qt.NoBrush)
        elif e.button() == Qt.RightButton:
            brush = QBrush(PaintSettings.currentColor)

        return brush

    def mouseReleaseEvent(self, e):
        self.field.onRelease(Vertex(e.x(), e.y()))


