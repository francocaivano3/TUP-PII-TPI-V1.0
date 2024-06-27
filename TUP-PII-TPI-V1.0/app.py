from partida import Partida
from jugador import Jugador 
from datos import * 

def agregarMazo(nuevaPartida:Partida, listaPreguntas:list):
        for pregunta in listaPreguntas:
            nuevaPartida.mazo.append(pregunta)

print("\nBienvenidos/as.")

def menu():
    print("\n1- Iniciar nuevo juego.\n2- Mostrar puntuaciones de la última partida.\n3- Finalizar.")
    

def nuevoJuego():
    agregarMazo(nuevaPartida, listaPreguntas)
    while True:
        try:
            cantJugadores = int(input("Ingrese el número de jugadores (de 2 a 4): "))
            break
        except ValueError:
            print("No ha ingresado un número")
            
    while cantJugadores < 2 or cantJugadores > 4:
        cantJugadores = int(input("Ingrese un número de 2 a 4: "))

    if cantJugadores == 2:
        cantJugadores = 3

    elif cantJugadores == 3:
        cantJugadores = 4
    
    elif cantJugadores == 4:
        cantJugadores = 5
    
    

    for i in range(1, cantJugadores):
        print("\n")
        jugador = Jugador(input(f"Ingrese el nombre del jugador {i}: "))             
        nuevaPartida.ingresarJugadores(jugador)
        print(f"Se ha añadido el jugador número {i}: {jugador.nombre}")
        
    ronda = 0

    while len(nuevaPartida.mazo) > 0:
        ronda = ronda + 1
        
        for jugador in nuevaPartida.listaJugadores:
            
            if jugador.turno == True and len(nuevaPartida.mazo) > 0:
                if jugador.cantRespuestasAcertadas == 3 and jugador.beneficio: 
                    jugador.beneficio = False

                    print("\n════════════════════════════════════════════════════════")
                    print(f"El jugador {jugador.nombre} tiene el beneficio del turno extra!")
                    print("════════════════════════════════════════════════════════")

                    tarjeta = nuevaPartida.generarPregunta()
                    print(f"{tarjeta}")
                    print(f"\nRonda: {ronda}")
                    print(f"Turno del jugador N°{jugador.id}: {jugador.nombre}")

                    if jugador.responder(tarjeta, nuevaPartida):
                        print("\nRespuesta correcta!")
                        print(f"\nCantidad de respuestas acertadas de {jugador.nombre}: {jugador.cantRespuestasAcertadas}")
                    else:
                        print(f'Incorrecto, la respuesta es: {tarjeta.respuestaCorrecta}')

                print(f"La puntuación de {jugador.nombre} ahora es: {jugador.puntuacion}")
                
                print(f"\nRonda: {ronda}")
                tarjeta = nuevaPartida.generarPregunta()
                print(tarjeta)
                
                print(f"Turno del jugador N°{jugador.id}: {jugador.nombre}")

                if jugador.responder(tarjeta, nuevaPartida):
                    print("\nRespuesta correcta!")
                    print(f"\nCantidad de respuestas acertadas de {jugador.nombre}: {jugador.cantRespuestasAcertadas}")
                else:
                    print(f'Incorrecto, la respuesta es: {tarjeta.respuestaCorrecta}')

                print(f"La puntuación de {jugador.nombre} ahora es: {jugador.puntuacion}") 

    print("\n════════════════════")    
    print('Ha acabado el juego.')
    print("════════════════════")


while True:
    menu()
    opt = input("Ingrese una opción: ")

    if opt == "1":
        nuevaPartida = Partida()
        nuevoJuego()

    elif opt == "2":
        try: 
            ranking =  nuevaPartida.mostrarRanking(nuevaPartida)
            print("\nRanking\n") 
            for indice, jugador in enumerate(ranking):
                print(f"{indice + 1}. Nombre: {jugador.nombre}, puntuación: {jugador.puntuacion}")  
        except:
            print("\nPrimero debe jugar una partida")

    elif opt == "3":
        print("Gracias por jugar!")
        break

    else:
        print("Ingrese una opción válida")



