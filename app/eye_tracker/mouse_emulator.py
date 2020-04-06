import pyautogui
from helpers.vertex import Vertex
import time
from PyQt5 import QtCore

"""Mouse emulator for eye tracker"""
class MouseEmulator:

    firstTimer = QtCore.QTimer()
    secondTimer = QtCore.QTimer()
    thirdTimer = QtCore.QTimer()
    mainWindow = None
    down = False

    @staticmethod
    def moveMouseTo(x, y):
        pyautogui.moveTo(x, y)

    @staticmethod
    def clickMouseAt():
        MouseEmulator.thirdTimer.stop()
        pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
        MouseEmulator.mainWindow.setupDefaultCursor()

    @staticmethod
    def downMouseAt():
        MouseEmulator.thirdTimer.stop()
        pyautogui.mouseDown(pyautogui.position()[0], pyautogui.position()[1])
        MouseEmulator.mainWindow.setupDefaultCursor()
        MouseEmulator.down = True

    @staticmethod
    def upMouseAt():
        MouseEmulator.thirdTimer.stop()
        pyautogui.mouseUp(pyautogui.position()[0], pyautogui.position()[1])
        MouseEmulator.clickMouseAt()
        MouseEmulator.mainWindow.setupDefaultCursor()
        MouseEmulator.down = False


    @staticmethod
    def mouseMoveEvent(e, mainWindow):

        MouseEmulator.mainWindow = mainWindow
        mainWindow.setupDefaultCursor()

        try:
            MouseEmulator.firstTimer.disconnect()
            MouseEmulator.secondTimer.disconnect()
            MouseEmulator.thirdTimer.disconnect()
        except:
            print("Failed")

   #     MouseEmulator.firstTimer.timeout.connect(mainWindow.setupFirstCursor)
   #     MouseEmulator.firstTimer.start(300)

   #     MouseEmulator.secondTimer.timeout.connect(mainWindow.setupSecondCursor)
   #     MouseEmulator.secondTimer.start(600)

   #     MouseEmulator.thirdTimer.timeout.connect(MouseEmulator.clickMouseAt)
   #     MouseEmulator.thirdTimer.start(600)

    @staticmethod
    def mouseMoveEventCanvas(e, mainWindow):

        MouseEmulator.mainWindow = mainWindow
        mainWindow.setupDefaultCursor()

        try:
            MouseEmulator.firstTimer.disconnect()
            MouseEmulator.secondTimer.disconnect()
            MouseEmulator.thirdTimer.disconnect()
        except:
            print("Failed")

   #     MouseEmulator.firstTimer.timeout.connect(mainWindow.setupFirstCursor)
   #     MouseEmulator.firstTimer.start(300)

    #    MouseEmulator.secondTimer.timeout.connect(mainWindow.setupSecondCursor)
    #    MouseEmulator.secondTimer.start(600)

   #     if not MouseEmulator.down:
    #        MouseEmulator.thirdTimer.timeout.connect(MouseEmulator.downMouseAt)
   #     else:
   #         MouseEmulator.thirdTimer.timeout.connect(MouseEmulator.upMouseAt)

    #    MouseEmulator.thirdTimer.start(600)



