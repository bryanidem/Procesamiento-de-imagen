#//////////////////////////////////////
#//Transformacion lineal por partes
#//Autor: Bryan Medina
#//////////////////////////////////////

import cv2
import numpy as np
import matplotlib.pyplot as plt

f = cv2.imread('C:/Users/bryan/Desktop/image processing python/data/pelvis.jpg', 0)

#defino los puntos (r1, s1), (r2, s2) que formarán la recta que mapeará el rango dinámico de la imagen de entrada, en una de mayor constraste

r1 = 80
s1 = 0
r2 = 175
s2 = 255

#pendientes de las rectas
a = (s1/r1)
b = (s2-s1)/(r2-r1)
c = (255-s2)/(255-r2)

#definición de las rectas
x1 = np.array(range(r1))
y1 = a * x1

x2 = np.array(range(r1,r2+1))
y2 = b * (x2 - r1) + a * r1

x3 = np.array(range(r2, 256))
y3 = c * (x3 - r2) + b * (r2 - r1) + a * r1


width, height = f.shape
g = np.zeros((width, height), np.uint8)

#asigno los nuevos valores que tendrá la imagen de salida
for i in range(width):
    for j in range(height):
        if(f[i, j] >= 0 and f[i, j] <= r1):
            g[i, j] = a * f[i, j]

        elif(f[i, j] > r1 and f[i, j] <= r2):
            g[i, j] = b * ((f[i, j] - r1) + (a * r1))

        else:
            if(f[i, j] > r2 and f[i, j] <= 255):
                g[i, j] = c * (f[i, j] - r2) + b * (r2 - r1) + a * r1




#grafica donde se muestra la funcion de transformacion
plt.figure()
plt.plot(x1, y1, 'r')
plt.plot(x2, y2, 'g')
plt.plot(x3, y3, 'b')
plt.xlabel('intensidades imagen de entrada')
plt.ylabel('intensidades imagen de salida')
plt.title('mapeo de intensidades')

#histograma para visualizar los valores de brillo min y max que presenta la imagen
fHist, bins = np.histogram(f, 256, [0, 256])
fHist = fHist/(width*height)

#histograma para visualizar el efecto de la transformación
gHist, bins = np.histogram(g, 256, [0, 256])
gHist = gHist/(width*height)

x = np.array(range(256))

#mostrar histogramas
plt.figure()
plt.bar(x, fHist)
plt.xlabel('niveles de intensidad')
plt.ylabel('ocurrencia')
plt.title('histograma de f')

plt.figure()
plt.bar(x, gHist)
plt.xlabel('niveles de intensidad')
plt.ylabel('ocurrencia')
plt.title('histograma de g')
plt.show()

#mostras imagenes de entrada y salida
cv2.imshow('f', f)
cv2.imshow('g', g)
#cv2.imwrite('pelvisChida.jpg', g)
cv2.waitKey(0)
cv2.destroyAllWindows()
