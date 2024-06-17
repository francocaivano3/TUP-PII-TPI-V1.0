class Opcion:
    def __init__(self, opcion:str, correcta:bool) -> None:
        self.__opcion = opcion
        self.__correcta = None #agregar al UML

    @property
    def opcion(self):
        return self.__opcion
    
    @opcion.setter
    def opcion (self, newOpcion):
        self.opcion = newOpcion

    @property
    def correcta(self):
        return self.__correcta

    @correcta.setter
    def correcta(self, valor:bool):
        self.__correcta = valor

    def __str__(self):
        return f'{self.__opcion}'