from categoria import Categoria
from opcion import Opcion
import random


class Tarjeta():
    __numTarjeta = 0

    def __init__(self, pregunta:str, categoria:Categoria):
        self.__pregunta:str = pregunta
        self.__opciones: list = []
        self.__numTarjeta = Tarjeta.addNumTarjeta()
        self.__respuestaCorrecta = None
        self.__categoria = categoria


    @property
    def numTarjeta(self):
        return self.__numTarjeta

    @classmethod
    def addNumTarjeta(cls):
        cls.__numTarjeta += 1
        return cls.__numTarjeta

    @property
    def respuestaCorrecta(self):
        return self.__respuestaCorrecta
    
    @respuestaCorrecta.setter
    def respuestaCorrecta(self, valor:Opcion):
        self.__respuestaCorrecta = valor

    @property
    def categoria(self):
        return self.__categoria

    @property
    def pregunta(self):
        return self.__pregunta
    
    @property
    def opciones(self):
        return self.__opciones

    # @property
    # def respuestaCorrecta(self):
    #     return self.__respuestaCorrecta

    def agregarOpcion(self, opcion:Opcion):

        self.__opciones.append([opcion.opcion, opcion.correcta])

        # if opcion.correcta:
        #     self.__respuestaCorrecta = opcion

  


    def __str__(self):

        random.shuffle(self.opciones)
        print(self.opciones)

        opcionesStr = '\n'.join(f'Opción {i+1}: {opcion[0]}' for i, opcion in enumerate(self.__opciones))
        return f'Tarjeta número: {self.numTarjeta}\nCategoría: {self.categoria}\n{self.pregunta}\nOpciones:\n{opcionesStr}\n'


        # random.shuffle(self.__opciones)
        # print(f'{self.__pregunta}\nOpciones:\n')
        
        # for i, opcion in enumerate(self.__opciones):
        #     print(f'Opción {i+1}: {opcion}\n')
        


# pregunta = Tarjeta("¿Cuál es el país más grande del mundo en territorio?", Categoria("Azul", "Geografía", 2))
# opcion1 = Opcion('Rusia', True)
# pregunta.agregarOpcion(opcion1)
# opcion2 = Opcion('Brasil', False)
# pregunta.agregarOpcion(opcion2)
# opcion3 = Opcion('EE.UU', False)
# pregunta.agregarOpcion(opcion3)
# opcion4 = Opcion('Canadá', False)
# pregunta.agregarOpcion(opcion4)

# print(pregunta)

