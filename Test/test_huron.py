import unittest
from Models.huron import Huron

class TestHuron(unittest.TestCase):
    def test_hacer_sonido(self)->str:
        huron1 = Huron("Colombia", 5000, "Carlitos", 5, 30)
        self.assertEqual(huron1.hacer_sonido(),"¡Tsss!")

    def test_calcular_flete(self):
        huron1 = Huron("Colombia", 5000, "Carlitos", 5, 30)
        self.assertEqual(huron1.calcular_flete(),160000)