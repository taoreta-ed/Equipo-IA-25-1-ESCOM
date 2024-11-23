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
movimientos = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1.-1),(0,-1  )]

def dfs(laberinto,punto_inicial,meta):
    #Lista para manejar los nodos por explorar (pila)
    pila = [(punto_inicial,[])]
    #Matriz de visitados
    filas = np.shape(laberinto)[0]
    columnas = np.shape(laberinto)[1]
    visitados = np.zeros((filas,columnas))
    #Marcamos el nodo inicial como visitado

    #Definir una lista que contenga todos los nodos que he visitado
    considerados = []

    while len(pila) > 0:
        nodo_actual,camino = pila[-1]
        pila = pila[:-1]

        #Guardar los nodos que se han ido visitando
        considerados += [nodo_actual]

        if nodo_actual == meta:
            return camino + [nodo_actual],considerados

        visitados[nodo_actual[0],nodo_actual[1]] = 1
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0],nodo_actual[1] + direccion[1])
            #Ver que el vecino (nueva posición) esté dentro del laberinto
            if((0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas)):
                #Ver si el nodo a evaluar (nueva_posicion) es un cambio accesible y además si ese nodo NO LO HE VISITADO
                if((maze[nueva_posicion[0],nueva_posicion[1]]) == 0 and visitados[nueva_posicion[0],nueva_posicion[1]] == 0):
                    pila += [(nueva_posicion,camino + [nodo_actual])]
    return None,considerados

def desplegar_laberinto(maze,camino = None,considerados = None):
    plt.imshow(maze,cmap = 'binary')
    if considerados:
        for i in considerados:
            plt.plot(i[1],i[0],'o',color = 'blue')
    if camino:
        for j in camino:
            plt.plot(j[1],j[0],'o',color = 'red')
    plt.show()

camino,considerados = dfs(maze,punto_inicial,meta)
desplegar_laberinto(maze,camino,considerados)