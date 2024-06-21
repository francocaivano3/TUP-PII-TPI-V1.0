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





# Ciencia:
# ¿Cuál es la unidad básica de la vida?
# A) Célula
# B) Átomo
# C) Molécula
# D) Protón

# ¿Qué fenómeno es responsable de las estaciones del año?
# A) Inclinación del eje terrestre
# B) Distancia al Sol
# C) Rotación de la Tierra
# D) Efecto invernadero

# ¿Cuál es el planeta más grande del Sistema Solar?
# A) Júpiter
# B) Saturno
# C) Neptuno
# D) Urano

# ¿Qué tipo de energía es generada por el sol?
# A) Energía solar
# B) Energía eólica
# C) Energía nuclear
# D) Energía hidráulica

# Deporte:
# ¿En qué deporte se utiliza una raqueta?
# A) Tenis
# B) Baloncesto
# C) Fútbol
# D) Golf

# ¿Qué equipo de fútbol ganó la Copa Mundial de la FIFA en 2018?
# A) Francia
# B) Brasil
# C) Alemania
# D) Argentina

# ¿Cuál de estas competiciones no pertenece al mundo del atletismo?
# A) Copa del Mundo de la FIFA
# B) Maratón
# C) Salto de altura
# D) Lanzamiento de jabalina

# ¿Qué deporte se juega en el Super Bowl?
# A) Fútbol americano
# B) Béisbol
# C) Baloncesto
# D) Hockey sobre hielo

# Geografía:
# ¿Cuál es el río más largo del mundo?
# A) Amazonas
# B) Nilo
# C) Yangtsé
# D) Misisipi

# ¿Cuál es la capital de España?
# A) Madrid
# B) Barcelona
# C) Lisboa
# D) Roma

# ¿En qué país se encuentra la Torre Eiffel?
# A) Francia
# B) Italia
# C) Reino Unido
# D) Alemania

# ¿Cuál es el desierto más grande del mundo?
# A) Sahara
# B) Gobi
# C) Kalahari
# D) Atacama

# Programación:
# ¿Cuál de los siguientes no es un lenguaje de programación?
# A) Photoshop
# B) Python
# C) Java
# D) C++

# ¿Qué significa HTML en programación web?
# A) Hyper Text Markup Language
# B) High Tech Modular Language
# C) Home Tool Management Language
# D) Hyperlinks and Text Markup Language

# ¿Cuál es el símbolo utilizado para comentarios de una sola línea en Python?
# A) #
# B) //
# C) --
# D) %

# ¿Qué es JSON en el contexto de la programación?
# A) JavaScript Object Notation
# B) Java Script Online Notation
# C) JavaScript Object Navigation
# D) Java Syntax Object Naming

# Cine:
# ¿Quién interpretó a Harry Potter en las películas de Harry Potter?
# A) Daniel Radcliffe
# B) Rupert Grint
# C) Emma Watson
# D) Tom Felton

# ¿Cuál de estas películas fue dirigida por Steven Spielberg?
# A) E.T. el extraterrestre
# B) El Padrino
# C) Titanic
# D) El Señor de los Anillos

# ¿Quién ganó el Premio de la Academia al Mejor Actor en 2020?
# A) Joaquin Phoenix
# B) Brad Pitt
# C) Leonardo DiCaprio
# D) Anthony Hopkins

# ¿Qué película ganó el Premio de la Academia a la Mejor Película en 2021?
# A) Nomadland
# B) Parasite
# C) The Shape of Water
# D) Green Book

# Continuación de las preguntas...
# ¿Cuál es la capital de Argentina?
# A) Buenos Aires
# B) Santiago
# C) Montevideo
# D) Asunción

# ¿En qué país se encuentra el Taj Mahal?
# A) India
# B) China
# C) Japón
# D) Tailandia

# ¿Cuál es la capital de Francia?
# A) París
# B) Londres
# C) Berlín
# D) Madrid

# ¿Qué es un bucle while en programación?
# A) Una estructura de control repetitiva
# B) Una función de impresión
# C) Un tipo de variable
# D) Un operador lógico

# ¿Quién fue el primer astronauta en caminar sobre la luna?
# A) Neil Armstrong
# B) Buzz Aldrin
# C) Yuri Gagarin
# D) Alan Shepard

# ¿Cuál es la capital de Italia?
# A) Roma
# B) Milán
# C) Nápoles
# D) Venecia

# ¿Qué es una función en programación?
# A) Un conjunto de instrucciones que realizan una tarea específica
# B) Una variable de tipo numérico
# C) Un tipo de dato
# D) Una declaración de importación

# ¿Quién es el director de la película "El Padrino"?
# A) Francis Ford Coppola
# B) Steven Spielberg
# C) Martin Scorsese
# D) Quentin Tarantino

# ¿Cuál es la capital de Alemania?
# A) Berlín
# B) Múnich
# C) Hamburgo
# D) Frankfurt

# ¿Qué es CSS en programación web?
# A) Cascading Style Sheets
# B) Creative Style Sheets
# C) Computer Style Sheets
# D) Colorful Style Sheets

# ¿Cuál es la capital de Canadá?
# A) Ottawa
# B) Toronto
# C) Vancouver
# D) Montreal

# ¿Qué significa la sigla SQL en programación?
# A) Structured Query Language
# B) Simple Query Language
# C) System Query Language
# D) Server Query Language

# ¿Cuál es la capital de Australia?
# A) Canberra
# B) Sídney
# C) Melbourne
# D) Brisbane

# ¿Qué actor interpretó a Iron Man en las películas de Marvel?
# A) Robert Downey Jr.
# B) Chris Evans
# C) Chris Hemsworth
# D) Mark Ruffalo

# ¿Cuál de estos no es un planeta del Sistema Solar?
# A) Plutón
# B) Marte
# C) Júpiter
# D) Orión

# ¿Quién escribió la novela "Cien años de soledad"?
# A) Gabriel García Márquez
# B) Julio Cortázar
# C) Mario Vargas Llosa
# D) Pablo Neruda