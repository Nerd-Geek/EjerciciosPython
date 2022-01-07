# Diseñar un algoritmo que nos diga el dinero que tenemos 
# (en euros y céntimos) después de pedirnos cuantas monedas 
# tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

euro2 = int(input("Monedas de 2 euros: "))
euro1 = int(input("Monedas de 1 euro: "))
cent50 = int(input("Monedas de 50 céntimos: "))
cent20 = int(input("Monedas de 20 centimos: "))
cent10 = int(input("Monedas de 10 centimos: "))

totalEuros = euro2 * 2 + euro1
totalCentimos = cent50 * 50 + cent20 * 20 + cent10 * 10
totalEuros = totalEuros + totalCentimos // 100
totalCentimos = totalCentimos %100
print(totalEuros,"euros y",totalCentimos,"céntimos")