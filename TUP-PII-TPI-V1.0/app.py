from partida import Partida
from jugador import Jugador 
from datos import * 
from colorama import init, Fore, Back, Style

def agregarMazo(nuevaPartida:Partida, listaPreguntas:list):
        for pregunta in listaPreguntas:
            nuevaPartida.mazo.append(pregunta)

print("\nBienvenidos/as.")

def menu():
    print("\n1- Iniciar nuevo juego.\n2- Mostrar puntuaciones\n3- Finalizar")
    

def nuevoJuego():
    agregarMazo(nuevaPartida, listaPreguntas)
    

    for i in range(1, 5):
        print("\n")
        jugador = Jugador(input(f"Ingrese el nombre del jugador {i}: "))
        nuevaPartida.ingresarJugadores(jugador)
        print(f"Se ha añadido el jugador número {i}: {jugador.nombre}")


    while len(nuevaPartida.mazo) > 0:
        
        for jugador in nuevaPartida.listaJugadores:
            
            if jugador.turno == True and len(nuevaPartida.mazo) > 0:
                
                if jugador.cantRespuestasAcertadas == 3: 
                    print("\n════════════════════════════════════════════════════════")
                    print(f"El jugador {jugador.nombre} tiene el beneficio del turno extra!")
                    print("════════════════════════════════════════════════════════")
                    tarjeta = nuevaPartida.generarPregunta()
                    print(f"Turno del jugador N°{jugador.id}: {jugador.nombre}")
                    jugador.responder(tarjeta, nuevaPartida)
                
                tarjeta = nuevaPartida.generarPregunta()
                print(f"Turno del jugador N°{jugador.id}: {jugador.nombre}")
                jugador.responder(tarjeta, nuevaPartida)

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
             nuevaPartida.mostrarRanking(nuevaPartida)   
        except:
            print("\nPrimero debe jugar una partida")

    elif opt == "3":
        print("Gracias por jugar!")
        break

    else:
        print("Ingrese una opción válida")



