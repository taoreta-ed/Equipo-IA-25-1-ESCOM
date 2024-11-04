# Imports
import matplotlib.pyplot as plt
import numpy as np

#Laberinto
maze = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,1,0,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0],
    [1,0,1,0,1,1,1,1,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,1,1,1,1,1,1,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,0,1,0,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,1,0,0,0,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
])
#Inicializar de punto inicial y final 
punto_inicial = (0, 0)
meta = (7, 8)
#Tipos de movimiento
movimientos = [(-1,0), (0,1), (1,0), (0,-1)]

def dfs(maze, punto_inicial, meta):
    #Lista para manejar los nodos por explorar (pila)
    pila = [(punto_inicial, [])]
    #Matriz de visitados
    filas = np.shape(maze)[0]
    columnas = np.shape(maze)[1]
    visitados = np.zeros((filas,columnas))
    #Marcamos el nodo inicial como visitados
    #Definir una lista que contenga a todos los nodos que he visitado
    considerados = []

    while len(pila) > 0:
        nodo_actual, camino = pila[-1]
        pila = pila[:-1]

        #Guardar los nodos que se han ido visitando
        considerados += [considerados], nodo_actual

        if nodo_actual == meta:
            return camino + [nodo_actual], considerados

        visitados[nodo_actual[0], nodo_actual[1]] = 1
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            #Ver que el vecino (nueva posición) este dentro del laberinto
            if ((0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas)):
                ## Ver si el nodo a evaluar (nueva_posicion)  es un camino accesible y ademas si ese nodo no lo he visitado
                if (maze[nueva_posicion[0], nueva_posicion[1]]) == 0 and (visitados[nueva_posicion[0], nueva_posicion[1]]==0):
                    pila += [(nueva_posicion, camino + [nodo_actual])]
    return None, considerados

def desplegar_laberinto(maze, camino = None, considerados = None):
    plt.imshow(maze, cmap="grey")
    if camino:
        for i in camino:
            plt.plot(i[1], i[0], 'o', color = 'blue')
    if considerados:
        for j in considerados:
            plt.plot(j[1], j[0], 'o', color = 'red')
    plt.show()

camino, considerados = dfs(maze, punto_inicial, meta)
desplegar_laberinto(maze, camino, considerados)