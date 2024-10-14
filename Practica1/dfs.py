import time
import tracemalloc

def dfs(grafo, nodo_raiz):
    # Inicio de medición de memoria y tiempo
    tracemalloc.start()
    start_time = time.time()

    # Usamos una lista para simular una pila
    pila = [nodo_raiz]

    # Lista para marcar los nodos visitados
    visitados = [False] * (len(grafo) + 1)

    while pila:
        # Sacamos el último nodo usando nuestra función `pop`
        nodo_actual, pila = pop(pila)

        # Si no ha sido visitado, lo marcamos y lo mostramos
        if not visitados[nodo_actual]:
            print(nodo_actual)
            visitados[nodo_actual] = True

            # Agregamos los vecinos no visitados a la pila
            for vecino in grafo[nodo_actual]:
                if not visitados[vecino]:
                    pila = push(vecino, pila)

    # Finaliza medición de memoria y tiempo
    memoria_consumida = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Tiempo de ejecución: {time.time() - start_time:.6f} segundos")
    print(f"Memoria usada: {memoria_consumida[1] / 1024:.2f} KB")

def push(elemento, pila):
    # Crear una nueva lista con un elemento adicional
    nueva_pila = [0] * (len(pila) + 1)

    # Copiar los elementos existentes
    for i in range(len(pila)):
        nueva_pila[i] = pila[i]

    # Añadir el nuevo elemento al final
    nueva_pila[len(pila)] = elemento

    return nueva_pila

def pop(pila):
    # Obtenemos el último elemento
    elemento = pila[-1]

    # Creamos una nueva lista sin el último elemento
    nueva_pila = [0] * (len(pila) - 1)
    for i in range(len(nueva_pila)):
        nueva_pila[i] = pila[i]

    # Devolvemos el elemento eliminado y la lista modificada
    return elemento, nueva_pila

# Grafo de ejemplo representado como lista de adyacencia
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

# Llamamos a la función DFS con el nodo raíz 1
dfs(grafo, 1)
