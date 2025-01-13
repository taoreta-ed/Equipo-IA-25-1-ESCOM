#Práctica 9 - Lógica de primer orden
## 9) Realizar con lógica de primer orden, la solución de dados únicamente en la base de conocimiento 
#     las relaciones padre-hijo de al menos 10 parejas. Determinar quien es abuelo de quien y quien es tío de quien. 

#Base de conocimientos de las relaciones padre-hijo
relaciones = [
    ["Juan","Pedro"],       #1
    ["Pedro","María"],      #2
    ["Pedro","Luis"],       #3
    ["Lucía","Pedro"],      #4
    ["Carlos","Vanessa"],   #5
    ["Vanessa","Sofía"],    #6
    ["Vanessa","Diego"],    #7
    ["Elena","María"],      #8
    ["Lucía","Matías"],     #9
    ["Matías","Diego"],     #10
    ["Elena","Luis"],       #11
    ["Juan","Matías"],      #12
    ["Matías","Sofía"]      #13
]

def padres():
    padre = []
    hijo = []
    relacionHijo = {}
        
    #Determinar quién es padre de quién en un diccionario
    for i in range(len(relaciones)):
        padre += [relaciones[i][0]]
        hijo += [relaciones[i][1]]
        if padre[i] not in relacionHijo:
            relacionHijo[padre[i]] = []
        relacionHijo[padre[i]] += [hijo[i]]
    
    return relacionHijo

def hijos():
    padre = []
    hijo = []
    relacionPadre = {}
        
    #Determinar quién es hijo de quién en un diccionario
    for i in range(len(relaciones)):
        padre += [relaciones[i][0]]
        hijo += [relaciones[i][1]]
        if hijo[i] not in relacionPadre:
            relacionPadre[hijo[i]] = []
        relacionPadre[hijo[i]] += [padre[i]]
    
    return relacionPadre

def parejas():
    relacionHijos = hijos()
    pareja = {} 
    hijos_comunes = {}

    for hijo, padres in relacionHijos.items():
        if len(padres) == 2:
            padre1, padre2 = padres
            # Verificar si ambos padres no están ya en el diccionario
            if padre1 not in pareja and padre2 not in pareja:
                pareja[padre1] = padre2
            
            # Guardar los hijos únicos
            if padre1 not in hijos_comunes:
                hijos_comunes[padre1] = []
            if padre2 not in hijos_comunes:
                hijos_comunes[padre2] = []
            hijos_comunes[padre1].append(hijo)
            hijos_comunes[padre2].append(hijo)

    # Retornar ambos valores
    return pareja, hijos_comunes

    
def abuelos():
    relacionHijo = hijos()
    #relacionParejas = parejas()
    relacionAbuelos = {}

    for padre in relacionHijo:
        for hijo in relacionHijo[padre]:
            if hijo in relacionHijo:
                if padre not in relacionAbuelos:
                    relacionAbuelos[padre] = []
                for i in relacionHijo[hijo]:
                    relacionAbuelos[padre] += [i]

    return relacionAbuelos

def hermanos():
    relacionPadres = padres()
    procesados = []  # Lista para rastrear personas ya procesadas
    hermanos_unicos = {}

    for padre in relacionPadres:
        hijos = relacionPadres[padre]
        if len(hijos) > 1:  # Considerar solo si hay más de un hijo
            for i in range(len(hijos)):
                hijo = hijos[i]
                if hijo not in procesados:
                    hermanos_unicos[hijo] = []
                    for j in range(i + 1, len(hijos)):  # Evitar redundancia
                        hermano = hijos[j]
                        if hermano not in procesados:
                            hermanos_unicos[hijo] += [hermano]

                    procesados += hijo
                    for hermano in hermanos_unicos[hijo]:
                        procesados += hermano

    # Filtrar personas sin hermanos
    resultado = {}
    for hijo in hermanos_unicos:
        if len(hermanos_unicos[hijo]) > 0:
            resultado[hijo] = hermanos_unicos[hijo]

    return resultado

def tios():
    pareja, hijos_comunes = parejas()  # Obtener los hijos comunes directamente
    relacionHermanos = hermanos()  # Obtener la relación de hermanos
    relacionTios = {}  # Diccionario para almacenar tíos y sobrinos

    # Iterar sobre los padres con hijos comunes
    for padre, hijos in hijos_comunes.items():
        # Verificar si el padre tiene hermanos
        if padre in relacionHermanos:
            # Para cada hermano del padre
            for tio in relacionHermanos[padre]:
                # Si el tío aún no está registrado en el diccionario
                if tio not in relacionTios:
                    relacionTios[tio] = []
                # Agregar los hijos del padre como sobrinos del tío
                for hijo in hijos:
                    if hijo not in relacionTios[tio]:
                        relacionTios[tio].append(hijo)

    return relacionTios



parejas,hijos_comunes = parejas()
print(padres())
print(parejas)
print(hijos_comunes)
print(hijos())
print("\n")
print(abuelos())
print("\n")
print(hermanos())
print(tios())