#Calcular el perímetro y área de un rectángulo dada su base y su altura.

import math

base = float(input("Indique la base del rectángulo:"))
altura = float(input("Indique la altura del rectángulo:"))

perimetro = altura + base
print("El perímetro del rectángulo es %.2f" % perimetro)

area = base * altura
print("El area del rectángulo es %.2f" % area)