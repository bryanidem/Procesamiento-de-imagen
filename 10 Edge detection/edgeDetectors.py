# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:55:51 2019

@author: bryan 

# =============================================================================
# EDGE DETECTORS
# =============================================================================

"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from skimage import io, color
#import skimage as sk



#cargar imagen y ponerla en un solo canal (escala de grises)
f = io.imread("uaslprv.jpg")
f = color.rgb2gray(f)

#definir los kernels para la detección de bordes

# =============================================================================
# Roberts
# =============================================================================

RGx = np.array((
    [-1, 0],
    [ 0, 1]    
    ), dtype = 'float')

RGy = np.array((
    [ 0, -1],
    [ 1,  0]    
    ), dtype = 'float')


# =============================================================================
# Prewwit
# =============================================================================

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


# =============================================================================
# Sobel
# =============================================================================

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

SGdiag1 = np.array((
    [ 0,  1,  2],
    [-1,  0,  1],
    [-2, -1,  0]
    ), dtype = 'float')

SGdiag2 = np.array((
    [-2, -1,  0],
    [-1,  0,  1],
    [ 0,  1,  2]
    ), dtype = 'float')


#convolucion de la imagen con el kernel

##conv con kernels de Roberts
#convRGx = sp.signal.convolve2d(f, RGx, 'same')
#convRGy = sp.signal.convolve2d(f, RGy, 'same')
#
##conv con kernels de Prewitt
#convPGx = sp.signal.convolve2d(f, PGx, 'same')
#convPGy = sp.signal.convolve2d(f, PGy, 'same')

#conv con kernels de Sobel
convSGx = sp.signal.convolve2d(f, SGx, 'same')
convSGy = sp.signal.convolve2d(f, SGy, 'same')
convSGdiag1 = sp.signal.convolve2d(f, SGdiag1, 'same')
convSGdiag2 = sp.signal.convolve2d(f, SGdiag2, 'same')


#valores absolutos para visualizar
#absRGx = np.abs(convRGx)
#absRGy = np.abs(convRGy)

#absPGx = np.abs(convPGx)
#absPGy = np.abs(convPGy)

absSGx = np.abs(convSGx)
absSGy = np.abs(convSGy)
absSGdiag1 = np.abs(convSGdiag1)
absSGdiag2 = np.abs(convSGdiag2)


# magnitud y angulo Sobel
magnitud = absSGx + absSGy
angulo = np.arctan2(convSGy,convSGx)


#ahora probaremos suavizando la imagen
#ventana de 5x5 de smoothing
smoothing = np.ones((5,5), dtype = 'float') * (1/25)
smoothF = sp.signal.convolve2d(f, smoothing, 'same')

smoothMagnitudX = sp.signal.convolve2d(smoothF, SGx)
smoothMagnitudY = sp.signal.convolve2d(smoothF, SGy)

smoothMagnitud = np.abs(smoothMagnitudX) + np.abs(smoothMagnitudY)



#mostrar imágenes

plt.figure()
plt.title('uaslp Rioverde')
plt.axis('off')
plt.imshow(f, cmap = 'gray')
#
#plt.figure()
#plt.subplot(1, 2, 1)
#plt.title('Abs Roberts Gx')
#plt.axis('off')
#plt.imshow(absRGx, cmap = 'gray')
#
#plt.subplot(1, 2, 2)
#plt.title('Abs Roberts Gy')
#plt.imshow(absRGy, cmap = 'gray')
#plt.axis('off')
#
#
#plt.figure()
#plt.subplot(1, 2, 1)
#plt.title('Abs de Prewitt Gx')
#plt.axis('off')
#plt.imshow(absPGx, cmap = 'gray')
#
#plt.subplot(1, 2, 2)
#plt.title('Abs de Prewitt Gy')
#plt.imshow(absPGy, cmap = 'gray')
#plt.axis('off')
#
#
#plt.figure()
#plt.subplot(2, 2, 1)
#plt.title('Abs de Sobel Gx')
#plt.axis('off')
#plt.imshow(absSGx, cmap = 'gray')
#
#plt.subplot(2, 2, 2)
#plt.title('Abs de Sobel Gy')
#plt.imshow(absSGy, cmap = 'gray')
#plt.axis('off')
#
#plt.subplot(2, 2, 3)
#plt.title('Abs de Sobel diagonal 1')
#plt.axis('off')
#plt.imshow(absSGdiag1, cmap = 'gray')
#
#plt.subplot(2, 2, 4)
#plt.title('Abs de Sobel diagonal 2')
#plt.imshow(absSGdiag2, cmap = 'gray')
#plt.axis('off')

plt.figure()
plt.subplot(1, 2, 1)
plt.title('magnitud  (gradiente |Gx| + |Gy|)')
plt.imshow(magnitud, cmap = 'gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('angulo')
plt.imshow(angulo, cmap = 'gray')
plt.axis('off')

plt.figure()
plt.subplot(1, 2, 1)
plt.title('imagen suavizada con filtro de smoothing 5x5')
plt.imshow(smoothF, cmap = 'gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('gradiente con Sobel')
plt.imshow(smoothMagnitud, cmap = 'gray')
plt.axis('off')






plt.show()





















