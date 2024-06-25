from categoria import Categoria
from opcion import Opcion
import random
from colorama import init, Fore, Back, Style

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

  
    def colorCategoria(self):
        colores = {
            "BLUE": Fore.BLUE,
            "GREEN": Fore.GREEN,
            "MAGENTA": Fore.MAGENTA,
            "ORANGE": Fore.LIGHTRED_EX,
            "YELLOW": Fore.YELLOW
        }
        
        return colores.get(self.categoria.color, Fore.RESET)

    def __str__(self):
        bordeSuperior = "╔" + "═" * 50 + "╗"
        bordeInferior = "╚" + "═" * 50 + "╝"
        random.shuffle(self.opciones)
        
        opcionesStr = '\n'.join(f'Opción {i+1}: {opcion[0]}' for i, opcion in enumerate(self.__opciones))
        print(self.colorCategoria())
        print(bordeSuperior)
        return f'Tarjeta número: {self.numTarjeta}\n\nCategoría: {self.categoria}\n\n{self.pregunta}\nOpciones:\n\n{opcionesStr}\n{bordeInferior}'
        
     
      

