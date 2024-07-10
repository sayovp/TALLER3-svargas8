from Models.animal_exotico import AnimalExotico

class Huron(AnimalExotico):
    def __init__(self, pais_origen: str, impuestos: float, nombre: str, edad: int, peso: float):
        super().__init__(pais_origen, impuestos, nombre, edad, peso)

    def hacer_sonido(self)->str:
        return "¡Eek Eek!"
