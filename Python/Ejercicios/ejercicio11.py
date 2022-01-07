# Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

import math

num1 = int(input("Introduce el valor:"))
num2 = int(input("Introduce el valor:"))

distancia = abs(num1 - num2)

print("La distancia entre",num1,"y",num2,"es:",distancia)