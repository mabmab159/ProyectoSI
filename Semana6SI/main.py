import math
import random

X = [[1, 1, 1, 1], [1, -1, -1, 1], [-1, 1, 1, 1], [-1, -1, -1, 1]]
T = [[1, -1], [-1, 1], [1, -1], [-1, 1]]
W = [random.random() for i in range(24)]
U = [random.random() for i in range(6)]
n = 0.65
itera = -1
maxitera = 2500
minError = 0.1
Emc = 1000000


def f(x):
    return 1 / (1 + math.exp(-x))


def fprima(x):
    return f(x) * (1 - f(x))


while itera < maxitera and Emc > minError:
    itera = itera + 1
    Error = [0 for i in range(4)]
    for p in range(4):
        neta0 = X[p][0] * W[0] + X[p][1] * W[4] + X[p][2] * W[8] + X[p][3] * W[12] - U[0]
        neta1 = X[p][0] * W[1] + X[p][1] * W[5] + X[p][2] * W[9] + X[p][3] * W[13] - U[1]
        neta2 = X[p][0] * W[2] + X[p][1] * W[6] + X[p][2] * W[10] + X[p][3] * W[14] - U[2]
        neta3 = X[p][0] * W[3] + X[p][1] * W[7] + X[p][2] * W[11] + X[p][3] * W[15] - U[3]
        fneta0 = f(neta0)
        fneta1 = f(neta1)
        fneta2 = f(neta2)
        fneta3 = f(neta3)
        neta4 = fneta0 * W[16] + fneta1 * W[18] + fneta2 * W[20] + fneta3 * W[22] - U[4]
        neta5 = fneta0 * W[17] + fneta1 * W[19] + fneta2 * W[21] + fneta3 * W[23] - U[5]
        fneta4 = f(neta4)
        fneta5 = f(neta5)
        landa4 = (T[p][0] - fneta4) * fprima(4)
        landa5 = (T[p][1] - fneta5) * fprima(5)
        landa3 = fprima(neta3) * (landa5 * W[23] + landa4 * W[22])
        landa2 = fprima(neta2) * (landa5 * W[21] + landa4 * W[20])
        landa1 = fprima(neta1) * (landa5 * W[19] + landa4 * W[18])
        landa0 = fprima(neta0) * (landa5 * W[17] + landa4 * W[16])
        # actualizar los pesos de la capa oculta o la capa de salida
        W[23] = W[23] + n * landa5 * fneta3
        W[22] = W[22] + n * landa4 * fneta3
        W[21] = W[21] + n * landa5 * fneta2
        W[20] = W[20] + n * landa4 * fneta2
        W[19] = W[19] + n * landa5 * fneta1
        W[18] = W[18] + n * landa4 * fneta1
        W[17] = W[17] + n * landa5 * fneta0
        W[16] = W[16] + n * landa4 * fneta0
        # actualizar los pesos de la capa de entrada a la capa oculta
        W[0] = W[0] + n * landa0 * X[p][0]
        W[1] = W[1] + n * landa1 * X[p][0]
        W[2] = W[2] + n * landa2 * X[p][0]
        W[3] = W[3] + n * landa3 * X[p][0]
        W[4] = W[4] + n * landa0 * X[p][1]
        W[5] = W[5] + n * landa1 * X[p][1]
        W[6] = W[6] + n * landa2 * X[p][1]
        W[7] = W[7] + n * landa3 * X[p][1]
        W[8] = W[8] + n * landa0 * X[p][2]
        W[9] = W[9] + n * landa1 * X[p][2]
        W[10] = W[10] + n * landa2 * X[p][2]
        W[11] = W[11] + n * landa3 * X[p][2]
        W[12] = W[12] + n * landa0 * X[p][3]
        W[13] = W[13] + n * landa1 * X[p][3]
        W[14] = W[14] + n * landa2 * X[p][3]
        W[15] = W[15] + n * landa3 * X[p][3]
        # actualizar los umbrales
        U[5] = U[5] + n * landa5 * (-1)
        U[4] = U[4] + n * landa4 * (-1)
        U[3] = U[3] + n * landa3 * (-1)
        U[2] = U[2] + n * landa2 * (-1)
        U[1] = U[1] + n * landa1 * (-1)
        U[0] = U[0] + n * landa0 * (-1)
        # almacenar los errores
        Error[p] = 0.5 * (T[p][0] - fneta4) ** 2 + 0.5 * (T[p][1] - fneta5) ** 2
    Emc = Error[0] + Error[1] + Error[2] + Error[3]
    print(itera, " Error medio cuadratico : ", Emc)

print(" Los pesos sinapticos son: ")
print(W)
print(U)


def valor(x):
    if x > 0.5:
        return 1
    else:
        return -1


# realizar el mapeo o comprobación de lo aprendido
for p in range(4):
    neta0 = X[p][0] * W[0] + X[p][1] * W[4] + X[p][2] * W[8] + X[p][3] * W[12] - U[0]
    neta1 = X[p][0] * W[1] + X[p][1] * W[5] + X[p][2] * W[9] + X[p][3] * W[13] - U[1]
    neta2 = X[p][0] * W[2] + X[p][1] * W[6] + X[p][2] * W[10] + X[p][3] * W[14] - U[2]
    neta3 = X[p][0] * W[3] + X[p][1] * W[7] + X[p][2] * W[11] + X[p][3] * W[15] - U[3]
    fneta0 = f(neta0)
    fneta1 = f(neta1)
    fneta2 = f(neta2)
    fneta3 = f(neta3)
    neta4 = fneta0 * W[16] + fneta1 * W[18] + fneta2 * W[20] + fneta3 * W[22] - U[4]
    neta5 = fneta0 * W[17] + fneta1 * W[19] + fneta2 * W[21] + fneta3 * W[23] - U[5]
    fneta4 = f(neta4)
    fneta5 = f(neta5)
    print(fneta4, " ==> ", valor(fneta4), " ", fneta5, " ==> ", valor(fneta5))
