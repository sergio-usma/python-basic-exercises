class Person:
    def __init__(self, name, lastName, age, *info, **preferences):
        self.name = name
        self.last_name = lastName
        self.age = age
        self.info = info
        self.preferences = preferences

    def show_detail(self):
        print(f'Persona: {self.name} {self.last_name} {self.age} {self.info} {self.preferences}')


person1 = Person('John', 'Doe', 29, 'Married', 'Lawyer', 'Law&Order inc.', spouse='Whiskas Lopez', children=3, born='05-03-1995')
person1.show_detail()
print(person1.info[1])
print(person1.preferences['spouse'])
# Person.show_detail(person1)

person2 = Person('Jane', 'Doe', 33)
person2.show_detail()



