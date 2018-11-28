from PyQt5.QtCore import Qt

class Primitive:
    def __init__(self, position, clickCountMax, color=Qt.black, qPen=None, qBrush=None):
        self.position = position
        self.color = color
        self.clickCountMax = clickCountMax
        self.clickCount = 0
        self.canChange = True
        self.qPen = qPen
        self.qBrush = qBrush

    def onClick(self, p):
        self.clickCount += 1

        if self.clickCount == self.clickCountMax:
            self.canChange = False
        else:
            self.change(p)

    def isChange(self):
        return self.canChange

    def change(self, p):
        pass

    def onRelease(self, p):
        pass

    def onMove(self, p):
        if self.canChange:
            self.change(p)

    def draw(self, canvas):
        self.qPen.setColor(self.color)
        canvas.setPen(self.qPen)

        if self.qBrush is not None:
            canvas.setBrush()
