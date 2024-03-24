print('\nHi!👋 Welcome to Interval Number Checker!!')

firstNumber = 0
secondNumber = 10
number = int(input('\nInsert a number for checking!: '))

if firstNumber <= number <= secondNumber:
    print(f'\nThe number {number} is between the range! ✅')
else:
    print(f'\nThe number {number} is not between the range! ❌')
