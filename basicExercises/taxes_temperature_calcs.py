# # Taxes Calculator
# def taxCalc(value, taxes):
#     return value + (value * (taxes / 100))
#
#
# cost = float(input('Enter the value without taxes: '))
# tax = float(input('Enter the tax percentage: '))
# total = taxCalc(cost, tax)
# print(f'The total value is {total}')

# Temperature converter
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def farenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


celsius = float(input('Insert your value in celsius: '))
result = celsius_fahrenheit(celsius)
print(f'{celsius}C a F: {result:.2f}')

fahrenheit = float(input('Insert your value in fahrenheit: '))
result = farenheit_celsius(fahrenheit)
print(f'{fahrenheit}C a F: {result:.2f}')

