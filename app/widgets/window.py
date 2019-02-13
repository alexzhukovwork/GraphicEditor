from PyQt5.QtWidgets import *
from widgets.window_view import WindowView

"""Callbacks for main window"""
class Window(WindowView):
    def __init__(self, width, height):
        WindowView.__init__(self, width, height)

    def onClickItem(self, func):
        def onClick():
            for i in self.tools:
                i.setDefaultStyle()

            func()

        return onClick

    def show(self):
        self.win.showMaximized()
