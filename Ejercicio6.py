""" Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo con tantos renglones como indique el
usuario. """

import random
renglonesTriangulo = int(input("Ingrese la cantidad de renglones del tríangulo Rectángulo:"));
for i in range(1,renglonesTriangulo + 1):
    print(str(random.randint(0,9))*i);