# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:14:25 2019

@author: bryan

"""

# =============================================================================
# Line detection
# =============================================================================


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from skimage import io, color
#from mpl_toolkits.mplot3d import Axes3D
from skimage.transform import resize



f = io.imread('jordan.jpg')
f = color.rgb2gray(f)


laplacian = np.array((
    [  1,  1,  1],
    [  1, -8,  1],
    [  1,  1,  1]), dtype = 'float')

convolucion = sp.signal.convolve2d(f, laplacian, 'same')

plt.figure()
plt.title('imagen de entrada')
plt.axis('off')
plt.imshow(f, cmap = 'gray')

plt.figure()
plt.title('convolucion con el laplaciano')
plt.axis('off')
plt.imshow(convolucion, cmap = 'gray')

###valor absoluto de la convolución con el laplaciano
laplacianAbs = np.abs(convolucion)

plt.figure()
plt.title('valor absoluto del laplaciano')
plt.imshow(laplacianAbs, cmap ='gray')
plt.show()

##solo valores positivos de la convolucion con el laplaciano
positivos = np.zeros(f.shape, dtype = 'float')
positivos = np.where(convolucion > 0, convolucion, 0)

plt.figure()
plt.title('valores positivos de la convolucion')
plt.imshow(positivos, cmap ='gray')
plt.show()

# =============================================================================
# Para verlos como una superficie (mas chido osiosi)
# =============================================================================
#fSurf = resize(convolucion, (40, 80), anti_aliasing=True)
#
## create the x and y coordinate arrays (here we just use pixel indices)
#xx, yy = np.mgrid[0:fSurf.shape[0], 0:fSurf.shape[1]]
#
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#surf = ax.plot_surface(xx, yy, fSurf, cmap=plt.cm.gray, linewidth=0, antialiased=False)
#fig.colorbar(surf, shrink=0.5, aspect=5)





