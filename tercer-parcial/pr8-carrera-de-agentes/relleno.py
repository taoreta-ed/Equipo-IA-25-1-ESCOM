#Realizar un programa con 2 agentes que se inicien en 
#posiciones aleatorias en un mapa de 20x20
#Cada agente tiene diferentes reglas de movimiento
#Los agentes no pueden atravesar paredes
#Los agentes no pueden salirse del mapa
#1 ganador

import numpy as np
import random
import matplotlib.pyplot as plt

maze = np.array([
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,0,0,0,0,1],
    [0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0,1],
    [1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,0,1,0,0,1],
    [1,0,1,0,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,1],
    [1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1,0,1,1],
    [1,0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1],
    [1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,1,0,1,1],
    [1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,1,1,0,0,1,1,1,0,1,1,0,1],
    [1,0,1,1,1,1,0,0,1,0,1,1,0,0,1,0,1,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,1],
    [1,0,0,1,1,1,1,0,0,1,0,1,0,0,1,0,0,1,0,1],
    [1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,1,1,1,0,1,0,1,0,0,0,0,1,1,1],
    [1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1],
    [1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
])

#Inicializar de punto inicial y final 
punto_inicial = (0, 0)
meta = (19, 19)


#Posicion inicial de los agentes
def posicion_inicial_agente(maze):
    #(filas=20, columnas=20)
    filas, columnas = maze.shape

    while True:
        #Selecciona una fila aleatoria del tamano del total de filas
        fila = random.randint(0, filas-1)
        #Selecciona una columna aleatoria del tamano del total de filas
        col = random.randint(0,columnas-1)

        #Esa posicion no es un muro
        if maze[fila,col]==0:
            #Devuelve la coordenada
            return(fila,col)
        

#Tipos de movimiento
movimientos = [(-1,0),(0,1),(1,0),(0,-1)]

def dfs(maze,punto_inicial,meta):
    #Lista para manejar los nodos por explorar (pila)
    pila = [(punto_inicial,[])]
    #Matriz de visitados
    filas = np.shape(maze)[0]
    columnas = np.shape(maze)[1]
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
    return [],considerados


def bfs(maze, punto_inicial, meta):
    # Cola para manejar los nodos por explorar (FIFO)
    cola = [(punto_inicial, [])]
    # Matriz de visitados
    filas = np.shape(maze)[0]
    columnas = np.shape(maze)[1]
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

        #Marca el nodo actual como visitado dentro del laberinto
        visitados[nodo_actual[0], nodo_actual[1]] = 1
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            # Verificar que el vecino esté dentro del laberinto y no haya sido visitado
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                if (maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0):
                    #cola.append((nueva_posicion, camino + [nodo_actual]))
                    mi_append(cola, (nueva_posicion, camino + [nodo_actual]))
    return [], considerados

#Funcion que reemplaza append en bfs
def mi_append(lista, elemento):
    #"""Agrega un elemento al final de la lista."""
    lista += [elemento]  # Usamos la concatenación para evitar append.
   
    
def main():
    print("Carrera de agentes")
    agente_uno_pos= posicion_inicial_agente(maze)
    agente_dos_pos= posicion_inicial_agente(maze)
    
    #Si son iguales se cambia de posicion al agente2
    while agente_uno_pos == agente_dos_pos:
        agente_dos_pos = posicion_inicial_agente(maze)

    print(f"Posicion agente DFS: {agente_uno_pos}")
    print(f"Posicion agente BFS: {agente_dos_pos}")
    print(f"Meta:{meta} ")

    cont_movimientos=0
    movimientos_totales=100
    
    #Obtenemos los caminos de los agentes
    #AGENTE 1 CON DFS
    camino_dfs, _=dfs(maze,agente_dos_pos,meta)
    #AGENTE 2 CON BFS
    camino_bfs, _ = bfs(maze, agente_dos_pos, meta)

    if not camino_dfs and not camino_bfs:
        print("No se encontró un camino para ninguno de los agentes.")
        return
    elif not camino_dfs:
        print("DFS no encontró un camino.")
    elif not camino_bfs:
        print("BFS no encontró un camino.")

    indice_dfs = 0
    indice_bfs = 0
    
    while cont_movimientos < movimientos_totales:
        cont_movimientos+=1

        #AGENTE 1 CON DFS
        if indice_dfs < len(camino_dfs):
            agente_uno_pos = camino_dfs[indice_dfs]
            indice_dfs += 1

            #Revisar si el agente llego a la meta
            if agente_uno_pos == meta:
                print(f"Agente DFS en {agente_uno_pos} ha ganado en {cont_movimientos} movimientos.")
                return

        #AGENTE 2 CON BFS
        if indice_bfs < len(camino_bfs):
            agente_dos_pos = camino_bfs[indice_bfs]
            indice_bfs += 1

            #Revisar si el agente llego a la meta
            if agente_dos_pos == meta:
                print(f"Agente BFS en {agente_dos_pos} ha ganado en {cont_movimientos} movimientos.")
                return 

        print(f"Turno {cont_movimientos}:")
        print(f"  Agente DFS en {agente_uno_pos}")
        print(f"  Agente BFS en {agente_dos_pos}")


main()