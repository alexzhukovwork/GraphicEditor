import sys
import threading
from widgets.window import Window
from PyQt5.QtWidgets import *
import time
from eye_tracker.mouse_emulator import MouseEmulator


def exceptHook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def mouse():
    for i in range(0, 1000):
        MouseEmulator.moveMouseTo(1920 - i, 200)
        MouseEmulator.clickMouseAt(1920 - i, 200)
        time.sleep(0.1)


"""Start point"""
if __name__ == '__main__':
    sys.excepthook = exceptHook
    app = QApplication(sys.argv)
    w = Window(QDesktopWidget().availableGeometry().width(), QDesktopWidget().availableGeometry().height())
    w.show()

    #  t = threading.Thread(target=mouse)
    # t.daemon = True
    # t.start()
    sys.exit(app.exec_())
