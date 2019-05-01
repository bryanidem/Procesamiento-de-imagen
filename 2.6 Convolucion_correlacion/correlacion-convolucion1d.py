#//////////////////////////////////
#/correlacion convolucion en 1 D
#/Autor: Bryan Medina
#//////////////////////////////////


import numpy as np

#correlacion en 1d

#funcion impulso 1d
# f1d = np.zeros(8)
# f1d[3] = 1
f1d = np.array([0,0,2,1,2,0,1,0,1,2])
#kernel
w1d = np.array([1,2,3,2,8])



def correlation1d(function, kernel, convolution = False):
    """realiza la correlacion (convolution = false) de la funcion respecto al kernel
    cuando convolution = true calcula la convolucion"""
    if(convolution == True):
        kernel = np.flip(kernel)
    #rellenar de ceros para que sea alineable con el kernel
    fPad = np.pad(function, (kernel.size-1, kernel.size-1), 'constant')
    correlacion = np.zeros(len(fPad) - (len(kernel)-1))
    for i in range(correlacion.size):
        correlacion[i] = sum(fPad[i:i+(kernel.size)]*kernel)
        # print(fPad[i:i+(kernel.size)]*kernel)
    return correlacion


#calculo de la convolucion con mi funcion
myfunction = correlation1d(f1d, w1d, True).astype('int')

#calculo de la convolucion utilizando numpy
numpyconv = np.convolve(f1d, w1d)
print('señal de entrada:' + str(f1d))
print('kernel:          ' + str(w1d))
print("mi implementacion: " + str(myfunction))
print("la de numpy:       " + str(numpyconv))
