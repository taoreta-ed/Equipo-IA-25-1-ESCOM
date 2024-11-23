# -*- coding: utf-8 -*-
"""Maze_Runner_DFS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v7FwZgHmOH6R8WP9QMoNd0leBMiK1qg4
"""

import matplotlib.pyplot as plt
import numpy as np

#Laberinto de 15x15 con 1 representado por paredes y 0 por caminos
maze = np.array([
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1],
    [1,0,0,0,1,0,1,1,1,0,1,0,1,0,0,0,0,1,1,1],
    [1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1],
    [1,0,0,0,1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,1],
    [1,0,0,1,0,1,1,1,0,1,0,0,1,0,0,0,0,0,1,1],
    [1,0,1,0,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1],
    [1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,1],
    [1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1],
    [1,0,0,1,0,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,1],
    [1,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,0,1,0,1],
    [1,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ])

#Inicializar punto inicial y punto final
punto_inicial = (1,1)
meta = (13,15)

#Tipos de movimiento
movimientos = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

def desplegar_laberinto(maze,camino = None,considerados = None):
    plt.imshow(maze,cmap = 'binary')
    if considerados:
        # considerados : lista cerrada
        for i in considerados:
            plt.plot(i[1],i[0],'o',color = 'blue')
    if camino:
        for j in camino:
            plt.plot(j[1],j[0],'o',color = 'red')
    plt.show()

# def heuristica(nodo_actual,objetivo):
#     # energia que gasta del nodo actual al nodo destino
#     return (abs(objetivo[0]- nodo_actual[0]) + abs(objetivo[1]-nodo_actual[1]) )

#Practica 4a
def distancia_euclidiana(nodo_actual, objetivo):
    return np.sqrt((objetivo[0] - nodo_actual[0])**2 + (objetivo[1] - nodo_actual[1])**2)



def A_estrella(laberinto, punto_inicial, meta):
    # Lista para manejar los nodos por explorar

    # lista_abierta = [(punto_inicial, 0, heuristica(punto_inicial, meta), [])]
    lista_abierta = [(punto_inicial, 0, distancia_euclidiana(punto_inicial, meta), [])]
   
    # Considerados: Almacena los nodos ya explorados para visualización
    considerados = []

    # Matriz de visitados (0 = no visitado, 1 = visitado)
    filas, columnas = laberinto.shape
    lista_cerrada = np.zeros((filas, columnas))

    while lista_abierta:
        # Ordenar la lista abierta por el menor costo f = g + h
        lista_abierta.sort(key=lambda x: x[1] + x[2])
        nodo_actual, costo_g, _, camino = lista_abierta.pop(0)

        # Agregar nodo a considerados
        considerados.append(nodo_actual)
        lista_cerrada[nodo_actual[0], nodo_actual[1]] = 1

        # Si alcanzamos la meta, devolvemos el camino
        if nodo_actual == meta:
            return camino + [nodo_actual], considerados

        # Explorar vecinos
        for movimiento in movimientos:
            vecino = (nodo_actual[0] + movimiento[0], nodo_actual[1] + movimiento[1])

            # Verificar que el vecino está dentro del laberinto y no es una pared
            if 0 <= vecino[0] < filas and 0 <= vecino[1] < columnas:
                if laberinto[vecino[0], vecino[1]] == 0 and not lista_cerrada[vecino[0], vecino[1]]:
                    nuevo_costo_g = costo_g + 1
                    # nuevo_costo_h = heuristica(vecino, meta)
                    nuevo_costo_h = distancia_euclidiana(vecino, meta)
                    
                    lista_abierta.append((vecino, nuevo_costo_g, nuevo_costo_h, camino + [nodo_actual]))

    # Si no hay camino, devolvemos None
    return None, considerados

# Resolver el laberinto
camino, considerados = A_estrella(maze, punto_inicial, meta)

# Visualizar el laberinto con el camino y nodos explorados
desplegar_laberinto(maze, camino, considerados)
