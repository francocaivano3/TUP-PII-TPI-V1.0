from jugador import Jugador
from tarjeta import Tarjeta
import random

class Partida():
    def __init__(self):
        self.__jugadores: list = [] 
        self.__ranking: list = []
        self.__mazo: list = []
        self.__tarjetasUtilizadas: list = []
        

    @property
    def ranking(self):
        return self.__ranking

    @property
    def mazo(self):
        return self.__mazo
    
    @property
    def tarjetasUtilizadas(self):
        return self.__tarjetasUtilizadas
    
    @property
    def listaJugadores(self):
        return self.__jugadores

    def ingresarJugadores(self, jugador: Jugador):
        self.__jugadores.append(jugador)

  
    def generarPregunta(self):
        if len(self.mazo) > 0:
            tarjetaSacada = random.choice(self.mazo)
            self.mazo.remove(tarjetaSacada)
            return tarjetaSacada
        else:
            return 0
        
        
    def modificarPuntuacion(self, jugador:Jugador, tarjeta:Tarjeta):
        valorTarjeta = tarjeta.categoria.valor
        return jugador.puntuacion + valorTarjeta
    
    
    def mostrarRanking(self, partida):
        ranking = sorted(partida.listaJugadores, key=lambda x: x.puntuacion, reverse=True)
        return ranking  
        

