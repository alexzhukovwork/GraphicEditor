from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5 import QtWidgets
import sys

from factories.paint_settings import PaintSettings
from factories.palette_factory import PaletteFactory

from widgets.canvas import Canvas
from widgets.widget_item import WidgetItem
from widgets.palette_item import PaletteItem
from widgets.item_container import ItemContainer
from eye_tracker.mouse_emulator import MouseEmulator

"""Main Window"""
class WindowView(QMainWindow):
    def __init__(self, width, height):
        QMainWindow.__init__(self, flags=Qt.Window)
        self.width = width
        self.height = height
        self.win = QWidget()
        self.widgetItems = []
        self.__setupWindow()
        self.image = None

    def setupFirstCursor(self):
        pm = QtGui.QPixmap('../resources/cursorRedCircle.png')
        cursor = QtGui.QCursor(pm)
        self.win.setCursor(cursor)
        self.win.update()
        MouseEmulator.firstTimer.stop()

    def setupSecondCursor(self):
        pm = QtGui.QPixmap('../resources/cursorGreenCircle.png')
        cursor = QtGui.QCursor(pm)
        self.win.setCursor(cursor)
        self.win.update()
        MouseEmulator.secondTimer.stop()

    def setupDefaultCursor(self):
        self.win.setCursor(Qt.CustomCursor)
        self.win.update()

    def __setupWindow(self):
        self.win.setStyleSheet("background-color:rgb(200,209,222);")
        self.win.setWindowTitle("PyQt")

        toolContainerWidth = self.width * 0.07
        toolContainerHeight = self.height

        self.tools = self.__createTools(toolContainerWidth, toolContainerWidth * 0.45)
        self.fileTools = self.__createFileTools(toolContainerWidth, self.width * 0.035)


        currentColor = PaletteItem(
            toolContainerWidth,
            toolContainerWidth * 0.5,
            None,
            PaintSettings.currentColor
        )

        paletteItems = []
        for palette in PaletteFactory.createPalette(PaintSettings.paletteId):
            paletteItems.append(PaletteItem(
                toolContainerWidth * 1,
                toolContainerWidth * 0.25,
                None,
                palette,
                currentColor
            ))

        colorLayoutFirstColumn = self.__createToolContainer(
            QVBoxLayout(),
            0,
            0,
            paletteItems
        )

        colorCurrentContainer = self.__createToolContainer(
            QVBoxLayout(),
            toolContainerWidth,
            toolContainerHeight,
            [currentColor]
        )

        self.canvas = self.__createCanvas(self.width * 0.93, self.height)

        mainLayout = self.__createBox(
            QHBoxLayout(),
            0,
            0,
            self.width,
            self.height,
            (10, 10, 0, 0),
            [
                self.canvas,
                self.__createToolContainer(
                    QVBoxLayout(),
                    toolContainerWidth,
                    toolContainerHeight,
                    self.tools + [colorCurrentContainer] + [colorLayoutFirstColumn] + self.fileTools,

                )
            ]
        )

        self.win.setLayout(
            mainLayout
        )

        self.win.setMouseTracking(True)

    def __createBox(self, box, x, y, width, height, margins, widgets):
        box.setGeometry(QRect(x, y, width, height))
        box.setContentsMargins(*margins)

        for widget in widgets:
            box.addWidget(widget)

        return box

    def __createCanvas(self, width, height):
        canvas = Canvas(
            width,
            height,
            self
        )

        canvas.setFocusPolicy(Qt.StrongFocus)

        return canvas

    def __createToolContainer(self, layout, width, height, tools):
        toolContainer = ItemContainer(
            width,
            height,
            self
        )

        layout.setContentsMargins(0, 10, 0, -5)

        toolContainer.setWidgets(
            layout,
            tools
        )

        return toolContainer

    def __createSliderContainer(self, layout, width, height, margins, tools):
        sliderContainer = ItemContainer(
            width,
            height,
            self
        )

        layout.setContentsMargins(*margins)

        sliderContainer.setWidgets(
            layout,
            tools
        )

        return sliderContainer

    def __createTools(self, width, height):
        tools = [
            WidgetItem(
                width, height,
                self.onClickItem(PaintSettings.selectRectangle),
                QtGui.QIcon(QtGui.QPixmap("../resources/rectangle.png"))
            ),
            WidgetItem(
                width, height,
                self.onClickItem(PaintSettings.selectTriangle),
                QtGui.QIcon(QtGui.QPixmap("../resources/triangle.png"))
            ),
            WidgetItem(
                width, height,
                self.onClickItem(PaintSettings.selectCircle),
                QtGui.QIcon(QtGui.QPixmap("../resources/circle.png"))
            ),
            WidgetItem(
                width, height,
                self.onClickItem(PaintSettings.selectLine),
                QtGui.QIcon(QtGui.QPixmap("../resources/line.png"))
            ),
            WidgetItem(
                width, height,
                self.onClickItem(PaintSettings.selectPen),
                QtGui.QIcon(QtGui.QPixmap("../resources/pen.png"))
            ),
            WidgetItem(
                width, height,
                self.onClickItem(PaintSettings.selectBrush),
                QtGui.QIcon(QtGui.QPixmap("../resources/brush.png"))
            ),
            WidgetItem(
                width, height,
                self.onClickItem(PaintSettings.selectSmartPen),
                QtGui.QIcon(QtGui.QPixmap("../resources/smartPen.png"))
            ),
            WidgetItem(
                width, height,
                self.onClickItem(PaintSettings.selectEraser),
                QtGui.QIcon(QtGui.QPixmap("../resources/eraser.png"))
            ),

        ]

        tools[0].setClickStyle()

        return tools

    def __createFileTools(self, width, height):
        tools = [
            WidgetItem(
                width, height,
                self.saveImage,
                QtGui.QIcon(QtGui.QPixmap("../resources/save.png")),
                True
            ),
            WidgetItem(
                width, height,
                self.openFileNameDialog,
                QtGui.QIcon(QtGui.QPixmap("../resources/open.png")),
                True
            ),
        ]

        return tools

    def openFileNameDialog(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Image Files (*.png *.jpg *.bmp)", options=options)
        if fileName:
            print(fileName)
            self.canvas.clearImage()
            self.image = QImage(fileName)

    def saveImage(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "Image Files (*.png *.jpg *.bmp)", options=options)
        if fileName:
            print(fileName)
            if ".png" not in fileName:
                fileName += ".png"

            self.canvas.saveCanvas(fileName)

