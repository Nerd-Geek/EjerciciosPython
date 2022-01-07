# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

num = int(input("Introduce un número: "))

invertido = str(num)
print("El número invertido es:",invertido[1]+""+invertido[0])