from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys
from widgets.canvas import Canvas
from widgets.item import Item
from widgets.palette_item import PaletteItem
from widgets.item_container import ItemContainer
from singleton.paint_settings import PaintSettings
from factories.palette_factory import PaletteFactory


def exceptHook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window:
    def __init__(self):
        self.height = QDesktopWidget().availableGeometry().height()
        self.width = QDesktopWidget().availableGeometry().width()
        self.win = QWidget()
        self.items = []
        self.__setupWindow()

    def __setupWindow(self):
        self.win.setStyleSheet("background-color:rgb(200,209,222);")
        self.win.setWindowTitle("PyQt")

        self.tools = self.__createTools(self.width * 0.04)
        toolContainerWidth = self.width * 0.07
        toolContainerHeight = self.height

        currentColor = PaletteItem(
            toolContainerWidth * 0.4,
            toolContainerWidth * 0.4,
            None,
            PaintSettings.currentColor
        )

        colorCurrentContainer = self.__createToolContainer(
            QHBoxLayout(),
            toolContainerWidth,
            toolContainerWidth,
            [
                currentColor
            ]
        )

        paletteItems = []
        for palette in PaletteFactory.createPalette(PaintSettings.paletteId):
            paletteItems.append(PaletteItem(
                toolContainerWidth * 0.2,
                toolContainerWidth * 0.2,
                None,
                palette,
                currentColor
            ))

        colorLayoutFirstColumn = self.__createToolContainer(
            QVBoxLayout(),
            0,
            0,
            paletteItems[0:int(len(paletteItems)/2)]
        )

        colorLayoutSecondColumn = self.__createToolContainer(
            QVBoxLayout(),
            0,
            0,
            paletteItems[int(len(paletteItems)/2):len(paletteItems) + 1]
        )

        colorLayout = self.__createToolContainer(
            QHBoxLayout(),
            toolContainerWidth,
            toolContainerWidth * 2,
            [colorLayoutFirstColumn, colorLayoutSecondColumn]
        )

        mainLayout = self.__createBox(
            QHBoxLayout(),
            0,
            0,
            self.width,
            self.height,
            (10, 10, 10, 50),
            [
                self.__createCanvas(self.width * 0.93, self.height),
                self.__createToolContainer(
                    QVBoxLayout(),
                    toolContainerWidth,
                    toolContainerHeight,
                    self.tools + [colorCurrentContainer, colorLayout]
                )
            ]
        )

        self.win.setLayout(
            mainLayout
        )

        c = QColor(22, 22, 22)
        print(c.getRgb())

    def __createBox(self, box, x, y, width, height, margins, widgets):
        box.setGeometry(QRect(x, y, width, height))
        box.setContentsMargins(*margins)

        for widget in widgets:
            box.addWidget(widget)

        return box

    def __createCanvas(self, width, height):
        canvas = Canvas(
            width,
            height
        )

        canvas.setFocusPolicy(Qt.StrongFocus)

        return canvas

    def __createToolContainer(self, layout, width, height, tools):
        toolContainer = ItemContainer(
            width,
            height
        )

        layout.setContentsMargins(0, 10, 0, 0)

        toolContainer.setWidgets(
            layout,
            tools
        )

        return toolContainer

    def onClickItem(self, func):
        def onClick():
            for i in self.tools:
                i.setDefaultStyle()

            func()

        return onClick


    def __createTools(self, size):
        return [
            Item(
                size, size,
                self.onClickItem(PaintSettings.selectRectangle),
                QtGui.QIcon(QtGui.QPixmap("../resources/rectangle.png"))
            ),
            Item(
                size, size,
                self.onClickItem(PaintSettings.selectTriangle),
                QtGui.QIcon(QtGui.QPixmap("../resources/triangle.png"))
            ),
            Item(
                size, size,
                self.onClickItem(PaintSettings.selectCircle),
                QtGui.QIcon(QtGui.QPixmap("../resources/circle.png"))
            ),
            Item(
                size, size,
                self.onClickItem(PaintSettings.selectLine),
                QtGui.QIcon(QtGui.QPixmap("../resources/line.png"))
            ),
            Item(
                size, size,
                self.onClickItem(PaintSettings.selectPen),
                QtGui.QIcon(QtGui.QPixmap("../resources/pen.png"))
            ),
            Item(
                size, size,
                self.onClickItem(PaintSettings.selectBrush),
                QtGui.QIcon(QtGui.QPixmap("../resources/brush.png"))
            ),
            Item(
                size, size,
                self.onClickItem(PaintSettings.selectEraser),
                QtGui.QIcon(QtGui.QPixmap("../resources/eraser.png"))
            ),
        ]

    def show(self):
        self.win.showMaximized()


if __name__ == '__main__':
    sys.excepthook = exceptHook
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
