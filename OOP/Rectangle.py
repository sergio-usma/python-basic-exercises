class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return self.base * 2 + self.height * 2


base1 = int(input('Insert the base in meters: '))
height1 = int(input('Insert the height in meters: '))

rectangle1 = Rectangle(base1, height1)
print(f'The rectangle area is {rectangle1.area()} and the perimeter is {rectangle1.perimeter()}')
