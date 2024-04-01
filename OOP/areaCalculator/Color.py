class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        print('Implementing get method in color')
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'[Color: {self.color}]'


