from categoria import Categoria 
from jugador import Jugador
from opcion import Opcion
from partida import Partida
from tarjeta import Tarjeta

#Pregunta 1
pregunta1 = Tarjeta("¿Cuál es el país más grande del mundo en territorio?", Categoria("Azul", "Geografía", 3))
opcion1 = Opcion('Rusia', True)
pregunta1.agregarOpcion(opcion1)
pregunta1.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion('Brasil', False)
pregunta1.agregarOpcion(opcion2)
opcion3 = Opcion('EE.UU', False)
pregunta1.agregarOpcion(opcion3)
opcion4 = Opcion('Canadá', False)
pregunta1.agregarOpcion(opcion4)


#Pregunta 2
pregunta2 = Tarjeta("¿Cuántas provincias tiene Argentina?", Categoria("Azul", "Geografía", 3))
opcion1 = Opcion('23', True)
pregunta2.agregarOpcion(opcion1)
pregunta2.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion('21', False)
pregunta2.agregarOpcion(opcion2)
opcion3 = Opcion('22', False)
pregunta2.agregarOpcion(opcion3)
opcion4 = Opcion('24', False)
pregunta2.agregarOpcion(opcion4)


#Pregunta 3
pregunta3 = Tarjeta("¿Cuántos elementos hay en la tabla periódica?", Categoria("Verde", "Ciencia", 2))
opcion1 = Opcion('118', True)
pregunta3.agregarOpcion(opcion1)
pregunta3.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion('110', False)
pregunta3.agregarOpcion(opcion2)
opcion3 = Opcion('119', False)
pregunta3.agregarOpcion(opcion3)
opcion4 = Opcion('112', False)
pregunta3.agregarOpcion(opcion4)


#Pregunta 4
pregunta4 = Tarjeta("¿Cuál de las opciones es notación científica?", Categoria("Verde", "Ciencia", 2))
opcion1 = Opcion('2 x 10²', True)
pregunta4.agregarOpcion(opcion1)
pregunta4.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion('2³', False)
pregunta4.agregarOpcion(opcion2)
opcion3 = Opcion('2 x 10', False)
pregunta4.agregarOpcion(opcion3)
opcion4 = Opcion('2 x 3', False)
pregunta4.agregarOpcion(opcion4)


listaPreguntas = [pregunta1, pregunta2, pregunta3, pregunta4]