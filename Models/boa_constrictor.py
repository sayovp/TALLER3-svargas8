from Models.animal_exotico import AnimalExotico

class BoaConstrictor(AnimalExotico):
    def __init__(self, pais_origen: str, impuestos: float, nombre: str, edad: int, peso: float):
        super().__init__(pais_origen, impuestos, nombre, edad, peso)
        self.__ratones_comidos = 0

    def hacer_sonido(self)->str:
        return "¡Tsss!"
    
    def comer_raton(self)->None:
        if self.__ratones_comidos >= 20:
            raise ValueError("¡Demasiados Ratones!")
        self.__ratones_comidos =+1

    def comer_raton2(self)->None:
        if self.__ratones_comidos >= 10:
            raise ValueError("¡La boa está llena!")
        self.__ratones_comidos =+1  
       
    
    def dar_ratones_comidos(self)->int:
        return self.__ratones_comidos

    