class Person:
    def __init__(self, name, lastName, age):
        self.name = name
        self.last_name = lastName
        self.age = age

    def show_detail(self):
        print(f'Persona: {self.name} {self.last_name} {self.age}')


person1 = Person('John', 'Doe', 29)
person1.show_detail()
person1.telephone = '42313'
# Person.show_detail(person1)
print(person1.telephone)

person2 = Person('Jane', 'Doe', 33)
person2.show_detail()



