# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
# C = (F-32)*5/9

fahrenheit = int(input("Introduce los grados Fahrenheit:"))

celsius = (fahrenheit - 32)* 5 / 9

print("Valor grados Celsius es:", celsius)