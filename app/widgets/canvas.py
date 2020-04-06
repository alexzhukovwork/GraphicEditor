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
import threading

from primitives.pen import Pen

import numpy as np
from PIL import Image
import cv2

import datetime

import classifier.predict as predicter


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
        self.initImage()
        self.increment = 0

    def paintEvent(self, e):
        qp = QPainter()

        qp.begin(self)

        if self.mainWindow.image is not None:
            qp.drawImage(QPoint(0, 0), self.mainWindow.image, QRect(*(0, 0, self.mainWindow.width, self.mainWindow.height)), Qt.AutoColor)
        self.field.draw(qp, PaintSettings.currentAlpha)

        qp.end()

    def initImage(self):
        h = 400
        w = 400
        self.image = QImage(w, h, QImage.Format_RGB32)
        self.path = QPainterPath()
        self.clearImage()

    def clearImage(self):
        self.path = QPainterPath()
        self.image.fill(Qt.white)
        self.field.clear()
        self.update()

    def saveImage(self, fileName, fileFormat):
        self.image.save(fileName, fileFormat)

    def mouseMoveEvent(self, e):
        MouseEmulator.mouseMoveEventCanvas(e, self.mainWindow)
        self.field.onMove(Vertex(e.x(), e.y()))
     #   self.paintEvent(e)
     #   self.update()

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

            self.recognizePrimitive = primitive

            self.field.addObject(
                primitive
            )

        self.field.onClick(Vertex(e.x(), e.y()))

    @staticmethod
    def _createBrush(e):
      #  if e.button() == Qt.LeftButton:
        brush = QBrush()
        brush.setStyle(Qt.NoBrush)
    #    elif e.button() == Qt.RightButton:
     #       PaintSettings.setAlpha(10)

   #         PaintSettings.currentColor.setAlpha(PaintSettings.currentAlpha)
    #        brush = QBrush(PaintSettings.currentColor)

        return brush

    def mouseReleaseEvent(self, e):
        self.field.onRelease(Vertex(e.x(), e.y()))

        if type(self.recognizePrimitive) == Pen:
            pixels = self.recognizePrimitive.get_pixels()

            len = pixels.__len__() - 1

            minX = 1920
            maxX = 0
            minY = 1080
            maxY = 0

            for i in range(0, len):
                current = pixels[i]

                if current.x < minX:
                    minX = current.x
                if current.x > maxX:
                    maxX = current.x
                if current.y < minY:
                    minY = current.y
                if current.y > maxY:
                    maxY = current.y


            width = maxX - minX
            height = maxY - minY

            # Create a black image
            img = np.zeros((height + 10, width + 10, 3), np.uint8)
            img[:, :] = (255, 255, 255)

            for i in range(0, len):
                current = pixels[i]
                next = pixels[i + 1]
                img = cv2.line(img, (current.x - minX + 5, current.y - minY + 5),
                               (next.x - minX + 5, next.y - minY + 5), (0, 0, 0), 5)

          #  self.increment += 1
            image_path = "classifier/" + str(self.increment) + ".png"
            cv2.imwrite(image_path, img)

            self.onPredict(predicter.predict(image_path), minX, minY, width, height)

        #    print("start " + str(minX) + " " + str(minY))
        #    print("finish " + str(maxX) + " " + str(maxY))
        #    print(str(width) + " " + str(height))

    def saveCanvas(self, name):
        pixmap = self.grab()
        pixmap.save(name, "PNG")

    def drawCircle(self, x, y, width, height):
        print("Circle")
        self.drawCustom(ToolFactory.CIRCLE, x, y)
        self.field.onClick(Vertex(x, y))
        self.field.onMove(Vertex(x + width, y + height))
        self.field.onClick(Vertex(x + width, y + height))

    def drawRectangle(self, x, y,  width, height):
        print("Rectangle")
        self.drawCustom(ToolFactory.RECTANGLE, x, y)
        self.field.onClick(Vertex(x, y))
        self.field.onMove(Vertex(x + width, y + height))
        self.field.onClick(Vertex(x + width, y + height))

    def drawTriangle(self, x, y, width, height):
        print("Triangle")
        self.drawCustom(ToolFactory.TRIANGLE, x, y+ height)
        self.field.onClick(Vertex(x, y + height))
        self.field.onMove(Vertex(x + width, y + height))
        self.field.onClick(Vertex(x + width, y + height))
        self.field.onMove(Vertex(x + width / 2, y))
        self.field.onClick(Vertex(x + width / 2, y))
        self.paintEvent(None)
        self.update()

    def onPredict(self, predictable, x, y, width, height):
        self.field.removeObject(self.recognizePrimitive)

        if predictable == "Rectangle":
            self.drawRectangle(x, y, width, height)
        elif predictable == "Circle":
            self.drawCircle(x, y, width, height)
        elif predictable == "Triangle":
            self.drawTriangle(x, y, width, height)

    def drawCustom(self, id, x, y):
        primitiveId = id
        color = PaintSettings.currentColor
        color.setAlpha(PaintSettings.currentAlpha)
        point = Vertex(x, y)
        pen = PenFactory.createPen(PaintSettings.penId)
        brush = self._createBrush(None)

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


