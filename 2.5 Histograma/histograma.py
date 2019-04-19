#//////////////////////////////////////
#//Histograma
#//Autor: Bryan Medina
#/////////////////////////////////////


import cv2
import numpy as np
import matplotlib.pyplot as plt

#imagen de entrada
f = cv2.imread('zorro.jpg', 0)

def histograma(sourceImage):
    """calculo del histograma, la cual regresa el eje x con 256 valores de intensidad
    y la frecuencia de estos en la imagen, es decir, el histograma beibe"""

    #inicializacion del histograma y de los 256 de intensidad
    hist = np.zeros(256)
    x = np.array(range(256))

    #iteraremos sobre cada pixel de la imagen
    width, height = sourceImage.shape

    for i in range(width):
        for j in range(height):
            brillo = f[i, j]
            #aumentamos en 1 el nivel de brillo del pixel actual
            hist[brillo] += 1

    return x, hist


x, histF = histograma(f)

plt.figure()
plt.plot(x, histF)
plt.xlabel('niveles de intensidad')
plt.ylabel('número de pixeles')
plt.title('histograma')
plt.show()

# y buuuueeeno, tambien se puede usar la funcion de opencv y de numpy, ya cada quien
numpyHistogram, bins = np.histogram(f, 256, [0, 256])
opencvHistogram = cv2.calcHist([f], [0], None, [256], [0, 256])

plt.figure()
plt.plot(x, opencvHistogram)
plt.xlabel('niveles de intensidad')
plt.ylabel('número de pixeles')
plt.title('histograma')
plt.show()
