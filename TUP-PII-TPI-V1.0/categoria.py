class Categoria:
    def __init__(self, color:str, nombre:str, valor:int) -> None:

        self.__color = color
        self.__nombre = nombre
        self.__valor = valor

    @property
    def color(self):
        return self.__color
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def valor(self):
        return self.__valor
    

    def __str__(self):
        return self.__nombre