from primitives.primitive import Primitive
from helpers.vertex import Vertex


class Line(Primitive):
    def __init__(self, position, color, qPen):
        Primitive.__init__(self, position, 2, color, qPen)
        self.secondP = position

    def draw(self, canvas):
        self.qPen.setColor(self.color)
        canvas.setPen(self.qPen)
        canvas.drawLine(
            self.position.x,
            self.position.y,
            self.secondP.x,
            self.secondP.y
        )

    def change(self, p):
        self.secondP = p
