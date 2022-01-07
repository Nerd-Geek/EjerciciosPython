# Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

primera_nota = float(input("Introduce la primera nota examen parcial:"))
segunda_nota = float(input("Introduce la segunda nota examen parcial:"))
tercera_nota = float(input("Introduce la tercera nota examen parcial:"))

promedio_parcial = (primera_nota + segunda_nota + tercera_nota) / 3
total_parcial = promedio_parcial * 5.5

examen_final = float(input("Introduce la nota del examen final:"))
total_examen_final = examen_final * 3

trabajo_final = float(input("Introduce la nota del trabajo:"))
total_trabajo_final = trabajo_final * 1.5

nota = (total_parcial + total_examen_final + total_trabajo_final)/10

print("La nota del alumno es:",nota)