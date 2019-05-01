import numpy as np
import cv2

#funcion o imagen de entrada
#f = np.array([[1,2,3],[4,5,6],[7,8,9]]).astype('uint8')
f = cv2.imread('Lenna.png', 0)

#kernel de tamano 31*31 la cual es un promedio, con lo cual le dara un efecto blureado a la 
#aqui se puede cambiar por otro tipo de kernel para otros efectos chiros
kernel = np.ones((31, 31), dtype="float") * (1.0 / (31 * 31))



def correlacion(f, kernel):
    """funcion de correlacion que tiene como argumentos una imagen de entrada f, y la mascara/kernel que se le aplicara, en caso de querer utilizar la convolucion, se tendria que sacar supongo la transpuesta (no estoy seguro) pero en mayor caso se utilizan kernels simetricos, entonces no hay tanto peisi"""
    #el offset es el padding que se le agrega a la imagen con el fin de que el centro del kernel pueda operar en las        orillas
    offset = int((kernel.shape[0]-1)/2)
    #aqui es realiza el padding, en mode puede ser ceros, reflejar o muchas mas wooo
    fPad = np.pad(f, ((offset, offset),(offset, offset)), mode = 'reflect')

    #inicializar imagen de salida
    g = np.zeros([f.shape[0], f.shape[1]], 'uint8')

    fW, fH = f.shape

    #proceso de correlacion-convolucion
    correlacion = np.zeros([fW, fH])
    for i in np.arange(offset, fW + offset):
        for j in np.arange(offset, fH + offset):
            #se define la region de la imagen correspondiente a la posicion del kernel
            roi = fPad[i-offset:i+offset+1, j-offset:j+offset+1]
            corr = np.sum(roi * kernel)
            correlacion[i-offset, j-offset] = corr

    return correlacion.astype('uint8')


#funcion de openCV para comparar con mi correlacion
opencvG = cv2.filter2D(f, -1, kernel)
g = correlacion(f, kernel)

#los valores me salen distintos con un error menor a la unidad, presumiblemente debido a los tipos que utilize en las operaciones, pero el resultado es virtualmente igual-
cv2.imshow('Lennna', f)
cv2.imshow('own conv', g)
cv2.imshow('opencv conv', opencvG)

cv2.waitKey(0)
cv2.destroyAllWindows()










