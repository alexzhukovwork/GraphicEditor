from widgets.item import Item
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QColor
from singleton.paint_settings import PaintSettings

class PaletteItem(Item):
    currentColor = QColor(0, 0, 0)

    def __init__(self, width, height, onClick, color, main=None):
        Item.__init__(self, width, height, onClick)
        self.color = color
        self.main = main
        self.__setStyle()
        self.installEventFilter(self)

    def eventFilter(self, qobject, event):
        if self.main is not None:
            if event.type() == QEvent.HoverEnter:
                style = "border:5px solid rgb(0,255,0); background-color:rgba{};".format(self.color.getRgb())
                self.setStyleSheet(style)
            if event.type() == QEvent.HoverLeave:
                self.__setStyle()

        return Item.eventFilter(self, qobject, event)

    def __setStyle(self):
        style = "border:5px solid rgb(200,209,222); background-color:rgba{};"\
            .format(self.color.getRgb())
        self.setStyleSheet(style)

    def setStyle(self, color):
        style = "border:5px solid rgb(200,209,222); background-color:rgba{};" \
            .format(color.getRgb())
        self.setStyleSheet(style)

    def onClickEvent(self):
        if self.main is not None:
            PaintSettings.currentColor = self.color
            self.main.setStyle(self.color)
            if self.onClick is not None:
                self.onClick()
