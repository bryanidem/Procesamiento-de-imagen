#//////////////////////////////////////
#//Transformacion lineal por partes
#//Autor: Bryan Medina
#//////////////////////////////////////

import cv2
import numpy as np
import matplotlib.pyplot as plt

f = cv2.imread('gordon.jpg', 0)

r1 = 120
s1 = 1
r2 = 121
s2 = 255

a = (s1/r1)
b = (s2-s1)/(r2-r1)
c = (255-s2)/(255-r2)

x1 = np.array(range(r1))
y1 = a * x1

x2 = np.array(range(r1,r2+1))
y2 = b * (x2 - r1) + a * r1

x3 = np.array(range(r2, 256))
y3 = c * (x3 - r2) + b * (r2 - r1) + a * r1



width, height = f.shape
g = np.zeros((width, height), np.uint8)


for i in range(width):
    for j in range(height):
        if(f[i, j] >= 0 and f[i, j] <= r1):
            g[i, j] = a * f[i, j]

        elif(f[i, j] > r1 and f[i, j] <= r2):
            g[i, j] = b * ((f[i, j] - r1) + (a * r1))

        else:
            if(f[i, j] > r2 and f[i, j] <= 255):
                g[i, j] = c * (f[i, j] - r2) + b * (r2 - r1) + a * r1





plt.figure()
plt.plot(x1, y1, 'r')
plt.plot(x2, y2, 'g')
plt.plot(x3, y3, 'b')
plt.show()

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(f, cmap = 'gray')
plt.axis('off')
plt.title('imagen de entrada f')

plt.subplot(1, 2, 2)
plt.imshow(g, cmap = 'gray')
plt.axis('off')
plt.title('imagen de salida g')
plt.show()


cv2.imshow('f', f)
cv2.imshow('g', g)
cv2.waitKey(0)
cv2.destroyAllWindows()

#datos de la imagen de entrada
print("tipo: " + str(f.dtype) + ", tamaño: " + str(f.shape))
print("tipo: " + str(g.dtype) + ", tamaño: " + str(g.shape))
