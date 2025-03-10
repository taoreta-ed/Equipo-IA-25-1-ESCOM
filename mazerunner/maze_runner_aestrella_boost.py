import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

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

#Inicializar punto inicial y punto final
punto_inicial = (1,1)
meta = (1,8)
#Tipos de movimiento
movimientos = [(-1,-1),(-1,0),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

def heuritica_chebyshev(nodo_actual,objetivo):
  d0 = abs(nodo_actual[0] - objetivo[0])
  d1 = abs(nodo_actual[1] - objetivo[1])
  return max(d0,d1)

def animar_recorrido(maze,consideradosB = None,camino = None):
    figura, ax = plt.subplots()
    ax.imshow(maze,cmap="binary")

    # Inicializar los puntos
    puntos_considerados, = ax.plot([],[],"o", color="blue")
    puntos_camino, = ax.plot([],[],"o", color="red")

    # Crear arrays para las coordenadas
    explorados_x = [nodo[0] for nodo in consideradosB]
    explorados_y = [nodo[1] for nodo in consideradosB]
    camino_x = [nodo[0] for nodo in camino]
    camino_y = [nodo[1] for nodo in camino]

    def actualizar(frame):
        # Mostrar los nodos explorados hasta el frame actual
        if frame < len(consideradosB):
            puntos_considerados.set_data(explorados_y[:frame + 1], explorados_x[:frame + 1])
        # Mostrar el camino hasta el frame actual
        if frame >= len(consideradosB):
            idx = frame - len(consideradosB)
            puntos_camino.set_data(camino_y[:idx + 1], camino_x[:idx + 1])
        # Detener la animación una vez que se haya mostrado todo
        if frame == len(consideradosB) + len(camino) - 1:
            animacion.event_source.stop()

        return puntos_considerados,puntos_camino

    total_frames = len(consideradosB) + len(camino)
    animacion = animation.FuncAnimation(figura,actualizar,frames=total_frames,interval=50,blit=False)
    plt.show()

    # Contadores
    print(f"Total de bolitas azules (nodos explorados): {len(consideradosB)}")
    print(f"Total de bolitas rojas (camino final): {len(camino)}")

def A_estrella_B(maze,punto_inicial,meta):
  #Lista para manejar los nodos por explorar (pila)

  #lista_abierta = [(punto_inicial,0,heuristica(punto_inicial,meta),[])]
  lista_abierta = [(punto_inicial,0,heuritica_chebyshev(punto_inicial, meta),[])]
  
  #lista_abierta = (nodo,g,f,camino)
  consideradosB = []

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
      consideradosB += [nodo_actual]

      #Evaluamos si el nodo actual es o no el nodo meta
      if nodo_actual == meta:
          return camino_actual + [nodo_actual],consideradosB
      
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

  return None,consideradosB

camino,consideradosB = A_estrella_B(maze,punto_inicial,meta)
animar_recorrido(maze, consideradosB, camino)
