from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
from helpers.vertex import Vertex
from field import Field
from singleton.paint_settings import PaintSettings
from factories.pen_factory import PenFactory
from factories.tool_factory import ToolFactory


class Canvas(QFrame):

    def __init__(self, width, height):
        super().__init__()
        self.field = Field()
        self.initUI(width, height)
        self.penFactory = PenFactory()

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
        self.field.onMove(Vertex(e.x(), e.y()))
        self.paintEvent(e)
        self.update()

    def mousePressEvent(self, e):
        if self.field.canCreate():
            self.field.addObject(
                ToolFactory.createPrimitive(
                    PaintSettings.primitiveId,
                    Vertex(e.x(), e.y()),
                    PaintSettings.currentColor,
                    self.penFactory.createPen(
                        PaintSettings.penId
                    )
                )
            )

        self.field.onClick(Vertex(e.x(), e.y()))

    def mouseReleaseEvent(self, e):
        self.field.onRelease(Vertex(e.x(), e.y()))

    def keyPressEvent(self, event):
        id = self.getId(event.key())

        if id is not None:
            if id < 10:
                self.primitiveId = id
            else:
                self.penId = id

    @staticmethod
    def getId(key):
        d = {
            QtCore.Qt.Key_1: ToolFactory.CIRCLE,
            QtCore.Qt.Key_2: ToolFactory.RECTANGLE,
            QtCore.Qt.Key_3: ToolFactory.TRIANGLE,
            QtCore.Qt.Key_4: ToolFactory.PEN,
            QtCore.Qt.Key_Q: PenFactory.SIMPLE_PEN,
            QtCore.Qt.Key_W: PenFactory.WIDTH_PEN,
        }

        if d.__contains__(key):
            return d[key]

