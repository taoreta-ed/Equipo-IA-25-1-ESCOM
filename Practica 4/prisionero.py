import numpy as np
import matplotlib.pyplot as plt

prisionero1 = 'Cooperar'
prisionero2 = 'Cooperar'

def evaluacion_prisionero(prisionero1, prisionero2):
    if prisionero1 == 'Cooperar' and prisionero2 == 'Cooperar':
        return (3,3)
    elif prisionero1 == 'Cooperar' and prisionero2 =='Traicionar':
        return(5,0)
    elif prisionero1 == 'Traicionar' and prisionero2 == 'Cooperar':
        return(0,5)
    else:
        return(10,10)
    

sentencia = evaluacion_prisionero(prisionero1,prisionero2)

print(f"El prisionero 1 tiene una condena de {sentencia[0]} y el prisionero 2 tiene una condena de {sentencia[1]}")


# En este ejercicio se parte de la idea de tener un agente que en un plano cartesiano, donde este se puede mover en cualquier direccion 
# encuentre el punto de meta a traves de sumar su posicion en 1 en cada iteracion

meta = [5,9]

def buscador(meta):
    pos_obj= [np.random.randint(0,20),np.random.randint(0,20)]

    #Definimos dos variables para cada posicion 
    pos_obj_x =  pos_obj[0]
    pos_obj_y = pos_obj[1]

    #Listas para el guardado de las diferentes posiciones
    camino_x = [None]*4000
    camino_y = [None]*4000

    cantidad_movimientos= 0

    while(pos_obj != meta):
        if (pos_obj_x < meta[0]):
            pos_obj_x = pos_obj_x + 1
        elif (pos_obj_x > meta[0]):
            pos_obj_x = pos_obj_x -1
        #se guarda la posicion en x 
        camino_x[cantidad_movimientos] = pos_obj_x

        if (pos_obj_y < meta[1]):
            pos_obj_y = pos_obj_y + 1
        elif (pos_obj_y > meta[1]):
            pos_obj_y = pos_obj_y -1
        #se guarda la posicion en y
        camino_y[cantidad_movimientos] = pos_obj_y
            

    #Cuantos movimientos hice
    cantidad_movimientos = cantidad_movimientos + 1
    pos_obj[0] = pos_obj_x
    pos_obj[1] = pos_obj_y

    return camino_x,camino_y


camino_x, camino_y = buscador(meta)

#GRAFICACION
plt.plot(camino_x,camino_y,'rx', markersize =12,label="Meta")
plt.plot(camino_x,camino_y,'rx', markersize =12,label="Mov agente")
plt.xlabel('X')
plt.xlabel('Y')
plt.title('Exploracion del entorno por el agente')
plt.legend()
plt.grid(True)




# camino_x,camino_y = buscador(meta)
    

