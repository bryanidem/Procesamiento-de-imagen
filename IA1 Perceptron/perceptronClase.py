# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 22:37:50 2019

@author: Bryan Medina

En este post discuto el algoritmo del perceptrón y explico a grandes rasgos la teoría: https://bryanmed.github.io/perceptron/

basado en el código de: https://www.youtube.com/watch?v=CMtLHs8qb60
y del libro: https://www.gandhi.com.mx/inteligencia-artificial-2
"""

#librería de métodos númericos
import numpy as np
#libreria para graficar
import matplotlib.pyplot as plt


class perceptron:
  """la clase perceptron cuenta con 3 metodos:
   init: constructor de la clase -> inicializar algunos parámetros de manera aleatoria
   salidaZ: para calcular la salida del perceptrón
   entrenamiento: en caso de que la diferencia entre la salidaZ y la salida esperada sea mayor a 1%, actualizar los parámetros """

# requerimos conocer el número <<n>> de entradas
  def __init__(self, n):
    """constructor de la clase"""

#   como vamos a tener n entradas, vamos a tener n pesos, que inicializamos de manera aleatoria
    self.pesos = np.random.rand(n)
    
#   bias o umbral 
    self.theta = np.random.rand(1)

#   velocidad de aprendizaje
    self.lambda_ = 0.2    

#   guardamos internamente el valor de n 
    self.n = n


# requerimos los valores de las e   ntradas para calcular la formula de z   
  def salidaZ(self, entradas):
#   la forumula para calcular z = sum(xi * wi) - theta... y también verificamos si se dispara o no (si z >= 0, entonces z = 1, else z = 0)
    self.z = np.where(np.dot(entradas, self.pesos) - self.theta >= 0, 1, 0)     
    self.entradas = entradas
    
    
  def entrenamiento(self, salidaY):
        
    self.error = salidaY - self.z

    print("entradas: " + str(self.entradas) + ", pesos: " + str(self.pesos) + ", theta: " + str(self.theta) + ", z: " + str(self.z) + ", y: " + str(salidaY))


#   Si el error es mayor al 0.1% actualizamos los parametros --> Pesos y theta
    if (np.abs(self.error) > 0.1):

#     delta de theta = -(lambda * e)
      deltaTheta = - (self.lambda_ * self.error) 
#     actualizamos el valor de theta = lambda * e * xi
      self.theta = self.theta + deltaTheta

      for i in range (self.n):              
        deltaPesos =  self.lambda_ * self.error * self.entradas[i] 
        self.pesos[i] = self.pesos[i] + deltaPesos
        

# =============================================================================
# visualizacion de resultados
# =============================================================================
def visualizacion(xi, wi, theta):
  """holo"""
  #para poder hacer un scatter plot separo los vectores en x y y
  x, y = xi.T


# Para graficar la línea de frontera entre los dos grupos
#nuestra recta está dada por la ecuación general de la recta Ax + By + C = 0 ==> Ax_1 + B_x2 - Theta = 0

#para obtener la pendiente m = -A/B
  m = -(wi[0]/wi[1])

#para obtener el cruce en el eje Y, b = -C/B 
#ojo aquí, b es positivo dado que para formar la ecuación general, pasamos a theta como (-theta)
  b = (theta/wi[1])

#valores de x para plottear la linea
  xGraph = np.linspace(-0.1, 1.1, 100)

#funcion de la recta
  yGraph = m * xGraph + b

#graficación
  plt.figure()

#limites para visualizar mejor
  axes = plt.gca()
  axes.set_xlim([-0.1, 1.1])
  axes.set_ylim([-0.1, 1.1])

#  plt.title('Perceptrón como compuerta lógica AND')
#valores de entrada
  plt.scatter(x, y)
#línea frontera
  plt.plot(xGraph, yGraph, 'r')
  plt.xlabel('x1')
  plt.ylabel('x2')
#  plt.show()


# =============================================================================
# Correr el programa
# =============================================================================
    
#Tabla de verdad AND [x1|x2|y]
tablaAND = np.array([[0, 0, 0],
                     [0, 1, 0],
                     [1, 0, 0],
                     [1, 1, 1]])

# numero de entradas x_i, las dos columnas de la tabla de verdad
numeroEntradas = tablaAND.shape[1] - 1

perceptronPrueba = perceptron(numeroEntradas)

#Aquí voy a iterar hasta que se cumpla una iteracion sin error (sin modificacion de parámetros)

errores = True

while errores:
  errores = False

#iteramos sobre todos los valores de la tabla de verdad
  for i in range(tablaAND.shape[0]):
    perceptronPrueba.salidaZ(tablaAND[i, 0:numeroEntradas])  
    #en la ultima columna están los valores de salida esperados
    perceptronPrueba.entrenamiento(tablaAND[i, numeroEntradas])
    if (np.abs(perceptronPrueba.error) > 0.1):
      errores = True

#valores para graficar (si quieres ver como cambia la línea a medida que modificamos los valores, entonces mete estos valores dentro del for anterior)
xi = tablaAND[:, 0:numeroEntradas]
wi = perceptronPrueba.pesos
theta = perceptronPrueba.theta

visualizacion(xi, wi, theta)
























