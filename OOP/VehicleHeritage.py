class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'[Color: {self.color}, Ruedas: {self.ruedas}]'


class Coche(Vehiculo):
    def __init__(self, velocidad, color, ruedas):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'[Velocidad: {self.velocidad} km/h] {super().__str__()}'


class Bicicleta(Vehiculo):
    def __init__(self, tipo, color, ruedas):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'[Tipo: {self.tipo}] {super().__str__()}'


newCoche = Coche(120, 'Red', 4)
print(newCoche)

newBicicleta = Bicicleta('Montaña','Red', 2)
print(newBicicleta)
