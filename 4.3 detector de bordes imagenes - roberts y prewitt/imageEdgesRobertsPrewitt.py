# -*- coding: utf-8 -*-
"""
# =============================================================================
# deteccion de bordes en imagenes
# =============================================================================

Created on Mon Jul 29 13:59:25 2019

@author: bryan medina
"""

import numpy as np
import scipy as sp
import skimage as sk
import matplotlib.pyplot as plt

f = sk.io.imread('puente.jpg')
f = sk.color.rgb2gray(f)

# =============================================================================
# kernels
# =============================================================================

#primera derivada 1d
d1x = np.array(((-1, 1),(0, 0)), dtype = 'float')
d1y = np.array(((-1, 0),(1, 0)), dtype = 'float')

#Roberts
RGx = np.array((
    [-1, 0],
    [ 0, 1]    
    ), dtype = 'float')

RGy = np.array((
    [ 0, -1],
    [ 1,  0]    
    ), dtype = 'float')

# Prewitt
PGx = np.array((
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1] 
    ), dtype = 'float')

PGy = np.array((
    [-1,  0, 1],
    [-1,  0, 1],
    [-1,  0, 1] 
    ), dtype = 'float')

PGd1 = np.array((
    [ 0,  1,  1],
    [-1,  0,  1],
    [-1, -1,  0] 
    ), dtype = 'float')

PGd2 = np.array((
    [-1, -1,  0],
    [-1,  0,  1],
    [ 0,  1,  1] 
    ), dtype = 'float')

# Sobel
SGx = np.array((
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
    ), dtype = 'float')

SGy = np.array((
    [-1,  0,  1],
    [-2,  0,  2],
    [-1,  0,  1]
    ), dtype = 'float')


def edgeDetection(imagen, kernel, nombre):
  """en esta función realizamos la convolución de la imagen con el kernel, además de visualizar el resultado"""
#  convolución
  conv = sp.signal.convolve(imagen, kernel, 'same')
  conv = np.abs(conv)
  plt.figure()
  plt.title(nombre)
  plt.axis('off')
  plt.imshow(conv, cmap = 'gray')
  plt.show()
  return conv


# primera derivada
edgeDetection(f, d1x, 'derivada en x (valor absoluto)')
edgeDetection(f, d1y, 'derivada en y (valor absoluto)')

# Roberts
RobertsX = edgeDetection(f, RGx, 'Roberts x')
RobertsY = edgeDetection(f, RGy, 'Roberts y')

MagRoberts = RobertsX + RobertsY
porcentaje = 0.25
umbral = porcentaje*np.max(MagRoberts)
binaryRoberts = np.zeros(f.shape, dtype = 'float')
binaryRoberts[MagRoberts > umbral] = 1.0

plt.figure()
plt.title('magnitud de Roberts - binarizada con umbral de: ' + str(porcentaje))
plt.axis('off')
plt.imshow(binaryRoberts, cmap = 'gray')
plt.show()

plt.figure()
plt.title('magnitud de Roberts')
plt.axis('off')
plt.imshow(MagRoberts, cmap = 'gray')
plt.show()


#Prewitt
PrewittX = edgeDetection(f, PGx, 'Prewitt x')
PrewittY = edgeDetection(f, PGy, 'Prewitt y')
Prewittd1 = edgeDetection(f, PGd1, 'Prewitt d1')
Prewittd2 = edgeDetection(f, PGd2, 'Prewitt d2')

MagPrewitt = Prewittd1 + Prewittd2 + PrewittX + PrewittY

porcentaje = 0.25
umbral = porcentaje*np.max(MagPrewitt)
binaryPrewitt = np.zeros(f.shape, dtype = 'float')
binaryPrewitt[MagPrewitt > umbral] = 1.0

plt.figure()
plt.title('magnitud de Prewitt - binarizada con umbral de: ' + str(porcentaje))
plt.axis('off')
plt.imshow(binaryPrewitt, cmap = 'gray')
plt.show()













