from tkinter import ttk, filedialog
from tkinter import *

import cv2
from PIL import Image, ImageTk


def puntual_salida():
    resultado = puntual()
    resultado.save("resultadopuntual.tif")
    resultado.show()


def puntual():
    imagen_inicial = Image.open("test.png").convert("L")
    ancho, alto = imagen_inicial.size
    salida = Image.new("L", (ancho, alto))
    for i in range(imagen_inicial.size[0]):
        for j in range(imagen_inicial.size[1]):
            p = imagen_inicial.getpixel((i, j))
            q = 255 - p
            salida.putpixel((i, j), q)
    return salida


def vecindario():
    imagen_inicial = Image.open("test.png").convert("L")
    promedio = [[1 / 9, 1 / 9, 1 / 9],
                [1 / 9, 1 / 9, 1 / 9],
                [1 / 9, 1 / 9, 1 / 9]]
    img = filtrar3x3(imagen_inicial, promedio)
    img.save("resultadovecindario.tif")
    img.show()


def filtrar3x3(I=Image.open("test.png").convert("L"), M=[[1 / 9, 1 / 9, 1 / 9],
                                                         [1 / 9, 1 / 9, 1 / 9],
                                                         [1 / 9, 1 / 9, 1 / 9]]):
    Y = I
    alto, ancho = I.size
    k = len(M) // 2
    Ma = M[0][0]
    Mb = M[0][1]
    Mc = M[0][2]
    Md = M[1][0]
    Me = M[1][1]
    Mf = M[1][2]
    Mg = M[2][0]
    Mh = M[2][1]
    Mi = M[2][2]
    for x in range(k, alto - k, 1):
        for y in range(k, ancho - k, 1):
            la = float(I.getpixel((x - 1, y - 1)))
            lb = float(I.getpixel((x - 1, y)))
            lc = float(I.getpixel((x - 1, y + 1)))
            ld = float(I.getpixel((x, y - 1)))
            le = float(I.getpixel((x, y)))
            lf = float(I.getpixel((x, y + 1)))
            lg = float(I.getpixel((x + 1, y - 1)))
            lh = float(I.getpixel((x + 1, y)))
            li = float(I.getpixel((x + 1, y + 1)))
            q = int(la * Ma + lb * Mb + lc * Mc + ld * Md + le * Me + lf * Mf + lg * Mg + lh * Mh + li * Mi)
            Y.putpixel((x, y), q)
    return Y


def cargar_imagen():
    path_image = filedialog.askopenfilename()
    image = cv2.imread(path_image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(image)
    img = ImageTk.PhotoImage(image=im)
    ventana = Toplevel(root)
    canvas = Canvas(ventana)
    canvas.imageList = []
    canvas.create_image(0, 0, anchor="nw", image=img)
    canvas.imageList.append(img)
    canvas.pack()


def edge_demo():
    image = cv2.imread("test.png")
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_16SC1, 1, 0)
    grad_y = cv2.Sobel(gray, cv2.CV_16SC1, 0, 1)
    x_grad = cv2.convertScaleAbs(grad_x)
    y_grad = cv2.convertScaleAbs(grad_y)
    src1 = cv2.addWeighted(x_grad, 0.5, y_grad, 0.5, 0)
    edge = cv2.Canny(src1, 50, 100)
    cv2.imshow("Canny_edge_1", edge)


root = Tk()
root.configure(width=250, height=200)
root.title("Practica 2 - Berrio")
ttk.Label(root, text="Menu de navegación").place(x=20, y=20)
ttk.Button(root, text="Operador puntual", command=puntual_salida).place(x=20, y=50, width=200)
ttk.Button(root, text="Operador vecindad", command=vecindario).place(x=20, y=80, width=200)
ttk.Button(root, text="Operador con borde canny", command=edge_demo).place(x=20, y=110, width=200)
ttk.Button(root, text="Cerrar", command=root.destroy).place(x=20, y=140, width=200)
root.mainloop()
