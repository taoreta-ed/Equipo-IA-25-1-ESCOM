# b) Cuando el programa se inicie debera de pedirle al usuario la coordenada de fin y de inicio 
#    y despliegue 4 laberintos cada uno ejecutado con cada algoritmo y se ponga ARRIBA DE LA 
#    IMAGEN (DENTRO DE LA IMAGEN) DEL LABERINTO SU TIEMPO DE EJECUCION DE CADA UNO

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import heapq 
import time
import tracemalloc

#Laberinto de 20x35 con 1 representado por paredes y 0 por caminos
maze = np.array([
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,0,0,0,1],
    [1,0,1,0,1,1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,1],
    [1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0,0,0,1,0,1,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1],
    [1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1,1,1,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,1,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,0,1,1,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,1,1,0,0,1,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
])

#Tipos de movimiento
movimientos = [(-1,-1),(-1,0),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

#Inicializar punto inicial y punto final con coordenadas proporcionadas por el usuario
def coordenada_inicial():
  inicial = input("Ingrese la coordenada del punto inicial:")
  x,y = map(int,inicial.split(","))
  return x,y

def coordenada_meta():
  inicial = input("Ingrese la coordenada de la meta:")
  x,y = map(int,inicial.split(","))
  return x,y

punto_inicial = coordenada_inicial()
meta = coordenada_meta()

#Validar que las coordenadas ingresadas estén dentro del laberinto
filas,columnas = maze.shape
# Validar si el punto inicial y la meta son válidos
if (0 <= punto_inicial[0] < filas and 0 <= punto_inicial[1] < columnas and maze[punto_inicial[0], punto_inicial[1]] == 0):
    if (0 <= meta[0] < filas and 0 <= meta[1] < columnas and maze[meta[0], meta[1]] == 0):
        ## Comienza algoritmo DFS
        def DFS(maze,punto_inicial,meta):
            # Medición de tiempo y memoria
            tracemalloc.start()
            start_time = time.time()
            #Lista para manejar los nodos por explorar (pila)
            pila = [(punto_inicial,[])]
            #Matriz de visitados
            filas,columnas = maze.shape
            visitados = np.zeros((filas,columnas))
            #Marcamos el nodo inicial como visitados
            #Definir una lista que contenga a todos los nodos que he visitado
            considerados = []

            while len(pila) > 0:
                nodo_actual, camino = pila[-1]
                pila = pila[:-1]

                #Guarda todos los nodos que han sido evaluados aunque no formen parte del camino final
                visitados[nodo_actual[0], nodo_actual[1]] = 1
                considerados += [nodo_actual]

                if nodo_actual == meta:
                    return camino + [nodo_actual],considerados

                for direccion in movimientos:
                    nueva_posicion = (nodo_actual[0] + direccion[0],nodo_actual[1] + direccion[1])
                    #Ver que el vecino (nueva posición) este dentro del laberinto
                    if ((0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas)):
                        ## Ver si el nodo a evaluar (nueva_posicion)  es un camino accesible y ademas si ese nodo no lo he visitado
                        if (maze[nueva_posicion[0], nueva_posicion[1]]) == 0 and (visitados[nueva_posicion[0], nueva_posicion[1]]==0):
                            pila += [(nueva_posicion, camino + [nodo_actual])]
            return camino,considerados

        ## Comienza algoritmo BFS
        def BFS(maze,punto_inicial,meta):
            # Inicializar la cola y otros parámetros
            cola = [(punto_inicial, [])]
            #Matriz de visitados
            filas, columnas = maze.shape
            visitados = np.zeros((filas, columnas))
            visitados[punto_inicial[0], punto_inicial[1]] = 1
            #Definir una lista que contenga a todos los nodos que he visitado
            considerados = []

            while len(cola) > 0:
                nodo_actual, camino = mi_pop(cola)
                #Guarda todos los nodos que han sido evaluados aunque no formen parte del camino final
                considerados += [nodo_actual]
                
                if nodo_actual == meta:
                    return camino + [nodo_actual],considerados
                
                for movimiento in movimientos:
                    nueva_posicion = (nodo_actual[0] + movimiento[0], nodo_actual[1] + movimiento[1])

                    # Verificar que el vecino esté dentro del laberinto y no haya sido visitado
                    if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                        if (maze[nueva_posicion[0], nueva_posicion[1]] == 0) and (visitados[nueva_posicion[0], nueva_posicion[1]] == 0):
                            visitados[nueva_posicion[0], nueva_posicion[1]] = 1
                            mi_append(cola, (nueva_posicion, camino + [nodo_actual]))
            return camino,considerados

        # Funciones auxiliares
        def mi_append(lista, elemento):
            lista += [elemento]

        def mi_pop(lista):
            elemento = lista[0]
            lista[:] = lista[1:]
            return elemento

        ## Comienza algoritmo A*
        def heuritica_chebyshev(nodo_actual,objetivo):
            d0 = abs(nodo_actual[0] - objetivo[0])
            d1 = abs(nodo_actual[1] - objetivo[1])
            return max(d0,d1)

        def A_estrella(maze,punto_inicial,meta):
            #Lista para manejar los nodos por explorar (pila)

            #lista_abierta = [(punto_inicial,0,heuristica(punto_inicial,meta),[])]
            lista_abierta = [(punto_inicial,0,heuritica_chebyshev(punto_inicial, meta),[])]
            
            #lista_abierta = (nodo,g,f,camino)
            considerados = []

            #Matriz de visitados
            filas = np.shape(maze)[0]
            columnas = np.shape(maze)[1]
            lista_cerrada = np.zeros((filas,columnas))

            while len(lista_abierta) > 0:
                menor_f = lista_abierta[0][2]
                nodo_actual,g_actual,f_actual,camino_actual = lista_abierta[0]

                #Se recorre la posición 2 de la fila 1 (distancia Manhattan) de la lista abierta preguntado cual es el de menor valor
                indice_menor_f = 0
                for i in range(1,len(lista_abierta)):
                    if lista_abierta[i][2] < f_actual:
                        menor_f = lista_abierta[i][2]
                        nodo_actual,g_actual,f_actual,camino_actual = lista_abierta[i]
                        indice_menor_f = i

                #Eliminarlo de la lista abierta
                lista_abierta = lista_abierta[:indice_menor_f] + lista_abierta[indice_menor_f + 1:]

                #Guarda todos los nodos que han sido evaluados aunque no formen parte del camino final
                considerados += [nodo_actual]

                #Evaluamos si el nodo actual es o no el nodo meta
                if nodo_actual == meta:
                    return camino_actual + [nodo_actual],considerados
                
                #Agregar a la lista cerrada
                lista_cerrada[nodo_actual[0],nodo_actual[1]] = 1

                for direccion in movimientos:
                    nueva_posicion = (nodo_actual[0] + direccion[0],nodo_actual[1] + direccion[1])
                    #Ver que el vecino (nueva posición) esté dentro del laberinto
                    if((0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas)):
                    #Ver si el nodo a evaluar (nueva posición) es un camino accesible y además si ese nodo NO LO HEMOS VISITADO
                        if((maze[nueva_posicion[0],nueva_posicion[1]]) == 0 and lista_cerrada[nueva_posicion[0],nueva_posicion[1]] == 0):
                            #Evaluamos si la dirección es o no diagonal
                            dado6 = random.randint(1,6)
                            dado10 = random.randint(1,10)
                            if(abs(direccion[0]) + abs(direccion[1])) == 2:
                                g_nuevo = g_actual + dado10
                            else:
                                g_nuevo = g_actual + dado6

                            # f_nuevo = g_nuevo + heuristica(nueva_posicion,meta)
                            f_nuevo = g_nuevo + heuritica_chebyshev(nueva_posicion,meta)
                            bandera_lista = False

                            for nodo,g,f,camino in lista_abierta:
                                if nodo == nueva_posicion and g <= g_nuevo:
                                    bandera_lista = True
                                    break

                            if bandera_lista == False:
                                lista_abierta += [(nueva_posicion,g_nuevo,f_nuevo,camino_actual + [nueva_posicion])]

            return camino,considerados

        ## Comienza algoritmo Dijsktra
        def Dijkstra(maze,punto_inicial,meta):
            # Cola de prioridad para manejar los nodos según su costo
            cola_prioridad = [(0, punto_inicial, [])]  # (costo_acumulado, posición, camino)
            # Matriz de costos acumulados, inicializada con infinito
            filas, columnas = maze.shape
            costos = np.full((filas, columnas), np.inf)
            costos[punto_inicial] = 0
            # Matriz para los nodos visitados
            visitados = np.zeros((filas, columnas), dtype=bool)
            # Para visualización de nodos considerados
            considerados = []

            while cola_prioridad:
                # Extraer el nodo con menor costo acumulado
                costo_actual, nodo_actual, camino = heapq.heappop(cola_prioridad)
                
                #Guarda todos los nodos que han sido evaluados aunque no formen parte del camino final
                considerados += [nodo_actual]
                
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
                        if maze[nueva_posicion] == 0 and not visitados[nueva_posicion]:
                            nuevo_costo = costo_actual + 1  # Peso 1 para cada movimiento
                            # Si encontramos un camino más barato a nueva_posicion, lo actualizamos
                            if nuevo_costo < costos[nueva_posicion]:
                                costos[nueva_posicion] = nuevo_costo
                                heapq.heappush(cola_prioridad, (nuevo_costo, nueva_posicion, camino + [nodo_actual]))

            return camino,considerados

        # Lista de funciones de los algoritmos y sus nombres
        algoritmos = [DFS,BFS,A_estrella,Dijkstra]
        nombres_algoritmos = ['DFS','BFS','A*','Dijkstra']

        # Inicializa las listas para almacenar los resultados
        caminos = []
        considerados_a = []
        tiempos = []

        # Ejecutar cada algoritmo y medir su tiempo de ejecución
        for algoritmo in algoritmos:
            inicio = time.time()
            camino, considerados = algoritmo(maze, punto_inicial, meta)
            fin = time.time()
            tiempo_ejecucion = fin - inicio

            caminos += [camino]
            considerados_a += [considerados]
            tiempos += [tiempo_ejecucion]

        def animar_algoritmos(maze,caminos,considerados_a,nombres_algoritmos,tiempos):
            fig, axes = plt.subplots(2,2,figsize=(10,10))
            axes = axes.flatten()

            animaciones = []

            for i in range(4):
                ax = axes[i]
                camino = caminos[i]
                considerados = considerados_a[i]
                nombre = nombres_algoritmos[i]
                tiempo = tiempos[i]

                ax.imshow(maze, cmap='binary')
                ax.set_title(f'Algoritmo {nombre} - Tiempo: {tiempo:.6f}s')

                explorados_x = [nodo[0] for nodo in considerados]
                explorados_y = [nodo[1] for nodo in considerados]
                camino_x = [nodo[0] for nodo in camino]
                camino_y = [nodo[1] for nodo in camino]

                puntos_considerados, = ax.plot([],[],'o',color='blue',markersize=2)
                puntos_camino, = ax.plot([],[],'o', color='red',markersize=2)

                total_frames = len(explorados_x) + len(camino_x)

                def actualizar(frame, puntos_considerados, puntos_camino, explorados_x, explorados_y, camino_x, camino_y):
                    if frame < len(explorados_x):
                        puntos_considerados.set_data(explorados_y[:frame + 1], explorados_x[:frame + 1])
                    else:
                        idx = frame - len(explorados_x)
                        puntos_camino.set_data(camino_y[:idx + 1], camino_x[:idx + 1])
                    return puntos_considerados, puntos_camino

                anim = animation.FuncAnimation(
                    fig, actualizar, frames=total_frames, interval=100, blit=False,
                    fargs=(puntos_considerados, puntos_camino, explorados_x, explorados_y, camino_x, camino_y),
                    repeat=False)
                animaciones.append(anim)

            plt.tight_layout()
            plt.show()

        animar_algoritmos(maze,caminos,considerados_a,nombres_algoritmos,tiempos)

    else:
        print("Meta no válida.")
        # No ejecutar los laberintos
else:
    print("Punto inicial no válido.")
    # No ejecutar los laberintos
