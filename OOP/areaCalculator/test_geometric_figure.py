from Square import Square
from Rectangle import Rectangle


print('Create object Square'.center(50, '-'))
square1 = Square(5, 4, 'red')
print(f'Square area: {square1.cal_area()}')
print(square1)

print('Create object Rectangle'.center(50, '-'))
rectangle1 = Rectangle(6, 7, 'blue')
print(f'Square area: {rectangle1.cal_area()}')
print(rectangle1)

