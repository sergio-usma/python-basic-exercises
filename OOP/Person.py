class Person:
    def __init__(self, name, lastName, age):
        self.name = name
        self.lastName = lastName
        self.age = age


nombre = input('Insert your name: ')
apellido = input('Insert your last name: ')
edad = int(input('Insert your age: '))

person1 = Person(nombre, apellido, edad)
print(person1.name, end=' ')
print(person1.lastName)
print(person1.age)





