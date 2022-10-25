import math
import random

import pandas as pd


def mean_norm(df_input):
    return (df_input - df_input.min()) / (df_input.max() - df_input.min())


df2 = pd.read_csv("tae.data", header=None)
print()
normalizado = mean_norm(df2).to_numpy()

# Arreglo de datos inicial
X = normalizado[:, :5]
# Arreglo de datos de salida
T = normalizado[:, 5]
W = [random.random() for i in range(18)]
U = [random.random() for i in range(4)]
n = 0.65
itera = -1
maxitera = 1000000
minError = 0.1
Emc = 1000000


def f(x):
    return 1 / (1 + math.exp(-x))


def fprima(x):
    return f(x) * (1 - f(x))


while itera < maxitera and Emc > minError:
    itera = itera + 1
    Error = [0 for i in range(151)]
    for p in range(151):
        neta0 = X[p][0] * W[0] + X[p][1] * W[3] + X[p][2] * W[6] + X[p][3] * W[9] + X[p][4] * W[12] - U[0]
        neta1 = X[p][0] * W[1] + X[p][1] * W[4] + X[p][2] * W[7] + X[p][3] * W[10] + X[p][4] * W[13] - U[1]
        neta2 = X[p][0] * W[2] + X[p][1] * W[5] + X[p][2] * W[8] + X[p][3] * W[11] + X[p][4] * W[14] - U[2]
        fneta0 = f(neta0)
        fneta1 = f(neta1)
        fneta2 = f(neta2)
        neta3 = fneta0 * W[15] + fneta1 * W[16] + fneta2 * W[17] - U[3]
        fneta3 = f(neta3)
        landa3 = (T[p] - fneta3) * fprima(neta3)
        landa2 = fprima(neta2) * landa3 * W[17]
        landa1 = fprima(neta1) * landa3 * W[16]
        landa0 = fprima(neta0) * landa3 * W[15]
        # Actualizar los pesos de la capa oculta o de la capa de salida
        W[17] = W[17] + n * landa3 * fneta2
        W[16] = W[16] + n * landa3 * fneta1
        W[15] = W[15] + n * landa3 * fneta0
        # Actualizar los pesos de la capa de entrada o la capa oculta
        W[0] = W[0] + n * landa0 * X[p][0]
        W[1] = W[1] + n * landa1 * X[p][0]
        W[2] = W[2] + n * landa2 * X[p][0]
        W[3] = W[3] + n * landa0 * X[p][1]
        W[4] = W[4] + n * landa1 * X[p][1]
        W[5] = W[5] + n * landa2 * X[p][1]
        W[6] = W[6] + n * landa0 * X[p][2]
        W[7] = W[7] + n * landa1 * X[p][2]
        W[8] = W[8] + n * landa2 * X[p][2]
        W[9] = W[9] + n * landa0 * X[p][3]
        W[10] = W[10] + n * landa1 * X[p][3]
        W[11] = W[11] + n * landa2 * X[p][3]
        W[12] = W[12] + n * landa0 * X[p][4]
        W[13] = W[13] + n * landa1 * X[p][4]
        W[14] = W[14] + n * landa2 * X[p][4]
        # Actualizar los umbrales
        U[3] = U[3] + n * landa3 * (-1)
        U[2] = U[2] + n * landa2 * (-1)
        U[1] = U[1] + n * landa1 * (-1)
        U[0] = U[0] + n * landa0 * (-1)
        # Almacenar los errores
        Error[p] = 0.5 * (T[p] - fneta3) ** 2
    Emc = sum(Error) / 5
    print(itera, " Error medio cuadratico: ", Emc)
print("Los pesos sinapticos son: ")
print(W)
print(U)


def valor(x):
    if x >= 2 / 3:
        return 1
    elif x >= 1 / 3:
        return 0
    else:
        return -1


# Realizar el mapeo o comprobación de lo aprendido
resultados = []
for p in range(151):
    neta0 = X[p][0] * W[0] + X[p][1] * W[3] + X[p][2] * W[6] + X[p][3] * W[9] + X[p][4] * W[12] - U[0]
    neta1 = X[p][0] * W[1] + X[p][1] * W[4] + X[p][2] * W[7] + X[p][3] * W[10] + X[p][4] * W[13] - U[1]
    neta2 = X[p][0] * W[2] + X[p][1] * W[5] + X[p][2] * W[8] + X[p][3] * W[11] + X[p][4] * W[14] - U[2]
    fneta0 = f(neta0)
    fneta1 = f(neta1)
    fneta2 = f(neta2)
    neta3 = fneta0 * W[15] + fneta1 * W[16] + fneta2 * W[17] - U[3]
    fneta3 = f(neta3)
    resultados.append(valor(fneta3))
    print(fneta3, " ==> ", valor(fneta3))

# Calculo de estadisticas generales
suma = 0
for i in range(151):
    if int(resultados[i]) == df2.to_numpy()[i, 5] - 2:
        suma = suma + 1
print(f"El porcentaje de predicción actual es de: {suma} %")
