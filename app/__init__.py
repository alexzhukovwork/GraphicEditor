from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys
from widgets.canvas import Canvas
from widgets.item import Item
from widgets.item_container import ItemContainer
from singleton.paint_settings import PaintSettings


def exceptHook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window:
    def __init__(self):
        self.items = []
        self.width = QDesktopWidget().availableGeometry().width()
        self.height = QDesktopWidget().availableGeometry().height()

        self.win = QWidget()
        self.win.setStyleSheet("background-color:rgb(200,209,222);")

        self.canvas = Canvas(
            self.width * 0.9,
            self.height
        )
        self.canvas.setFocusPolicy(Qt.StrongFocus)

        self.vBox = QHBoxLayout()
        self.vBox.setGeometry(QRect(0, 0, self.width, self.height))

        self.vBox.addWidget(self.canvas)

        self.itemContainer = ItemContainer(
            self.width * 0.1,
            self.height
        )

        self.vBox.setContentsMargins(10, 10, 10, 50)

        self.vBox.addWidget(self.itemContainer)

        self.initItems()
        self.itemContainer.setWidgets(
            *self.items
        )

        self.win.setLayout(self.vBox)
        self.win.setWindowTitle("PyQt")

    def onClickItem(self, func):
        def onClick():
            for i in self.items:
                i.setDefaultStyle()

            func()

        return onClick

    def initItems(self):
        self.items = [
            Item(
                self.itemContainer.geometry().width() * 0.4, self.itemContainer.geometry().width() * 0.4,
                self.onClickItem(PaintSettings.selectRectangle),
                QtGui.QIcon(QtGui.QPixmap("../resources/rectangle.png"))
            ),
            Item(
                self.itemContainer.geometry().width() * 0.4, self.itemContainer.geometry().width() * 0.4,
                self.onClickItem(PaintSettings.selectTriangle),
                QtGui.QIcon(QtGui.QPixmap("../resources/triangle.png"))
            ),
            Item(
                self.itemContainer.geometry().width() * 0.4, self.itemContainer.geometry().width() * 0.4,
                self.onClickItem(PaintSettings.selectCircle),
                QtGui.QIcon(QtGui.QPixmap("../resources/circle.png"))
            ),
            Item(
                self.itemContainer.geometry().width() * 0.4, self.itemContainer.geometry().width() * 0.4,
                self.onClickItem(PaintSettings.selectLine),
                QtGui.QIcon(QtGui.QPixmap("../resources/line.png"))
            ),
            Item(
                self.itemContainer.geometry().width() * 0.4, self.itemContainer.geometry().width() * 0.4,
                self.onClickItem(PaintSettings.selectPen),
                QtGui.QIcon(QtGui.QPixmap("../resources/pen.png"))
            ),
            Item(
                self.itemContainer.geometry().width() * 0.4, self.itemContainer.geometry().width() * 0.4,
                self.onClickItem(PaintSettings.selectBrush),
                QtGui.QIcon(QtGui.QPixmap("../resources/brush.png"))
            ),
            Item(
                self.itemContainer.geometry().width() * 0.4, self.itemContainer.geometry().width() * 0.4,
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
