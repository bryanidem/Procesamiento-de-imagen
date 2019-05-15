# ///////////////////////
# Correccion gama
# Autor: Bryan Medina
# ///////////////////////

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ubicacion de la imagen
f = cv2.imread('sigure.jpg', 0)

#asignamos gamma y obtenemos las constantes c encargadas de mantener a raya los valores del despliegue (0 - 255)
# en este caso con y obtenemos la función que graficaremos.
gamma = 0.4
x = np.array(range(256))
c = 255/np.power(255, gamma)
y =  c * np.power(x, gamma)

gamma1 = 1.0
c1 = 255/np.power(255, gamma1)
y1 =  c1 * np.power(x, gamma1)

gamma2 = 2.5
c2 = 255/np.power(255, gamma2)
y2 =  c2 * np.power(x, gamma2)

#graficamos las funciones

plt.figure()
plt.title('correción gamma')
plt.plot(x, y, label = '$\gamma = 0.4$')
plt.plot(x, y1, label = '$\gamma = 1.0$')
plt.plot(x, y2, label = '$\gamma = 2.5$')
plt.legend(loc='upper left')
plt.xlabel('intensidades de entrada')
plt.ylabel('intensidades de salida')
plt.show()

#calculamos la transformacion gamma, con la formulita
outputImg = np.array(c * np.power(f, gamma), dtype = 'uint8')
outputImg1 = np.array(c2 * np.power(f, gamma2), dtype = 'uint8')


cv2.imshow('gamma = 0.5', outputImg)
cv2.imshow('gamma = 2.0', outputImg1)
cv2.imshow('entrada', f)
#cv2.imwrite('punto5.jpg', outputImg)
#cv2.imwrite('2puntocero.jpg', outputImg1)
cv2.waitKey(0)
cv2.destroyAllWindows()


