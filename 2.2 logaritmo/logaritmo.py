# ///////////////////////
# Author : Bryan Medina
# ///////////////////////

import cv2
import numpy as np
import matplotlib.pyplot as plt

sourceImg = cv2.imread('C:/Users/bryan/Desktop/image processing python/data/darkNetflix.jpg', 0)

# calculo de la constante c, para obtener el mismo rango que el de entrada (0 - 255)
c = 255/np.log1p(sourceImg.max())

# calculo del logaritmo 
outputImg = c * np.log1p(np.double(sourceImg))


x = np.array(range(256))
y = c * np.log1p(np.double(x))

plt.figure()
plt.plot(x, y)
plt.title('g(x,y) = c log(1 + f(x, y))')
plt.xlabel('brillo - f(x,y)')
plt.ylabel('brillo - g(x, y)')
plt.show()

plt.figure()
plt.subplot(121)
plt.imshow(sourceImg, cmap='gray')
plt.title('Imagen de entrada')
plt.axis('off')

plt.subplot(122)
plt.imshow(outputImg, cmap='gray')
plt.title('Transformación logaritmo')
plt.axis('off')
plt.show()
