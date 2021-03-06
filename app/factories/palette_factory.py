from PyQt5.QtGui import QColor

"""Static class for creating different palettes"""
class PaletteFactory:

    FIRST = 1
    SECOND = 2
    THIRD = 3
    FIFTH = 4
    SIXTH = 5

    def __init__(self):
        pass

    @staticmethod
    def createPalette(id):
        return {
            PaletteFactory.FIRST: [
                QColor(255, 0, 0),
                QColor(0, 255, 0),
                QColor(0, 0, 255),
                QColor(0, 0, 0),
                QColor(255, 255, 255),
                QColor(255, 255, 0),
                QColor(255, 0, 255)
            ]
        }[id]


