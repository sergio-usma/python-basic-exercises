class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: [Nombre: {self.nombre} Edad: {self.edad}]'


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'[Sueldo: {self.sueldo}] {super().__str__()}'


if __name__ == '__main__':
    empleado1 = Empleado('Juan', 28, 5000)
    print(empleado1)
