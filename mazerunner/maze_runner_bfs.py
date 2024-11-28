import matplotlib.pyplot as plt
import numpy as np

# Laberinto de 15x15 con 1 representado por paredes y 0 por caminos
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

# Inicializar punto inicial y punto final
punto_inicial = (1,1)
meta = (13,15)

# Tipos de movimiento
movimientos = [(-1,0),(0,1),(1,0),(0,-1)]

def bfs(laberinto, punto_inicial, meta):
    # Cola para manejar los nodos por explorar (FIFO)
    cola = [(punto_inicial, [])]
    # Matriz de visitados
    filas = np.shape(laberinto)[0]
    columnas = np.shape(laberinto)[1]
    visitados = np.zeros((filas, columnas))
    # Definir una lista que contenga todos los nodos que he visitado
    considerados = []

    while len(cola) > 0:
        nodo_actual, camino = cola[0]
        cola = cola[1:]

        # Guardar los nodos que se han ido visitando
        #considerados.append(nodo_actual)
        mi_append(considerados, nodo_actual)

        if nodo_actual == meta:
            return camino + [nodo_actual], considerados

        visitados[nodo_actual[0], nodo_actual[1]] = 1
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            # Verificar que el vecino esté dentro del laberinto y no haya sido visitado
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                if (maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0):
                    #cola.append((nueva_posicion, camino + [nodo_actual]))
                    mi_append(cola, (nueva_posicion, camino + [nodo_actual]))
    return None, considerados

#Funcion que reemplaza append
def mi_append(lista, elemento):
    #"""Agrega un elemento al final de la lista."""
    lista += [elemento]  # Usamos la concatenación para evitar append.

def desplegar_laberinto(maze, camino=None, considerados=None):
    plt.imshow(maze, cmap='binary')
    if considerados:
        for i in considerados:
            plt.plot(i[1], i[0], 'o', color='blue')
    if camino:
        for j in camino:
            plt.plot(j[1], j[0], 'o', color='red')
    plt.show()

# Ejecutar BFS
camino, considerados = bfs(maze, punto_inicial, meta)
desplegar_laberinto(maze, camino, considerados)
