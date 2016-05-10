#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Se importa el módulo unittest y math
import unittest
#Se importa la funcion Raiz del modulo raizcuadrada
from raizcuadrada import Raiz

class RaizTest(unittest.TestCase):

    def test_Raiz(self):
        """Test para la raiz de nueve que devuelve 3 que debe pasar."""
        self.assertEqual(3, Raiz(9))

    def test_zero(self):
        """Test para la raiz de 0 que devuelve 0, que debe pasar."""
        self.assertEqual(0, Raiz(0))

        
    def test_negative(self):
        """Test para la raiz de un número negativo, que debe fallar."""
        # Este debe devolver un ValueError, pero se espera un IndexError.
        self.assertRaises(IndexError, Raiz(-10))


if __name__ == '__main__':
    #Se ejecuta la prueba unitaria
    unittest.main()


