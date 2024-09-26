import time
import tracemalloc

def bfs(grafo, nodo_raiz):
    ##Medicion de tiempo
    tracemalloc.start()
    start_time = time.time()

    ##Definir una lista o arreglo que vaya guardando los datos
    previos = [nodo_raiz]

    ##Definir una lista para guardar los nodos visitados
    visitados = [False]*(len(grafo)+1)

    ##Cambiar a True el nodo raiz en visitados
    visitados[nodo_raiz] = True

    i = 0
    while i < len(previos):
        ##Llegamos a un nivel
        nodo_actual = previos[i]
        print(nodo_actual)

        ##Recorremos los nodos
        for vecino in grafo[nodo_actual]:
            ##Si el nodo vecino que estoy revisando no lo he visitado, cambio su estado a visitado
            if not visitados[vecino]:
                visitados[vecino] = True

                ##Este nodo vecino es agregado a la lista de previos
                ##previos = previos + [vecino]
                previos = push(vecino, previos)
                print("Salio del push")
    i = i + 1;

def push(vecino, previos):
    ##listaNueva = [False]*(len(previos) + 2)
    for i in (0, len(previos) + 1):
        if i < len(previos):
            listaNueva[i] = previos[i]
        listaNueva[i] = vecino
    return listaNueva

grafo = {
    1:[3, 2],
    2:[1],
    3:[1]
}

bfs(grafo, 1)