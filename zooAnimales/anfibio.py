from zooAnimales.animal import Animal
class Anfibio(Animal):
    ranas=0
    salamandras=0
    _listado=[]
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPiel=None, venenoso=None):
        super(). __init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso= venenoso
        Anfibio._listado.append(self)
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "saltar"
    @classmethod
    def crearRana(cls,nombre, edad, genero):
        cls.ranas+=1
        animalito= Anfibio(nombre, edad, "selva" , genero, "rojo",True)
        return animalito
    @classmethod   
    def crearSalamandra(cls,nombre, edad, genero):
        cls.salamandras+=1
        animalito=Anfibio(nombre, edad, "selva" , genero, "negro y amarillo",False)
        return animalito
    
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self,color):
        self._colorPiel=color
    
    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self,valor):
        self._venenoso=valor
    
    @classmethod
    def setListado(cls,lista):
        cls._listado=lista
    def getListado(cls):
        return cls._listado