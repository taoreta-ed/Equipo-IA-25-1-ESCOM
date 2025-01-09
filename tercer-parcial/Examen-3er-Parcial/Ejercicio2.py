#Realizar el juego de piedra papel o tijera, el usuario juega contra la máquina
#La máquina tiene que ganarle al profesor

#Importamos la librería random
import random
from time import sleep

def juego():
    print("Juguemos piedra, papel o tijera")
    sleep(1)
    print("Piedra...")
    sleep(1)
    print("Papel...")
    sleep(1)
    print("Tijera...")
    jugador = input("Elige tu opción: ").upper()

    #opciones = ["PIEDRA", "PAPEL", "TIJERA"]
    #maquina = random.choice(opciones)

    if(jugador == "PIEDRA"):
        #maquina = "PAPEL"
        print("Jugador elige PIEDRA y máquina elige PAPEL")
        print("Gana la máquina!")
    elif(jugador == "PAPEL"):
        #maquina = "TIJERA"
        print("Jugador elige PAPEL y máquina elige TIJERA")
        print("Gana la máquina!")
    elif(jugador == "TIJERA"):
        #maquina = "PIEDRA"
        print("Jugador elige TIJERA y máquina elige PAPEL")
        print("Gana la máquina!")
    else:
        print("Opción no válida")
        juego()

juego()