numeros = []
for i in range(3):
    numeros.append(int(input(f"Ingrese el numero {i + 1} : ")))
numeros.sort()
print(f"El numero menor es {numeros[0]}")
print(f"El numero central es {numeros[1]}")
print(f"El numero mayor es {numeros[2]}")
