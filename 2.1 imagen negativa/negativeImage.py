
import numpy as np
import matplotlib.pyplot as plt
import cv2

#lectura de la imagen de entrada
img = cv2.imread('chest.jpg', cv2.IMREAD_GRAYSCALE)

def grafica(x, y, titulo):
    """funcion para graficar los niveles de intensidad (256) de la imagen de
    entrada respecto a la de salida"""
    plt.figure()
    plt.plot(x, y, 'r'); plt.title(titulo)
    plt.xlabel('brillo - imagen de entrada f(x, y)')
    plt.ylabel('brillo - imagen de salida g(x, y)')
    plt.show()

def imagenComplemento(sourceImage):
    """ Obtener la imagen complementaria (negativa) a partir de una
    imagen de entrada"""
    outputImage = 255 - sourceImage
    return outputImage

#valores de los niveles de intensidad de la imagen, para determinar la grafica de la funcion T
#en este caso la img de entrada es igual a la salida.
x1 = np.array(range(256))
y1 = x1
grafica(x1, y1, 'g(x, y) = f(x, y)')

#imagen negativa (inversa)
x2 = np.array(range(256))
y2 = 255 - x2
grafica(x2, y2, 'g(x, y) = 255 - f(x, y)')

negativa = imagenComplemento(img)

# #mostrar la imagen de entrada
cv2.imshow('normal', img)
# #mostrar la imagen complementaria
cv2.imshow('negativa', negativa)
cv2.waitKey(0)
cv2.destroyAllWindows()
