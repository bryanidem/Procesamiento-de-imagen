# ///////////////////////
# Correccion gama
# Autor: Bryan Medina
# ///////////////////////

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ubicacion de la imagen
sourceImg = cv2.imread('sigure.jpg', 0)

# valores de intensidad en la imagen de entrada
x = np.array(range(256))


def correccionGama(f, gamma):
    """ funcion en la cual, a partir de los valores de intensidad x (256), se calcula la potencia con el exponente gamma"""
    #se calcula c al igual que en el logaritmo, pero pa los cuates es 1
    c = 255/np.log1p(sourceImg.max())

    #interpolacion lineal para normalizar los valores de entrada y solamente calcular la potencia.
    f = np.interp(f, (f.min(), f.max()), (0, 1))

    #yup, solo calcular la potencia.
    y = c * np.power(f, gamma)

    # Vuelvo a poner los valores en el rango de 0 a 255
    # y = 255 * y
    y = np.interp(y, (y.min(), y.max()), (0, 255))
    return y


def graficar(gamma):
    """funcion para graficar tanto la imagen de salida, como la funcion de Transformación correspondiente"""

    imagen = correccionGama(sourceImg, gamma)
    grafica = correccionGama(x, gamma)

    plt.figure()
    plt.subplot(121)
    plt.imshow(imagen, cmap='gray')
    plt.axis('off')
    plt.title('corrección ' + r'$\gamma = $' + str(gamma))

    plt.subplot(122)
    plt.plot(x, grafica)
    plt.xlabel('brillo - f(x, y)')
    plt.ylabel('brillo - g(x, y)')
    plt.title('$g(x, y) = c*f(x, y)^\gamma$' + r'     $\gamma = $' + str(gamma))

    plt.show()


graficar(0.2)
graficar(1)
graficar(5)
