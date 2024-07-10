from ianimal import IAnimal

class AnimalGranja(IAnimal):
    def __init__(self, peso):
        self._peso = peso
        self._kilos_comidos = 0

    def obtener_peso(self):
        return self.__peso
    
    def comer(self, kilos):
        self.__kilos_comidos += (kilos*0.8)

    def obtener_kilos_comidos(self):
        return self._kilos_comidos