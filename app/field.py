from exceptions.objects_count_error import ObjectsCountError
from primitives.pen import Pen
"""Class contains all primitives which are on the canvas"""
class Field:
    def __init__(self):
        self.objects = []
        self.currentObject = None

    def draw(self, canvas, alpha):
        for o in self.objects:
            o.draw(canvas, alpha)

    def clear(self):
        self.objects.clear()

    def addObject(self, o):
        self.objects.append(o)
        self.currentObject = self.objects[-1]

    def removeObject(self, o):
        self.objects.remove(o)


        #self.currentObject = self.objects[-1]

    def haveCurrentChanging(self):
        if self.currentObject is not None:
            return self.currentObject.isChange()

    def canCreate(self):
        canCreate = True

        if self.currentObject is not None:
            canCreate = not self.currentObject.isChange()

        return canCreate

    def onClick(self, p):
        if self.currentObject is not None and self.currentObject.isChange:
            self.currentObject.onClick(p)

    def onRelease(self, p):
        if self.currentObject is not None and self.currentObject.isChange:
            self.currentObject.onRelease(p)

    def onMove(self, p):
        if self.currentObject is not None and self.currentObject.isChange:
            self.currentObject.onMove(p)

    def getCurrent(self):
        if self.currentObject is None:
            raise ObjectsCountError

        return self.currentObject
