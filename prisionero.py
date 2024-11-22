#En este ejercicio se parte de la idea de tener un agente que en un plano con dirección,
#encuentre el punto de meta a través de sumar sus posición  en 1
import numpy as np
import matplotlib.pyplot as plt
meta = (5,9)

#def buscador (meta):
pos_objeto = [np.random.randint(0,20),np.random.randint(0,20)]

#Definición de variables para cada posición
pos_objeto_x = pos_objeto[0]
pos_objeto_y = pos_objeto[1]

#listas para el guardado de las diferentes posiciones
camino_x = [None]*4000
camino_y = [None]*4000
cantidad_movimientos = 0

while(pos_objeto != meta):
    if(pos_objeto_x < meta[0]):
        pos_objeto_x = pos_objeto_x + 1
    elif (pos_objeto_x > meta[0]):
        pos_objeto_x = pos_objeto_x - 1
    camino_x[cantidad_movimientos] = pos_objeto_x

    if(pos_objeto_y < meta[1]):
        pos_objeto_y = pos_objeto_y + 1
    elif (pos_objeto_y > meta[1]):
        pos_objeto_y = pos_objeto_y - 1
    camino_y[cantidad_movimientos] = pos_objeto_y

    cantidad_movimientos = cantidad_movimientos + 1
    pos_objeto[0] = pos_objeto_x
    pos_objeto[1] = pos_objeto_y
    #return camino_x,camino_y

#camino_x,camino_y = buscador(meta)

plt.plot(meta[0],meta[1],'rx',markersize=12,label='Meta')
plt.plot(camino_x,camino_y,'o',label='Movimiento Agente')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Exploración del Entorno por el Agente')
plt.legend()
plt.grid(True)
plt.show()

