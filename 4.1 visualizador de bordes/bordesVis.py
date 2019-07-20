# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:17:59 2019

@author: bryan medina

# =============================================================================
# visualizador de los distintos tipos de bordes
# =============================================================================
"""

import numpy as np
from skimage import io, color
import matplotlib.pyplot as plt

#Requerida para visualizar la superficie/surface
from mpl_toolkits.mplot3d import Axes3D

#imágenes disponibles -> step.png, ramp.png y roof.png
f = io.imread('ramp.png')
f = color.rgb2gray(f)

#mostrar la imagen original
plt.figure()
plt.axis('off')
plt.title('imagen original')
plt.imshow(f, cmap = 'gray')


# create the x and y coordinate arrays (here we just use pixel indices)
xx, yy = np.mgrid[0:f.shape[0], 0:f.shape[1]]

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xx, yy, f, cmap=plt.cm.gray, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)