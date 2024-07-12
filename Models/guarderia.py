from Models.boa_constrictor import BoaConstrictor
from Models.huron import Huron

class Guarderia():
    def __init__(self, lista_animales):
        self.lista_animales = []

    def agregar_animal(self,animal):
        boaCantidad = 0
        huronCnatidad =0

        for animalLista in self.lista_animales:
            if isinstance(animalLista,BoaConstrictor):
                boaCantidad =+1
            else:
                huronCnatidad =+1
        
        try:
            if isinstance(animalLista,BoaConstrictor) and boaCantidad == 2:
                raise ValueError("maximo de boas")
            elif isinstance(animalLista,Huron) and huronCnatidad == 2:
                raise ValueError("maximo de Huron")
        
            self.lista_animales.append(animal)
        except ValueError as e:
            print(e)

    def alimentar_boa(self, boa):
        try:
            if boa in self.lista_animales:
                boa.comer_raton2()
            else :
                raise ValueError("Esta Boa no existe!")
            return "Éxito"
        except ValueError as e:
            print(e)