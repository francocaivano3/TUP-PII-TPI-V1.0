from jugador import Jugador
from tarjeta import Tarjeta
import random

class Partida():
    def __init__(self):
        self.__jugadores: list = [] 
        self.__ranking: list = []
        self.__mazo: list = ["a"]
        self.__tarjetasUtilizadas: list = []
        

    @property
    def ranking(self):
        return self.__ranking

    @property
    def mazo(self):
        self.__mazo
    
    @property
    def tarjetasUtilizadas(self):
        return self.__tarjetasUtilizadas
    
    @property 
    def listaJugadores(self):
        return self.__jugadores
  

    @listaJugadores.setter
    def ingresarJugadores(self, jugador: Jugador):
        self.__jugadores.append = jugador.nombre
        print(self.jugadores)

  
    
    def generarPregunta(self):
        tarjetaSacada = random.choice(self.mazo)
        self.mazo.remove(tarjetaSacada)
        print(tarjetaSacada)
        return tarjetaSacada

    def modificarPuntuacion(self, jugador:Jugador, tarjeta:Tarjeta):
        jugador.puntuacion += tarjeta.categoria.valor
       
    

