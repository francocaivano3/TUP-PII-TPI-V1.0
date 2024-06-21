from partida import Partida
from jugador import Jugador 
from datos import * 

def agregarMazo(nuevaPartida:Partida, listaPreguntas:list):
        for pregunta in listaPreguntas:
            nuevaPartida.mazo.append(pregunta)

def menu():
    print("Bienvenidos/as.\n1- Iniciar juego.\n2- Mostrar puntuaciones\n3- Finalizar")

def nuevoJuego():
    nuevaPartida = Partida()
    agregarMazo(nuevaPartida, listaPreguntas)
    
    jugador1 = Jugador(input("Ingrese el nombre del Jugador 1: ")) #Simplificarlo con un for
    nuevaPartida.ingresarJugadores(jugador1)
    print(f"Se ha añadido al Jugador 1: '{jugador1.nombre}'\n")

    jugador2 = Jugador(input("Ingrese el nombre del Jugador 2: "))
    nuevaPartida.ingresarJugadores(jugador2)
    print(f"Se ha añadido al Jugador 2: '{jugador2.nombre}'\n")

    jugador3 = Jugador(input("Ingrese el nombre del Jugador 3: "))
    nuevaPartida.ingresarJugadores(jugador3)
    print(f"Se ha añadido al Jugador 3: '{jugador3.nombre}'\n")

    jugador4 = Jugador(input("Ingrese el nombre del Jugador 4: "))
    nuevaPartida.ingresarJugadores(jugador4)
    print(f"Se ha añadido al Jugador 4: '{jugador4.nombre}'\n")

    
    while len(nuevaPartida.mazo) > 0:
        for jugador in nuevaPartida.listaJugadores:
            if jugador.turno == True:
                tarjeta = nuevaPartida.generarPregunta()
                jugador.responder(tarjeta, nuevaPartida)
    print('Ha acabado el juego.\n')
    
    nuevaPartida.mostrarRanking(nuevaPartida)



while True:
    menu()
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        nuevoJuego()
        break



