from GeometricFigure import GeometricFigure
from Color import Color


class Square(GeometricFigure, Color):
    def __init__(self, length, height, color):
        # super().__init__()
        GeometricFigure.__init__(self, length, height)
        Color.__init__(self, color)

    def cal_area(self):
        return self.length * self.height

    def __str__(self):
        return f'{Color.__str__(self)} {GeometricFigure.__str__(self)}'


if __name__ == '__main__':
    squareX = Square(2, 3, 'Red')
    print(squareX)
