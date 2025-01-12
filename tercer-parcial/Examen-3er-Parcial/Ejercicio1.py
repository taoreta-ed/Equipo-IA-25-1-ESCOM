# Ejercicio 1 
#  Realizar una base de conocimiento que tenga Nombre del alumno y materias tomadas. 3 materias máximo (Int. Artificial, ML y Procesamiento de Lenguaje)
#  Determinar si el alumno puede tomar una cuerta materia. Si ha tomado las 3 materias, no puede tomar más.
#  Si ha tomado 2 materias, arrojar la única tercera que no ha tomado.
#  Si solamente tomó 1 materia arroja las 2 posibles materias que puede tomar. 
alumnos = [
    ["Cassandra",["Inteligencia Artificial","Machine Learning","Procesamiento de Lenguaje"]],
    ["Ramón",["Machine Learning"]],
    ["Eduardo",["Inteligencia Artificial","Procesamiento de Lenguaje"]],
    ["Pieck",["Inteligencia Artificial","Machine Learning","Procesamiento de Lenguaje","Cálculo"]]
]

materias = ["Inteligencia Artificial","Machine Learning","Procesamiento de Lenguaje"]

for i in range(len(alumnos)):
    alumno = alumnos[i][0]
    materias_tomadas = alumnos[i][1]

    coincidencia_total = 0

    #Determinar si el alumno tiene más de 3 materias
    if(len(materias_tomadas) > 3):
        print(f"{alumno} no puede tomar más de 3 materias")

    #Determinar si el alumno ya ha tomado las 3 materias
    if len(materias_tomadas) == 3:
        print(f"{alumno} ya ha tomado las 3 materias")

    #Determinar si el alumno ha tomado 2 materias
    if len(materias_tomadas) == 2:
        for j in range(len(materias)-1):
            for k in range(len(materias_tomadas)-1):
                if materias[j] != materias_tomadas[k]:
                    print(f"{alumno} puede tomar la materia {materias[j]}")    

    #Determinar si el alumno ha tomado 1 materias
    if len(materias_tomadas) == 1:
        for j in range(len(materias)):
            for k in range(len(materias_tomadas)):
                if materias[j] != materias_tomadas[k]:
                    print(f"{alumno} puede tomar la materia {materias[j]}")
