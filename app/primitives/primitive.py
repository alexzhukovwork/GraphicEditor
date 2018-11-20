class Primitive:
    def __init__(self, position, clickCountMax, color):
        self.position = position
        self.color = color
        self.clickCountMax = clickCountMax
        self.clickCount = 0
        self.canChange = True

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

    def onMove(self, p):
        if self.clickCount < self.clickCountMax:
            self.change(p)
