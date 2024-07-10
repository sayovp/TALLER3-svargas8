import unittest
from Models.boa_constrictor import BoaConstrictor

class TestBoaConstrictor(unittest.TestCase):
    def test_hacer_sonido(self)->str:
        boa1 = BoaConstrictor("Venezuela", 2000, "Diego", 3, 80)
        self.assertEqual(boa1.hacer_sonido(),"¡Tsss!")

    def test_calcular_flete(self):
        boa1 = BoaConstrictor("Venezuela", 2000, "Diego", 3, 80)
        self.assertEqual(boa1.calcular_flete(),160000)

    def test_comer_raton(self)->None:
        boa1 = BoaConstrictor("Venezuela", 2000, "Diego", 3, 80)
        try:
            for x in range(10):
                boa1.comer_raton()
                self.assertEqual(boa1.dar_ratones_comidos(),1)
        except ValueError as e:
                self.assertEqual(str(e), "¡Demasiados Ratones!")
