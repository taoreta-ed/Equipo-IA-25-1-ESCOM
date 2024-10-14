import time
import tracemalloc

def bfs(grafo, nodo_raiz, nodo_objetivo):
    # Medición de tiempo y memoria
    tracemalloc.start()
    start_time = time.time()

    # Definir la lista que guarda los nodos por visitar (cola)
    previos = [nodo_raiz]

    # Definir una lista para marcar los nodos visitados
    visitados = [False] * (len(grafo) + 1)
    visitados[nodo_raiz] = True  # Marcar el nodo raíz como visitado

    # Definimos una bandera para saber si el nodo fue encontrado
    bandera = False

    i = 0
    while i < len(previos):
        nodo_actual = previos[i]
        print(nodo_actual)

        # Verificar si hemos encontrado el nodo objetivo
        if nodo_actual == nodo_objetivo:
            bandera = True
            print("Nodo encontrado: ", nodo_objetivo)
            break  # Detener la búsqueda

        # Recorrer los vecinos del nodo actual
        for vecino in grafo[nodo_actual]:
            if not visitados[vecino]:
                visitados[vecino] = True
                previos = push(vecino, previos)  # Agregar a la lista de previos

        i += 1
    
    if not bandera:
        print("El nodo objetivo no fue encontrado")

    # Finaliza medición de memoria y tiempo
    memoria_consumida = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Tiempo de ejecución: {time.time() - start_time:.6f} segundos")
    print(f"Memoria usada: {memoria_consumida[1] / 1024:.2f} KB")

def push(vecino, previos):
    # Crear una nueva lista con tamaño incrementado en 1
    listaNueva = [0] * (len(previos) + 1)

    # Copiar los elementos de 'previos' a 'listaNueva'
    for j in range(len(previos)):
        listaNueva[j] = previos[j]

    # Agregar el nuevo vecino al final de la lista
    listaNueva[len(previos)] = vecino

    return listaNueva

# Definicion del grafo 
grafoBase = {
    1: [2, 3],
    2: [1],
    3: [1]
}

grafo = {
1: [2, 3],
2: [1, 4, 5],
3: [1, 6, 7],
4: [2],
5: [2],
6: [3],
7: [3, 8],
8: [7],
}

# Llamada a la función con nodo objetivo 7
bfs(grafo, 1,55)
