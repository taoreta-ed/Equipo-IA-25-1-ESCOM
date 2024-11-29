#Propuesta de chatGPT
import numpy as np
import matplotlib.pyplot as plt
from random import randint

# Laberinto de 15x15 con 1 representado por paredes y 0 por caminos
maze = np.array([
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
])


# Función para generar una meta aleatoria
def obtenerMeta():
    while True:
        x, y = randint(1, maze.shape[0] - 2), randint(1, maze.shape[1] - 2)
        if maze[x][y] == 0:
            return (x, y)

# Punto inicial y meta
inicio = (1, 1)
meta = obtenerMeta()

# Agente que busca la meta moviéndose a la derecha
def busqueda(inicio, meta, maze):
    camino = [inicio]
    nodo_actual = np.array(inicio)
    
    while tuple(nodo_actual) != meta:
        nueva_posicion = nodo_actual + np.array([0, 1])  # Movimiento a la derecha
        
        # Si puede moverse a la derecha
        if (0 <= nueva_posicion[1] < maze.shape[1] and maze[nueva_posicion[0], nueva_posicion[1]] == 0):
            nodo_actual = nueva_posicion
        else:
            # Movimiento al azar arriba o abajo si no puede moverse a la derecha
            direccion = randint(-1, 1)
            nueva_posicion = nodo_actual + np.array([direccion, 1])
            if (0 <= nueva_posicion[0] < maze.shape[0] and maze[nueva_posicion[0], nueva_posicion[1]] == 0):
                nodo_actual = nueva_posicion

        camino.append(tuple(nodo_actual))
    return camino

# Función para graficar
def desplegar(maze, camino):
    plt.imshow(maze, cmap='binary')
    for j in camino:
        plt.plot(j[1], j[0], 'o', color='red')
    plt.show()

# Ejecutar la búsqueda y graficar
camino = busqueda(inicio, meta, maze)
desplegar(maze, camino)
