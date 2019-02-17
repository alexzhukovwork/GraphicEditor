from primitives.primitive import Primitive
from helpers.vertex import Vertex


class Rectangle(Primitive):
    def __init__(self, position, color, qPen, qBrush=None):
        Primitive.__init__(self, position, 2, color, qPen, qBrush)
        self.width = 0
        self.height = 0

    def draw(self, canvas, alpha):
        Primitive.draw(self, canvas, alpha)

        canvas.drawRect(
            self.position.x,
            self.position.y,
            self.width,
            self.height
        )

    def change(self, p):
        self.width =  p.x - self.position.x
        self.height = p.y - self.position.y
