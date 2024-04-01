class GeometricFigure:
    def __init__(self, length, height):
        self._length = length
        self._height = height

    @property
    def length(self):
        print('Implementing get method in length')
        return self._length

    @length.setter
    def length(self, length):
        print('Implementing set method in length')
        self._length = length

    @property
    def height(self):
        print('Implementing get method in height')
        return self._height

    @height.setter
    def height(self, height):
        print('Implementing set method in height')
        self._height = height








