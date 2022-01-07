# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir 
# un algoritmo que determine la hora de llegada a la ciudad B.

horaPartida = int(input("Introduce la hora de salida: "))
minPartida = int(input("Introduce los minutos de salida: "))
segPartida = int(input("Introduce los segundos de salida: "))
segViaje = int(input("Introduce el tiempo que has tardado en el viaje: "))

segInicial = horaPartida * 3600 + minPartida * 60 + segPartida

segFinal = segInicial + segViaje

horaLlegada = segFinal // 3600
minLlegada = (segFinal % 3600) // 60
segLlegada = (segFinal % 3600) % 60

print("La hora de llegada es:")
print(horaLlegada,":",minLlegada,":",segLlegada)