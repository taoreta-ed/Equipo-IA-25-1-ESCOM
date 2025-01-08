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
    ["Lucía","Matías"],     #8
    ["Matías","Diego"],     #9
    ["Elena","Luis"]       #10
]

def padres():
    padre = []
    hijo = []
    relacionHijo = {}
        
    #Determinar quién es hijo de quién en un diccionario
    for i in range(len(relaciones)):
        padre += [relaciones[i][0]]
        hijo += [relaciones[i][1]]
        if padre[i] not in relacionHijo:
            relacionHijo[padre[i]] = []
        relacionHijo[padre[i]] += [hijo[i]]
    return relacionHijo

#print(padres())

def parejas():
    padre = padres()
    relacionPareja = {}
    relacionPadreHijo = {}

    for padre,hijos in padre.items():
        for hijo in hijos:
            if hijo not in relacionPadreHijo:
                relacionPadreHijo[hijo] = []
            relacionPadreHijo[hijo] += [padre]
    
    # Determinamos las parejas: dos o más padres para el mismo hijo
    for hijo, lista_padres in relacionPadreHijo.items():
        if len(lista_padres) > 1:
            relacionPareja[hijo] = lista_padres
    
    return relacionPareja

print(parejas())

def tios():
    return

def abuelos():
    relacionHijo = padres()
    relacionAbuelos = {}

    for padre in relacionHijo:
        for hijo in relacionHijo[padre]:
            if hijo in relacionHijo:
                if padre not in relacionAbuelos:
                    relacionAbuelos[padre] = []
                relacionAbuelos[padre].extend(relacionHijo[hijo])

    return relacionAbuelos

#print("Relaciones de abuelos y nietos:", abuelos())


#    padre,hijo = hijos()
#    for i in range(len(relaciones)):
#        for j in range(len(relaciones)):
#            if(padre[i] == hijo[j]):
#                abuelo += [padre[i]]
#    return abuelo

#abuelo = abuelos()
#print(f"Abuelo: {abuelo}")

#abuelo()

#diagnosticos = []
#for i in range (len(pacientes)):
#    nombre_paciente = pacientes[i][0]
#    paciente_sintoma = pacientes[i][1]

#    coincidencias_total = 0
#    enfermedad_diagnosticada = "No sé"

#    for j in range(len(enfermedades)):
#        nombre_enfermedad = enfermedades[j][0]
#        nombre_sintoma = enfermedades[j][1]

#        coincidencias = 0

#        for k in range(len(paciente_sintoma)):
#            for l in range(len(nombre_sintoma)):
#                if paciente_sintoma[k] == nombre_sintoma[l]:
#                    coincidencias += 1

#        if coincidencias > coincidencias_total:
#            coincidencias_total = coincidencias
#            enfermedad_diagnosticada = nombre_enfermedad
    
#    diagnosticos = diagnosticos + [[nombre_paciente,enfermedad_diagnosticada]]

#for m in range(len(diagnosticos)):
#    print(f"{diagnosticos[m][0]}: diagnóstico probable => {diagnosticos[m][1]}")
