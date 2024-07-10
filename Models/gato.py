from animal import Animal

class Gato(Animal):
    def __init__(self, nombre, raza, peso, edad, color):
        super().__init__(nombre, peso, edad)
        self.__color = color
    
    def hacer_sonido(self):
        return "¡Miau, miau!"
    
    def obtener_color(self):
        return self._color