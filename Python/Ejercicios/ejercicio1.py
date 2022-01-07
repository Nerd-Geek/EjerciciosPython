# Dados los catetos de un triángulo, calcular su hipotenusa

import math

cateto1 = float(input("Introduce el cateto 1:"))
cateto2 = float(input("Introduce el cateto 2:"))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
print("La hipotenusa tiene: %.2f" % hipotenusa)
#print("La hipotenusa tiene:",hipotenusa)