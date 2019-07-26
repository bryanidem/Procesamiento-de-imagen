# -*- coding: utf-8 -*-
"""
# =============================================================================
# visualizar un borde y su primera y segunda derivada
# =============================================================================

Created on Thu Jul 11 09:36:06 2019

@author: bryan
"""

import numpy as np
import matplotlib.pyplot as plt

#impulso unitario
x = np.arange(0, 50, 1)
unitStep = np.zeros(x.size, dtype = 'float')
unitStep[np.where(x > 25)] = 1.0

#ramp = np.zeros(x.size, dtype = 'float')
#ramp[np.where((x > 0.5) & (x < 1.5))] = np.arange(0.01, 1, 0.01)
#ramp[x >= 1.5] = 1.0

#primera y segunda derivada
d1f = np.array([-1, 0, 1])
d2f = np.array([1, -2, 1])

convd1f = np.convolve(unitStep, d1f, 'same')
convd2f = np.convolve(unitStep, d2f, 'same')

convd1f = convd1f[np.arange(0, 49)]
convd2f = convd2f[np.arange(0, 49)]

xd1f = np.arange(0, 49) #quitar el ultimo elemento de las derivadas, para fines de visualizacion
label = np.array([0, 10, 20, 25, 26, 30, 40, 50])


plt.figure()
plt.title('función impulso unitario')
plt.ylabel('nivel de brillo (float)')
plt.xlabel('"pixeles"')
plt.xticks(label)
plt.plot(x, unitStep)

plt.figure()
plt.title('resultado de primera derivada')
plt.xticks(label)
plt.plot(xd1f, convd1f)

plt.figure()
plt.title('resultado de segunda derivada')
plt.xticks(label)
plt.plot(xd1f, convd2f)

plt.show()









