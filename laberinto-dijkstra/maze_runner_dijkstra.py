import matplotlib.pyplot as plt
import numpy as np
import heapq  # Usaremos una cola de prioridad para manejar el nodo con menor costo (el nodo de menor costo va en la parte superior)

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
movimientos = [(-1,0), (0,1), (1,0), (0,-1)]

def dijkstra(laberinto, punto_inicial, meta):
    # Cola de prioridad para manejar los nodos según su costo
    cola_prioridad = [(0, punto_inicial, [])]  # (costo_acumulado, posición, camino)
    # Matriz de costos acumulados, inicializada con infinito
    filas, columnas = laberinto.shape
    costos = np.full((filas, columnas), np.inf)
    costos[punto_inicial] = 0
    # Matriz para los nodos visitados
    visitados = np.zeros((filas, columnas), dtype=bool)
    # Para visualización de nodos considerados
    considerados = []

    while cola_prioridad:
        # Extraer el nodo con menor costo acumulado
        costo_actual, nodo_actual, camino = heapq.heappop(cola_prioridad)
        
        # Guardar los nodos que se han ido considerando
        considerados.append(nodo_actual)
        
        # Si llegamos a la meta, devolver el camino y los considerados
        if nodo_actual == meta:
            return camino + [nodo_actual], considerados
        
        # Marcar el nodo actual como visitado
        if visitados[nodo_actual]:
            continue
        visitados[nodo_actual] = True

        # Evaluar vecinos
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            
            # Verificar que el vecino esté dentro del laberinto y que sea accesible
            if 0 <= nueva_posicion[0] < filas and 0 <= nueva_posicion[1] < columnas:
                if laberinto[nueva_posicion] == 0 and not visitados[nueva_posicion]:
                    nuevo_costo = costo_actual + 1  # Peso 1 para cada movimiento
                    # Si encontramos un camino más barato a nueva_posicion, lo actualizamos
                    if nuevo_costo < costos[nueva_posicion]:
                        costos[nueva_posicion] = nuevo_costo
                        heapq.heappush(cola_prioridad, (nuevo_costo, nueva_posicion, camino + [nodo_actual]))

    return None, considerados  # Si no se encuentra un camino

def desplegar_laberinto(maze, camino=None, considerados=None):
    plt.imshow(maze, cmap='binary')
    if considerados:
        for i in considerados:
            plt.plot(i[1], i[0], 'o', color='blue')
    if camino:
        for j in camino:
            plt.plot(j[1], j[0], 'o', color='red')
    plt.show()

# Ejecutar Dijkstra
camino, considerados = dijkstra(maze, punto_inicial, meta)
desplegar_laberinto(maze, camino, considerados)
