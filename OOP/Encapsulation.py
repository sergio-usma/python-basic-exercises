class Person:
    def __init__(self, name, lastName, age):
        self._name = name
        self._last_name = lastName
        self._age = age

    @property  # Allows to access the method as where a property, without need of parenthesis
    def name(self):
        print('Implementing get method in name')
        return self._name

    # For 'Only-Read variables -rm te setter method below
    @name.setter  # Allows to edit private _name property
    def name(self, name):
        print('Implementing set method in name')
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, lastName):
        self._last_name = lastName

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def show_detail(self):
        print(f'Persona: {self._name} {self._last_name} {self._age}')


if __name__ == '__main__':  # Only for local execution
    person1 = Person('John', 'Doe', 29)
    print(person1.name)  # Call the method "name" without parenthesis because of @property decorator
    person1.show_detail()
    person1.name = "Juan Carlos"  # Edit prop using setter
    person1.last_name = "Lara"  # Edit prop using setter
    person1.age = 33  # Edit prop using setter
    person1.show_detail()
    # Person.show_detail(person1)

    print(__name__)  # Print the name of the current module or file
