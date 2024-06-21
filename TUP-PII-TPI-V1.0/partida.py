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
        tarjetaSacada = random.choice(self.mazo)
        self.mazo.remove(tarjetaSacada)
        print(tarjetaSacada)
        return tarjetaSacada
        
        
    def modificarPuntuacion(self, jugador:Jugador, tarjeta:Tarjeta):
        valorTarjeta = tarjeta.categoria.valor
        return jugador.puntuacion + valorTarjeta
    
    
    def mostrarRanking(self, partida):
        ranking = sorted(partida.listaJugadores, key=lambda x: x.puntuacion, reverse=True)
        print("Ranking:")
        for indice, jugador in enumerate(ranking):
            print(f"{indice + 1}. Nombre: {jugador.nombre}, puntuación: {jugador.puntuacion}")

