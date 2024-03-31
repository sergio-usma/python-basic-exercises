from Encapsulation import Person


print('Create a new object'.center(50, '-'))
person1 = Person('Sergio', 'Usma', 28)
person1.show_detail()

print('\n', 'Delete objects'.center(50, '-'))
del person1
