from tarjeta import Tarjeta

class Jugador:
    __id = 0
    def __init__(self, nombre:str) -> None:
        self.__nombre:str = nombre
        self.__turno:bool = True
        self.__cantRespuestasAcertadas:int = 0
        self.__puntuacion:int = 0
        self.__id:int = Jugador.jugador_id()
        self.__beneficio:bool = True
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def id(self):
        return self.__id
    
    @property 
    def beneficio(self):
        return self.__beneficio

    @beneficio.setter
    def beneficio(self, valor):
        self.__beneficio = valor

    @property
    def turno(self):
        return self.__turno
    
    @property
    def cantRespuestasAcertadas(self):
        return self.__cantRespuestasAcertadas 
    
    @cantRespuestasAcertadas.setter
    def cantRespuestasAcertadas(self, nuevoValor):
        self.__cantRespuestasAcertadas = nuevoValor
    
    @property 
    def puntuacion(self):
        return self.__puntuacion

    @puntuacion.setter
    def puntuacion(self, nuevaPuntuacion):
        self.__puntuacion = nuevaPuntuacion

    @classmethod
    def jugador_id(cls):
        cls.__id += 1
        return cls.__id 
    
    @classmethod
    def validar_id(cls,id):
        if id in cls.__id  :
            raise Exception ("ERROR: id ya existente")


    def sacarTarjeta(self, partida):
        partida.generarPregunta()
        
    def responder(self, tarjeta:Tarjeta, partida):

        respuestaSeleccionada = input('Seleccione la opción correcta: ')
        while respuestaSeleccionada != "1" and respuestaSeleccionada != "2" and respuestaSeleccionada != "3" and respuestaSeleccionada != "4":
            respuestaSeleccionada = input('Seleccione una opción válida: ')
            

        if tarjeta.opciones[int(respuestaSeleccionada)-1][1]:
        
            self.puntuacion = partida.modificarPuntuacion(self, tarjeta)
            self.cantRespuestasAcertadas = self.cantRespuestasAcertadas + 1
            return True
        else:
            return False


    def __str__(self):
        return f'Nombre: {self.nombre}, ID: {self.id}'
    
