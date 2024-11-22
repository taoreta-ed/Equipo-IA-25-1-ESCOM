## En este ejercicio se parte de la idea de tener un agente que en un plano cartesiano, donde este se puede mover en cualquier
## direccion, encuentre el punto de meta a traves de sumar su posicion en 1 en cada iteracion
import numpy as np

meta = (5, 9)

def buscador(meta):
    pos_objeto = (np.random.randint(0, 20), np.random.randint(0, 20))

    ## Definimos dos variables para cada posicion
    pos_objeto_x = pos_objeto[0]
    pos_objeto_y = pos_objeto[1]

    ## Listas para el guardado de las diferentes posiciones
    camino_x = [None]
    camino_y = [None]


    while(pos_objeto != meta):
        if (pos_objeto_x < meta[0]):
            pos_objeto_x = pos_objeto_x + 1;
        elif(pos_objeto_x > meta[0]):
            pos_objeto_x = pos_objeto_x - 1;
        
        if (pos_objeto_y < meta[0]):
            pos_objeto_y = pos_objeto_y + 1;
        elif(pos_objeto_y > meta[0]):
            pos_objeto_y = pos_objeto_y - 1;
    
    pos_objeto[0] = pos_objeto_x
    pos_objeto[1] = pos_objeto_y
