# Imports
import matplotlib.pyplot as plt
import numpy as np

#Inicializar de punto inicial y final 
punto_inicial = (1, 1)
meta = (14, 14)
#Tipos de movimiento
movimientos = [(-1,0), (0,1), (1,0), (0,-1)]

def dfs(laberinto, punto_inicial, meta):
    #Lista para manejar los nodos por explorar (pila)
    pila = [(punto_inicial, [])]
    #Matriz de visitados
    filas = np.shape(laberinto)[0]
    columnas = np.shape(laberinto)[1]
    visitados = np.zeros((filas,columnas))
    #Marcamos el nodo inicial como visitados
    #Definir una lista que contenga a todos los nodos que he visitado
    considerados = []

    while len(pila) > 0:
        nodo_actual, camino = pila[-1]
        pila = pila[:1]

        #Guardar los nodos que se han ido visitando
        considerados += [considerados]

        if nodo_actual == meta:
            return camino + [nodo_actual], considerados

        visitados[nodo_actual[0], nodo_actual[1]] = 1
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0])
            #Ver que el vecino (nueva posición) este dentro del laberinto
            if ((0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas)):
                ## Ver si el nodo a evaluar (nueva_posicion)  es un camino accesible y ademas si ese nodo no lo he visitado
                if (maze[nueva_posicion[0], nueva_posicion[1]]) == 0 and (visitados[nueva_posicion[0], nueva_posicion[1]]==0):
                    pila += [(nueva_posicion + [nodo_actual])]