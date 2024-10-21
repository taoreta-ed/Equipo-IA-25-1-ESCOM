# Imports
import matplotlib.pyplot as plt
import numpy as np

# Definimos la matriz para la practica 3
array = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,1,0,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0],
    [1,0,1,0,1,1,1,1,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,1,1,1,1,1,1,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,0,1,0,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,1,0,0,0,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]).reshape(9, 15)

plt.imshow(array, cmap="gray_r")

#Le preguntamos al usuario una coordenada para pintar el punto rojo
coordenadaX = int(input("Ingresa la coordenada en X: "))
coordenadaY = int(input("Ingresa la coordenada en Y: "))

if(coordenadaX>=0 and coordenadaX<=15 and coordenadaY>=0 and coordenadaY <= 9 and array[coordenadaY, coordenadaX] != 1):
    #Con la siguiente funcion colocamos un punto rojo en las coordenadas dadas
    plt.scatter(coordenadaX, coordenadaY, color="red", s=100)
else:
    print("Coordenada no valida")


plt.show()