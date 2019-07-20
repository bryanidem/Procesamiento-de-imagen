# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:47:34 2019

@author: bryan

Point detection 
"""

import numpy as np
import scipy
from skimage import io, color
import matplotlib.pyplot as plt
from skimage.transform import resize
from mpl_toolkits.mplot3d import Axes3D



f = io.imread('ramp.png')
f = color.rgb2gray(f)


laplacian = np.array((
    [  1,  1,  1],
    [  1, -8,  1],
    [  1,  1,  1]), dtype = 'float')

laplacian2 = np.array((
    [  0,  1,  0],
    [  1, -4,  1],
    [  0,  1,  0]), dtype = 'float')

pointDetection = scipy.signal.convolve2d(f, laplacian, 'same')




#print(np.max(pointDetection))

porcentaje = 0.5
umbral = porcentaje*np.max(pointDetection)
binaryPoint = np.zeros(f.shape, dtype = 'float')
binaryPoint[pointDetection > umbral] = 1.0

#plt.figure()
#plt.axis('off')
#plt.title('imagen original')
#plt.imshow(f, cmap = 'gray')
#
#
#plt.figure()
#plt.axis('off')
#plt.title('convolucion con laplaciano')
#plt.imshow(pointDetection, cmap = 'gray')
#
#plt.figure()
#plt.axis('off')
#plt.title('binarización con umbral a ' + str(porcentaje) + ' del máximo valor')
#plt.imshow(binaryPoint, cmap = 'gray')

# =============================================================================
# Para verlos como una superficie (mas chido osiosi)
# =============================================================================
fSurf = resize(f, (208, 437), anti_aliasing=True)

# create the x and y coordinate arrays (here we just use pixel indices)
xx, yy = np.mgrid[0:fSurf.shape[0], 0:fSurf.shape[1]]

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xx, yy, fSurf, cmap=plt.cm.gray, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)


