class Cube:
    def __init__(self, length, height, width ):
        self.length = length
        self.height = height
        self.width = width

    def calculate_volume(self):
        return self.length * self.height * self.width


length = int(input('Insert cube length: '))
height = int(input('Insert cube height: '))
width = int(input('Insert cube width: '))

cube1 = Cube(length, height, width)
print(f'The cube volume is {cube1.calculate_volume()}')


