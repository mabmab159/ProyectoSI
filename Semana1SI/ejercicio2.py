cantidadTotal = int(input("Ingrese la cantidad: "))
monedas = [5, 2, 1]
cantidadMonedas = []
for i in range(len(monedas)):
    cantidadMonedas.append(cantidadTotal // monedas[i])
    cantidadTotal %= monedas[i]
print(
    f"La cantidad de monedas a usarse")
for i in range(len(monedas)):
    print(f"Monedas de {monedas[i]} : {cantidadMonedas[i]}")
