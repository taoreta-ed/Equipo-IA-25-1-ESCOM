# -*- coding: utf-8 -*-
"""Maze_Runner_Aestrella.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CJvLVJSmnLDYuKynAgGzXJPCxfjMatDU
"""

import matplotlib.pyplot as plt
import numpy as np

#Laberinto de 15x15 con 1 representado por paredes y 0 por caminos
maze = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

#Inicializar punto inicial y punto final
punto_inicial = (1,1)
meta = (1,8)
#Tipos de movimiento
movimientos = [(-1,-1),(-1,0),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

# def heuristica(nodo_actual,objetivo):
#     return (abs(objetivo[0] - nodo_actual[0]) + abs(objetivo[1] - nodo_actual[1]))

def distancia_euclidiana(nodo_actual, objetivo):
  return np.sqrt((objetivo[0] - nodo_actual[0])**2 + (objetivo[1] - nodo_actual[1])**2)


def desplegar_laberinto(maze,camino = None,considerados = None):
    plt.imshow(maze,cmap = 'binary')
    if considerados:
        for i in considerados:
            plt.plot(i[1],i[0],'o',color = 'blue')
    if camino:
        for j in camino:
            plt.plot(j[1],j[0],'o',color = 'red')
    plt.show()


    # Contadores
    print(f"Total de bolitas azules (nodos explorados): {len(considerados)}")
    print(f"Total de bolitas rojas (camino final): {len(camino)}")

def A_estrella(maze,punto_inicial,meta):
  #Lista para manejar los nodos por explorar (pila)

  #lista_abierta = [(punto_inicial,0,heuristica(punto_inicial,meta),[])]
  lista_abierta = [(punto_inicial, 0, distancia_euclidiana(punto_inicial, meta), [])]
  
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
            if(abs(direccion[0]) + abs(direccion[1])) == 2:
              g_nuevo = g_actual + 14
            else:
              g_nuevo = g_actual + 10

            # f_nuevo = g_nuevo + heuristica(nueva_posicion,meta)
            f_nuevo = g_nuevo + distancia_euclidiana(nueva_posicion,meta)
            bandera_lista = False

            for nodo,g,f,camino in lista_abierta:
              if nodo == nueva_posicion and g <= g_nuevo:
                bandera_lista = True
                break

            if bandera_lista == False:
              lista_abierta += [(nueva_posicion,g_nuevo,f_nuevo,camino_actual + [nueva_posicion])]

  return None,considerados

#Ejecutar A* y mostrar el laberitno con el camino y considerados
camino,considerados = A_estrella(maze,punto_inicial,meta)
desplegar_laberinto(maze,camino,considerados)