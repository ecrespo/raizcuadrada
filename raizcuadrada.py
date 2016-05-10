#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Se importa el módulo math para calcular la raiz cuadrada.
"""
import math


#Función raiz cuadrada.
def Raiz(a):
    """Si a es mayor o igual a cero se calcula la raiz cuadrada"""
    if a >= 0:
        return math.sqrt(a)
    #Si es menor a cero se genera una excepción donde se informa que a debe ser mayor o igual a cero.
    else:
        raise ValueError("a debe ser >= 0")


if __name__ == '__main__':
    #Se importa el módulo doctest
    import doctest
    #Se realiza la prueba al archivo raizcuadra.txt
    doctest.testfile("raizcuadrada.txt")
