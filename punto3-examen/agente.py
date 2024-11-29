#Crea un agente inteligente que sólo pueda moverse a la derecha, si encuentra el nodo meta (puesto al azar)
#el programa para, si llega al extremo diagonal, al azar puede subir o bajar una columna y volver a moverse en
#diagonal, así hasta que encuentre solución. Graficar los movimientos

from matplotlib.pylab import randint
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

def obtenerMeta():
    x = randint(1, 14)
    y = randint(1, 14)
    #print(f"x es {x}, y es {y}")
    if(maze[x][y] == 1):
        obtenerMeta()
    else:
        return (x, y)

#Punto inicial y punto final
inicio = (1, 1)
meta = obtenerMeta()
#Movimientos disponibles
#Derecha, arriba izq, arriba der, abajo izq, abajo der, abajo, arriba
movimientos = [(0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0)]

def busqueda(inicio, meta, maze):
    camino = []
    encontrado = False
    nodo_actual = inicio

    while encontrado == False:
        print("buscando\n")
        
        if nodo_actual == meta:
            encontrado = True
            return camino
        
        if(nodo_actual[0] == 13 or nodo_actual[1] == 13 or nodo_actual[0] == 1 or nodo_actual[1] == 1):
            if(nodo_actual[1] == 1):
                nodo_actual = nodo_actual + movimientos[5]
                camino = camino + [nodo_actual]
            elif(nodo_actual[1] == 13):
                nodo_actual = nodo_actual + movimientos[6]
                camino = camino + [nodo_actual]
            else:
                eleccion = randint(0,1)
                if(eleccion == 0):
                    nodo_actual = nodo_actual + movimientos[5]
                    camino = camino + [nodo_actual]
                else:
                    nodo_actual = nodo_actual + movimientos[6]
                    camino = camino + [nodo_actual]
        
        movimiento_derecha = nodo_actual + movimientos[0]
        if(maze[nodo_actual[0]][movimiento_derecha[1]] == 1):
            nodo_actual = nodo_actual + movimientos[randint(1, 4)]
            camino = camino + [nodo_actual]

        nodo_actual = nodo_actual + movimientos[0]
        camino = camino + [nodo_actual]
    
    #return camino

def desplegar(maze, camino):
    plt.imshow(maze,cmap = 'binary')
    if camino:
        for j in camino:
            plt.plot(j[1],j[0],'o',color = 'red')
    plt.show()

camino = busqueda(inicio, meta, maze)
desplegar(maze, camino)