import random
def juego():
    lista_opciones = ["piedra", "papel", "tijeras"]
    maquina = random.choice(lista_opciones)
    jugador = str(input("Elige piedra, papel o tijera:  "))

    if maquina == jugador:
        print("Empate")
    elif maquina == "piedra" and jugador == "papel":
        print("Ganaste")
    elif maquina == "papel" and jugador == "tijeras":
        print("Ganaste")
    elif maquina == "tijera" and jugador == "piedra":
        print("Ganaste")
    else:
        print("Perdiste:")

juego()
respuesta = str(input("¿Desea Jugar de nuevo?  "))
while respuesta == "si":
    juego()
    respuesta = str(input("¿Desea Jugar de nuevo?  "))