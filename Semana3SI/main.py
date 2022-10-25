from PIL import Image
import numpy as np

imgGray = Image.open("huella.tif").convert("L")
img = np.array(imgGray)


def adelgazamiento(matriz):
    for i in range(len(matriz) - 2):
        for j in range(len(matriz) - 2):
            M = matriz[i:i + 3, j:j + 3]
            if (sum(M[0, :]) == 0 and sum(M[2, :]) == 3) \
                    or (sum(M[2, :]) == 0 and sum(M[0, :]) == 3) \
                    or (sum(M[:, 0]) == 0 and sum(M[:, 2]) == 3) \
                    or (sum(M[:, 2]) == 0 and sum(M[:, 0]) == 3) \
                    or (int(M[1, 0]) + int(M[2, 1]) == 2 and int(M[0, 1]) + int(M[0, 2]) + int(M[1, 2]) == 0) \
                    or (int(M[1, 0]) + int(M[0, 1]) == 2 and int(M[2, 1]) + int(M[1, 2]) + int(M[2, 2]) == 0) \
                    or (int(M[0, 1]) + int(M[1, 2]) == 2 and int(M[1, 0]) + int(M[2, 1]) + int(M[2, 0]) == 0) \
                    or (int(M[1, 0]) + int(M[2, 1]) == 2 and int(M[0, 1]) + int(M[0, 2]) + int(M[1, 2]) == 0) \
                    or (sum(M[0, :]) + sum(M[:, 2]) + M[1, 0] == 0) \
                    or (sum(M[0, :]) + sum(M[:, 0]) + M[1, 2] == 0):
                M[1, 1] = 0
            for x in range(3):
                for z in range(3):
                    img[x][z] = M[x][z]


def conteo(matriz):
    terminacion = 0
    bifurcacion = 0
    for i in range(len(matriz) - 2):
        for j in range(len(matriz) - 2):
            M = matriz[i:i + 3, j:j + 3]
            if sum(sum(M)) == 2 and int(M[1, 1]) and (int(M[0, 0]) + int(M[2, 0]) + int(M[0, 2]) + int(M[2, 2]) == 1):
                terminacion = terminacion + 1
            elif sum(sum(M)) == 4 and int(M[1, 1]) == 1 and (int(M[0, 0]) + int(M[2, 0]) + int(M[2, 2]) == 3) or (
                    int(M[0, 0]) + int(M[2, 0]) + int(M[0, 2]) == 3) or (
                    int(M[0, 0]) + int(M[0, 2]) + int(M[2, 2]) == 3) or (
                    int(M[0, 2]) + int(M[2, 0]) + int(M[2, 2]) == 3):
                bifurcacion = bifurcacion + 1
    print(f"La imagen tiene {terminacion} terminaciones")
    print(f"La imagen tiene {bifurcacion} bifurcaciones")


for i in range(imgGray.size[0]):
    for j in range(imgGray.size[1]):
        valor = img[i][j]
        if valor > 128:
            img[i][j] = 1
        else:
            img[i][j] = 0

for i in range(16):
    print(f"Iteracion {i + 1}")
    adelgazamiento(img)
    conteo(img)
test1 = Image.fromarray(img * 255)
test1.show()
