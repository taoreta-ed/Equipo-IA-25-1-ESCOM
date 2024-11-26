#pacientes con sus sintomas asociados
pacientes = [
    ["Juan", ["tos", "fiebre", "dificultad para respirar"]],
    ["Ana", ["diarrea", "dolor abodminal","vomitos"]],
    ["Carlos"], ["sed excesiva", "orinar frecuentemente", ""]
]

#Enfermedades con sus sintomas caractersticas
enfermedades = [
    ["infeccion respiratoria", ["tos","fiebre","dificultad para respirar"]],
    ["gastroenteritis", ["diarrea","dolor abdominal", "nauseas", "vomito"]],
    ["diabetes", ["sed excesiva","orina frecuentemente","dificultad para respirar"]]
]

for i in range (len(pacientes)):
    nombre_paciente = pacientes[i][0]
    paciente_sintoma= pacientes[i][1]

    coincidencias_total = 0
    enfermedad_diagnosticada = ""

    
    #para ver las enfermedades
    for j in range (len(enfermedades)):
        nombre_enfermedad = enfermedades[j][0]
        nombre_sintoma= enfermedades[j][1]

        coincidencias = 0

        for k in range (len(paciente_sintoma)):
            for l in range(len(nombre_sintoma)):
                if paciente_sintoma == nombre_sintoma:
                    coincidencias +=1
        
        if coincidencias > coincidencias:
            coincidencias_total = coincidencias
            enfermedad_diagnosticada = nombre_enfermedad

        #diagnosticos = diagnosticos + [[nombre_paciente, enfermedad_diagnosticada]]

    for m in range(len(diagnosticos)):
        print(f"{diagnosticos[m][0]}:")




