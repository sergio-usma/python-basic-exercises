from GeometricFigure import GeometricFigure
from Color import Color


class Square(GeometricFigure, Color):
    def __init__(self, length, height, color):
        # super().__init__()
        GeometricFigure.__init__(self, length, height)
        Color.__init__(self, color)

    def cal_area(self):
        return self.length * self.height

