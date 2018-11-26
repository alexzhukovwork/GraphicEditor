from primitives.primitive import Primitive


class Circle(Primitive):
    def __init__(self, position, color, qPen):
        Primitive.__init__(self, position, 2, color, qPen)
        self.radius = 0

    def draw(self, canvas):
        self.qPen.setColor(self.color)
        canvas.setPen(self.qPen)
        canvas.drawEllipse(
            self.position.x - self.radius / 2,
            self.position.y - self.radius / 2,
            self.radius,
            self.radius
        )

    def change(self, p):
        self.radius = self.position.calculateDistance(p)

