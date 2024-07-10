from Models.animal import Animal

class Perro(Animal):
    def __init__(self, nombre, raza, peso, edad):
        super().__init__(nombre, peso, edad)
        self.__raza = raza
    
    def hacer_sonido(self):
        return "¡Guau, Guau!"
    
    def obtener_raza(self):
        return self._raza