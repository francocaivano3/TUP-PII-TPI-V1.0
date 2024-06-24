from categoria import Categoria 
from jugador import Jugador
from opcion import Opcion
from partida import Partida
from tarjeta import Tarjeta


#Pregunta 1
pregunta1 = Tarjeta("¿Cuál es el país más grande del mundo en territorio?", Categoria("BLUE", "Geografía", 4))
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
pregunta2 = Tarjeta("¿Cuántas provincias tiene Argentina?", Categoria("BLUE", "Geografía", 4))
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
pregunta3 = Tarjeta("¿Cuántos elementos hay en la tabla periódica?", Categoria("GREEN", "Ciencia", 2))
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
pregunta4 = Tarjeta("¿Cuál de las opciones es notación científica?", Categoria("GREEN", "Ciencia", 2))
opcion1 = Opcion('2 x 10²', True)
pregunta4.agregarOpcion(opcion1)
pregunta4.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion('2³', False)
pregunta4.agregarOpcion(opcion2)
opcion3 = Opcion('2 x 10', False)
pregunta4.agregarOpcion(opcion3)
opcion4 = Opcion('2 x 3', False)
pregunta4.agregarOpcion(opcion4)

#Pregunta 5

pregunta5 = Tarjeta("¿Cuál es la unidad básica de la vida?", Categoria("GREEN", "Ciencia", 2))
opcion1 = Opcion("Célula", True)
pregunta5.agregarOpcion(opcion1)
pregunta5.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Átomo", False)
pregunta5.agregarOpcion(opcion2)
opcion3 = Opcion("Molécula", False)
pregunta5.agregarOpcion(opcion3)
opcion4 = Opcion("Protón", False)
pregunta5.agregarOpcion(opcion4)


pregunta6 = Tarjeta("¿Qué fenómeno es responsable de las estaciones del año?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("Inclinación del eje terrestre", True)
pregunta6.agregarOpcion(opcion1)
pregunta6.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Distancia al Sol", False)
pregunta6.agregarOpcion(opcion2)
opcion3 = Opcion("Rotación de la Tierra", False)
pregunta6.agregarOpcion(opcion3)
opcion4 = Opcion("Efecto invernadero", False)
pregunta6.agregarOpcion(opcion4)

pregunta7 = Tarjeta("¿Cuál es el planeta más grande del Sistema Solar?", Categoria("GREEN", "Ciencia", 2))
opcion1 = Opcion("Júpiter", True)
pregunta7.agregarOpcion(opcion1)
pregunta7.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Saturno", False)
pregunta7.agregarOpcion(opcion2)
opcion3 = Opcion("Neptuno", False)
pregunta7.agregarOpcion(opcion3)
opcion4 = Opcion("Urano", False)
pregunta7.agregarOpcion(opcion4)

pregunta8 = Tarjeta("¿Qué tipo de energía es generada por el sol?", Categoria("GREEN", "Ciencia", 2))
opcion1 = Opcion("Energía solar", True)
pregunta8.agregarOpcion(opcion1)
pregunta8.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Energía eólica", False)
pregunta8.agregarOpcion(opcion2)
opcion3 = Opcion("Energía nuclear", False)
pregunta8.agregarOpcion(opcion3)
opcion4 = Opcion("Energía hidráulica", False)
pregunta8.agregarOpcion(opcion4)

# Deporte:
pregunta9 = Tarjeta("¿En qué deporte se utiliza una raqueta?", Categoria("ORANGE", "Deporte", 3))
opcion1 = Opcion("Tenis", True)
pregunta9.agregarOpcion(opcion1)
pregunta9.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Baloncesto", False)
pregunta9.agregarOpcion(opcion2)
opcion3 = Opcion("Fútbol", False)
pregunta9.agregarOpcion(opcion3)
opcion4 = Opcion("Golf", False)
pregunta9.agregarOpcion(opcion4)

pregunta10 = Tarjeta("¿Qué equipo de fútbol ganó la Copa Mundial de la FIFA en 2018?", Categoria("ORANGE", "Deporte", 3))
opcion1 = Opcion("Francia", True)
pregunta10.agregarOpcion(opcion1)
pregunta10.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Brasil", False)
pregunta10.agregarOpcion(opcion2)
opcion3 = Opcion("Alemania", False)
pregunta10.agregarOpcion(opcion3)
opcion4 = Opcion("Argentina", False)
pregunta10.agregarOpcion(opcion4)

pregunta11 = Tarjeta("¿Cuál de estas competiciones no pertenece al mundo del atletismo?", Categoria("ORANGE", "Deporte", 3))
opcion1 = Opcion("Copa del Mundo de la FIFA", True)
pregunta11.agregarOpcion(opcion1)
pregunta11.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Maratón", False)
pregunta11.agregarOpcion(opcion2)
opcion3 = Opcion("Salto de altura", False)
pregunta11.agregarOpcion(opcion3)
opcion4 = Opcion("Lanzamiento de jabalina", False)
pregunta11.agregarOpcion(opcion4)

pregunta12 = Tarjeta("¿Qué deporte se juega en el Super Bowl?", Categoria("ORANGE", "Deporte", 3))
opcion1 = Opcion("Fútbol americano", True)
pregunta12.agregarOpcion(opcion1)
pregunta12.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Béisbol", False)
pregunta12.agregarOpcion(opcion2)
opcion3 = Opcion("Baloncesto", False)
pregunta12.agregarOpcion(opcion3)
opcion4 = Opcion("Hockey sobre hielo", False)
pregunta12.agregarOpcion(opcion4)
# Geografí4:
pregunta13 = Tarjeta("¿Cuál es el río más largo del mundo?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("Amazonas", True)
pregunta13.agregarOpcion(opcion1)
pregunta13.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Nilo", False)
pregunta13.agregarOpcion(opcion2)
opcion3 = Opcion("Yangtsé", False)
pregunta13.agregarOpcion(opcion3)
opcion4 = Opcion("Misisipi", False)
pregunta13.agregarOpcion(opcion4)

pregunta14 = Tarjeta("¿Cuál es la capital de España?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("Madrid", True)
pregunta14.agregarOpcion(opcion1)
pregunta14.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Barcelona", False)
pregunta14.agregarOpcion(opcion2)
opcion3 = Opcion("Lisboa", False)
pregunta14.agregarOpcion(opcion3)
opcion4 = Opcion("Roma", False)
pregunta14.agregarOpcion(opcion4)

pregunta15 = Tarjeta("¿En qué país se encuentra la Torre Eiffel?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("Francia", True)
pregunta15.agregarOpcion(opcion1)
pregunta15.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Italia", False)
pregunta15.agregarOpcion(opcion2)
opcion3 = Opcion("Reino Unido", False)
pregunta15.agregarOpcion(opcion3)
opcion4 = Opcion("Alemania", False)
pregunta15.agregarOpcion(opcion4)

pregunta16 = Tarjeta("¿Cuál es el desierto más grande del mundo?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("Sahara", True)
pregunta16.agregarOpcion(opcion1)
pregunta16.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Gobi", False)
pregunta16.agregarOpcion(opcion2)
opcion3 = Opcion("Kalahari", False)
pregunta16.agregarOpcion(opcion3)
opcion4 = Opcion("Atacama", False)
pregunta16.agregarOpcion(opcion4)

# Programación:
pregunta17 = Tarjeta("¿Cuál de los siguientes no es un lenguaje de programación?", Categoria("YELLOW", "Programación", 5))
opcion1 = Opcion("Photoshop", True)
pregunta17.agregarOpcion(opcion1)
pregunta17.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Python", False)
pregunta17.agregarOpcion(opcion2)
opcion3 = Opcion("Java", False)
pregunta17.agregarOpcion(opcion3)
opcion4 = Opcion("C++", False)
pregunta17.agregarOpcion(opcion4)

pregunta18 = Tarjeta("¿Qué significa HTML en programación web?", Categoria("YELLOW", "Programación", 5))
opcion1 = Opcion("Hyper Text Markup Language", True)
pregunta18.agregarOpcion(opcion1)
pregunta18.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("High Tech Modular Language", False)
pregunta18.agregarOpcion(opcion2)
opcion3 = Opcion("Home Tool Management Language", False)
pregunta18.agregarOpcion(opcion3)
opcion4 = Opcion("Hyperlinks and Text Markup Language", False)
pregunta18.agregarOpcion(opcion4)

pregunta19 = Tarjeta("¿Cuál es el símbolo utilizado para comentarios de una sola línea en Python?", Categoria("YELLOW", "Programación", 5))
opcion1 = Opcion("#", True)
pregunta19.agregarOpcion(opcion1)
pregunta19.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("//", False)
pregunta19.agregarOpcion(opcion2)
opcion3 = Opcion("--", False)
pregunta19.agregarOpcion(opcion3)
opcion4 = Opcion("%", False)
pregunta19.agregarOpcion(opcion4)

pregunta20 = Tarjeta("¿Qué es JSON en el contexto de la programación?", Categoria("YELLOW", "Programación", 5))
opcion1 = Opcion("JavaScript Object Notation", True)
pregunta20.agregarOpcion(opcion1)
pregunta20.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Java Script Online Notation", False)
pregunta20.agregarOpcion(opcion2)
opcion3 = Opcion("JavaScript Object Navigation", False)
pregunta20.agregarOpcion(opcion3)
opcion4 = Opcion("Java Syntax Object Naming", False)
pregunta20.agregarOpcion(opcion4)

# Cine:
pregunta21 = Tarjeta("¿Quién interpretó a Harry Potter en las películas de Harry Potter?", Categoria("MAGENTA", "Cine", 2))
opcion1 = Opcion("Daniel Radcliffe", True)
pregunta21.agregarOpcion(opcion1)
pregunta21.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Rupert Grint", False)
pregunta21.agregarOpcion(opcion2)
opcion3 = Opcion("Emma Watson", False)
pregunta21.agregarOpcion(opcion3)
opcion4 = Opcion("Tom Felton", False)
pregunta21.agregarOpcion(opcion4)

pregunta22 = Tarjeta("¿Cuál de estas películas fue dirigida por Steven Spielberg?", Categoria("MAGENTA", "Cine", 2))
opcion1 = Opcion("E.T. el extraterrestre", True)
pregunta22.agregarOpcion(opcion1)
pregunta22.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("El Padrino", False)
pregunta22.agregarOpcion(opcion2)
opcion3 = Opcion("Titanic", False)
pregunta22.agregarOpcion(opcion3)
opcion4 = Opcion("El Señor de los Anillos", False)
pregunta22.agregarOpcion(opcion4)

pregunta23 = Tarjeta("¿Quién ganó el Premio de la Academia al Mejor Actor en 2020?", Categoria("MAGENTA", "Cine", 2))
opcion1 = Opcion("Joaquin Phoenix", True)
pregunta23.agregarOpcion(opcion1)
pregunta23.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Brad Pitt", False)
pregunta23.agregarOpcion(opcion2)
opcion3 = Opcion("Leonardo DiCaprio", False)
pregunta23.agregarOpcion(opcion3)
opcion4 = Opcion("Anthony Hopkins", False)
pregunta23.agregarOpcion(opcion4)

pregunta24 = Tarjeta("¿Qué película ganó el Premio de la Academia a la Mejor Película en 2021?", Categoria("MAGENTA", "Cine", 2))
opcion1 = Opcion("Nomadland", True)
pregunta24.agregarOpcion(opcion1)
pregunta24.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Parasite", False)
pregunta24.agregarOpcion(opcion2)
opcion3 = Opcion("The Shape of Water", False)
pregunta24.agregarOpcion(opcion3)
opcion4 = Opcion("Green Book", False)
pregunta24.agregarOpcion(opcion4)

# Continuación de las preguntas...
pregunta25 = Tarjeta("¿Cuál es la capital de Argentina?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("Buenos Aires", True)
pregunta25.agregarOpcion(opcion1)
pregunta25.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Santiago", False)
pregunta25.agregarOpcion(opcion2)
opcion3 = Opcion("Montevideo", False)
pregunta25.agregarOpcion(opcion3)
opcion4 = Opcion("Asunción", False)
pregunta25.agregarOpcion(opcion4)

pregunta26 = Tarjeta("¿En qué país se encuentra el Taj Mahal?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("India", True)
pregunta26.agregarOpcion(opcion1)
pregunta26.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("China", False)
pregunta26.agregarOpcion(opcion2)
opcion3 = Opcion("Japón", False)
pregunta26.agregarOpcion(opcion3)
opcion4 = Opcion("Tailandia", False)
pregunta26.agregarOpcion(opcion4)

pregunta27 = Tarjeta("¿Cuál es la capital de Francia?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("París", True)
pregunta27.agregarOpcion(opcion1)
pregunta27.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Londres", False)
pregunta27.agregarOpcion(opcion2)
opcion3 = Opcion("Berlín", False)
pregunta27.agregarOpcion(opcion3)
opcion4 = Opcion("Madrid", False)
pregunta27.agregarOpcion(opcion4)

pregunta28 = Tarjeta("¿Qué es un bucle while en programación?", Categoria("YELLOW", "Programación", 5))
opcion1 = Opcion("Una estructura de control repetitiva", True)
pregunta28.agregarOpcion(opcion1)
pregunta28.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Una función de impresión", False)
pregunta28.agregarOpcion(opcion2)
opcion3 = Opcion("Un tipo de variable", False)
pregunta28.agregarOpcion(opcion3)
opcion4 = Opcion("Un operador lógico", False)
pregunta28.agregarOpcion(opcion4)

pregunta29 = Tarjeta("¿Quién fue el primer astronauta en caminar sobre la luna?", Categoria("GREEN", "Ciencia", 2))
opcion1 = Opcion("Neil Armstrong", True)
pregunta29.agregarOpcion(opcion1)
pregunta29.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Buzz Aldrin", False)
pregunta29.agregarOpcion(opcion2)
opcion3 = Opcion("Yuri Gagarin", False)
pregunta29.agregarOpcion(opcion3)
opcion4 = Opcion("Alan Shepard", False)
pregunta29.agregarOpcion(opcion4)

pregunta30 = Tarjeta("¿Cuál es la capital de Italia?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("Roma", True)
pregunta30.agregarOpcion(opcion1)
pregunta30.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Milán", False)
pregunta30.agregarOpcion(opcion2)
opcion3 = Opcion("Nápoles", False)
pregunta30.agregarOpcion(opcion3)
opcion4 = Opcion("Venecia", False)
pregunta30.agregarOpcion(opcion4)

pregunta31 = Tarjeta("¿Qué es una función en programación?", Categoria("YELLOW", "Programación", 5))
opcion1  = Opcion("Un conjunto de instrucciones que realizan una tarea específica", True)
pregunta31.agregarOpcion(opcion1)
pregunta31.respuestaCorrecta = opcion1.opcion
opcion2  = Opcion("Una variable de tipo numérico", False)
pregunta31.agregarOpcion(opcion2)
opcion3  = Opcion("Un tipo de dato", False)
pregunta31.agregarOpcion(opcion3)
opcion4  = Opcion("Una declaración de importación", False)
pregunta31.agregarOpcion(opcion4)

pregunta32 = Tarjeta('¿Quién es el director de la película "El Padrino"?', Categoria("MAGENTA", "Cine", 2))
opcion1 = Opcion("Francis Ford Coppola", True)
pregunta32.agregarOpcion(opcion1)
pregunta32.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Steven Spielberg", False)
pregunta32.agregarOpcion(opcion2)
opcion3 = Opcion("Martin Scorsese", False)
pregunta32.agregarOpcion(opcion3)
opcion4 = Opcion("Quentin Tarantino", False)
pregunta32.agregarOpcion(opcion4)

pregunta33 = Tarjeta("¿Cuál es la capital de Alemania?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("Berlín", True)
pregunta33.agregarOpcion(opcion1)
pregunta33.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Múnich", False)
pregunta33.agregarOpcion(opcion2)
opcion3 = Opcion("Hamburgo", False)
pregunta33.agregarOpcion(opcion3)
opcion4 = Opcion("Frankfurt", False)
pregunta33.agregarOpcion(opcion4)

pregunta34 = Tarjeta("¿Qué es CSS en programación web?", Categoria("YELLOW", "Programación", 5))
opcion1 = Opcion("Cascading Style Sheets", True)
pregunta34.agregarOpcion(opcion1)
pregunta34.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Creative Style Sheets", False)
pregunta34.agregarOpcion(opcion2)
opcion3 = Opcion("Computer Style Sheets", False)
pregunta34.agregarOpcion(opcion3)
opcion4 = Opcion("Colorful Style Sheets", False)
pregunta34.agregarOpcion(opcion4)

pregunta35 = Tarjeta("¿Cuál es la capital de Canadá?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("Ottawa", True)
pregunta35.agregarOpcion(opcion1)
pregunta35.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Toronto", False)
pregunta35.agregarOpcion(opcion2)
opcion3 = Opcion("Vancouver", False)
pregunta35.agregarOpcion(opcion3)
opcion4 = Opcion("Montreal", False)
pregunta35.agregarOpcion(opcion4)

pregunta36 = Tarjeta("¿Qué significa la sigla SQL en programación?", Categoria("YELLOW", "Programación", 5))
opcion1 = Opcion("Structured Query Language", True)
pregunta36.agregarOpcion(opcion1)
pregunta36.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Simple Query Language", False)
pregunta36.agregarOpcion(opcion2)
opcion3 = Opcion("System Query Language", False)
pregunta36.agregarOpcion(opcion3)
opcion4 = Opcion("Server Query Language", False)
pregunta36.agregarOpcion(opcion4)

pregunta37 = Tarjeta("¿Cuál es la capital de Australia?", Categoria("BLUE", "Geografía", 4))
opcion1 = Opcion("Canberra", True)
pregunta37.agregarOpcion(opcion1)
pregunta37.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Sídney", False)
pregunta37.agregarOpcion(opcion2)
opcion3 = Opcion("Melbourne", False)
pregunta37.agregarOpcion(opcion3)
opcion4 = Opcion("Brisbane", False)
pregunta37.agregarOpcion(opcion4)

pregunta38 = Tarjeta("¿Qué actor interpretó a Iron Man en las películas de Marvel?", Categoria("MAGENTA", "Cine", 2))
opcion1 = Opcion("Robert Downey Jr.", True)
pregunta38.agregarOpcion(opcion1)
pregunta38.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Chris Evans", False)
pregunta38.agregarOpcion(opcion2)
opcion3 = Opcion("Chris Hemsworth", False)
pregunta38.agregarOpcion(opcion3)
opcion4 = Opcion("Mark Ruffalo", False)
pregunta38.agregarOpcion(opcion4)

pregunta39 = Tarjeta("¿Cuál de estos no es un planeta del Sistema Solar?", Categoria("GREEN", "Ciencia", 2))
opcion1 = Opcion("Plutón", True)
pregunta39.agregarOpcion(opcion1)
pregunta39.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Marte", False)
pregunta39.agregarOpcion(opcion2)
opcion3 = Opcion("Júpiter", False)
pregunta39.agregarOpcion(opcion3)
opcion4 = Opcion("Orión", False)
pregunta39.agregarOpcion(opcion4)


pregunta40 = Tarjeta("En Python, ¿cuál de las siguientes opciones describe correctamente el comportamiento de los decoradores?", Categoria("YELLOW", "Programación", 5))
opcion1 = Opcion("Los decoradores pueden ser utilizados para modificar la funcionalidad de una función o método sin cambiar su código fuente.", True)
pregunta40.agregarOpcion(opcion1)
pregunta40.respuestaCorrecta = opcion1.opcion
opcion2 = Opcion("Los decoradores solo pueden modificar funciones, no métodos de clase.", False)
pregunta40.agregarOpcion(opcion2)
opcion3 = Opcion("Los decoradores se aplican solo a las funciones definidas dentro de las clases.", False)
pregunta40.agregarOpcion(opcion3)
opcion4 = Opcion("Los decoradores deben ser definidos utilizando la palabra clave decorator antes de su nombre.", False)
pregunta40.agregarOpcion(opcion4)

listaPreguntas = [pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9, pregunta10, pregunta11, pregunta12, pregunta13, pregunta14, pregunta15, pregunta16, pregunta17, pregunta18, pregunta19, pregunta20, pregunta21, pregunta22, pregunta23, pregunta24, pregunta25, pregunta26, pregunta27, pregunta28, pregunta29, pregunta30, pregunta31, pregunta32, pregunta33, pregunta34, pregunta35, pregunta36, pregunta37, pregunta38, pregunta39, pregunta40]
