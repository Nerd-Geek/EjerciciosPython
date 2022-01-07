# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados 
# por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide 
# hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y 
# sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo 
# (minutos) alcanzará el vehículo más rápido al otro.

velocidadUno = float(input("Introduce la velocidad del primer coche: "))
velocidadDos = float(input("Introduce la velocidad del segundo coche: "))
distancia = float(input("Introduce la distancia entre los dos coches: "))
tiempo = distancia / (velocidadUno - velocidadDos)
tiempo *= 60
print("Lo alcanzará en",tiempo,"minutos")