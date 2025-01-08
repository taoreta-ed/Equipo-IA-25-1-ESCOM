#Práctica 9 - Lógica de primer orden
## 9) Realizar con lógica de primer orden, la solución de dados únicamente en la base de conocimiento 
#     las relaciones padre-hijo de al menos 10 parejas. Determinar quien es abuelo de quien y quien es tío de quien. 

#Funcion que genera la relacion padre-hijo
def padre_hijo(padre, hijo):
    return ["padre_hijo", [padre, hijo]]

#Funcion que genera la relacion pareja
def pareja(persona1, persona2):
    return ["pareja", [persona1, persona2]]

#Funcion que genera la relacion abuelo-nieto
#def abuelo_nieto(base_conocimiento, abuelo, nieto):
    #if 