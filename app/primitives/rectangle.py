from primitives.primitive import Primitive
from helpers.vertex import Vertex


class Rectangle(Primitive):
    def __init__(self, position, color, qPen):
        Primitive.__init__(self, position, 2, color, qPen)
        self.width = 0
        self.height = 0

    def draw(self, canvas):
        self.qPen.setColor(self.color)
        canvas.setPen(self.qPen)
        canvas.drawRect(
            self.position.x,
            self.position.y,
            self.width,
            self.height
        )

    def change(self, p):
        self.width =  p.x - self.position.x
        self.height = p.y - self.position.y
