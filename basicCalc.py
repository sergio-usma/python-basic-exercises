print('Hello 👋! This is a basic calculator program')
number1 = int(input('Please insert first number: '))
number2 = int(input('Please insert second number: '))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = round((number1 / number2), 2)
divisionInt = number1 // number2  # Only returns the int part
module = number1 % number2
exponential = round((number1 ** number2), 2)

print(f'The addition of number is equal to: {addition:_^10}', type(addition))
print(f'The subtraction of number is equal to: {subtraction:_^10}', type(subtraction))
print(f'The multiplication of number is equal to: {multiplication:_^10}', type(multiplication))
print(f'The division of number is equal to: {division:_^10}', type(division))
print(f'The division (int) of number is equal to: {divisionInt:_^10}', type(divisionInt))
print(f'The module of {number1} divided by {number2} is equal to: {module:_^10}', type(module))
print(f'The exponential of {number1} raised to {number2}  is equal to: {exponential:_^10}', type(exponential))

print('Thank you for your time! 👋')
