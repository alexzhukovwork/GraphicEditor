from primitives.primitive import Primitive
from helpers.vertex import Vertex


class Line(Primitive):
    def __init__(self, position, color, qPen, qBrush=None):
        Primitive.__init__(self, position, 2, color, qPen, qBrush)
        self.secondP = position

    def draw(self, canvas, alpha):
        Primitive.draw(self, canvas, alpha)
        canvas.drawLine(
            self.position.x,
            self.position.y,
            self.secondP.x,
            self.secondP.y
        )

    def change(self, p):
        self.secondP = p
