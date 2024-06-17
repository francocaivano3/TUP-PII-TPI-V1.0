from categoria import Categoria 
from jugador import Jugador
from opcion import Opcion
from partida import Partida
from tarjeta import Tarjeta

partida1 = Partida

jugador1 = Jugador("Franco")
jugador2 = Jugador("Sebastián")
jugador3 = Jugador("Juan")

partida1.ingresarJugadores(partida1, jugador1.nombre)
partida1.ingresarJugadores(partida1, jugador2.nombre)
partida1.ingresarJugadores(partida1, jugador3.nombre)
print(partida1.listaJugadores)
#Pregunta 1
pregunta1 = Tarjeta("¿Cuál es el país más grande del mundo en territorio?", Categoria("Azul", "Geografía"))
opcion1 = Opcion('Rusia', True)
pregunta1.agregarOpcion(opcion1)
opcion2 = Opcion('Brasil', False)
pregunta1.agregarOpcion(opcion2)
opcion3 = Opcion('EE.UU', False)
pregunta1.agregarOpcion(opcion3)
opcion4 = Opcion('Canadá', False)
pregunta1.agregarOpcion(opcion4)
partida1.mazo.append(pregunta1)
print(partida1.mazo)
#Pregunta 2
pregunta2 = Tarjeta("¿Cuántas provincias tiene Argentina?", Categoria("Azul", "Geografía"))
opcion1 = Opcion('23', True)
pregunta2.agregarOpcion(opcion1)
opcion2 = Opcion('21', False)
pregunta2.agregarOpcion(opcion2)
opcion3 = Opcion('22', False)
pregunta2.agregarOpcion(opcion3)
opcion4 = Opcion('24', False)
pregunta2.agregarOpcion(opcion4)

#Pregunta 3
pregunta3 = Tarjeta("¿Cuántos elementos hay en la tabla periódica?", Categoria("Verde", "Ciencia"))
opcion1 = Opcion('118', True)
pregunta3.agregarOpcion(opcion1)
opcion2 = Opcion('110', False)
pregunta3.agregarOpcion(opcion2)
opcion3 = Opcion('119', False)
pregunta3.agregarOpcion(opcion3)
opcion4 = Opcion('112', False)
pregunta3.agregarOpcion(opcion4)

