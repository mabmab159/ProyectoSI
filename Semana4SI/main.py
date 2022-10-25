from PIL import Image
import numpy as np

imgGray = Image.open("placa12.png").convert("L")
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
    for i in range(len(matriz) - 13):
        for j in range(len(matriz) - 13):
            M = matriz[i:i + 14, j:j + 14]
            if int(M[13, 0]) + int(M[12, 1]) + int(M[11, 2]) + int(M[10, 3]) + sum(M[9, 4:7]) + int(M[10, 7]) + sum(
                    M[11, 8:11]) + sum(M[12:14, 10]) == 12 and sum(sum(M)) == 12:
                terminacion = terminacion + 1
            elif int(M[13, 0]) + int(M[12, 1]) + int(M[11, 2]) + int(M[10, 3]) + sum(M[9, 4:9]) + int(M[10, 9]) + sum(
                    M[11, 10:12]) + int(M[12, 12]) + int(M[13, 13]) == 14 and sum(sum(M)) == 14:
                terminacion = terminacion + 1
    print(f"La imagen tiene {terminacion} letras A")


for i in range(imgGray.size[0]):
    for j in range(imgGray.size[1]):
        valor = img[i][j]
        if valor > 128:
            img[i][j] = 1
        else:
            img[i][j] = 0

for i in range(10):
    print(f"Iteracion {i + 1}")
    adelgazamiento(img)
conteo(img)
test1 = Image.fromarray(img * 255)
test1.show()
