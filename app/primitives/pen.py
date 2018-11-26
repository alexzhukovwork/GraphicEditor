from primitives.primitive import Primitive


class Pen(Primitive):
    def __init__(self, position, color, qPen):
        Primitive.__init__(self, position, -1, color, qPen)
        self.pixels = []


    def draw(self, canvas):
        self.qPen.setColor(self.color)
        canvas.setPen(self.qPen)

        len = self.pixels.__len__() - 1

        for i in range(0, len):
            current = self.pixels[i]
            next = self.pixels[i+1]
            canvas.drawLine(current.x, current.y, next.x, next.y)

    def change(self, p):
        self.pixels.append(p)

    def click(self, p):
        self.canChange = True

    def onRelease(self, p):
        self.canChange = False
