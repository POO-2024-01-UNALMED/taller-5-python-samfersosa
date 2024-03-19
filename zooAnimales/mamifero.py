from zooAnimales.animal import Animal
class Mamifero(Animal):
    caballos=0
    leones=0
    _listado=[]
    def __init__(self,nombre=None,edad=None, habitat=None,genero=None,pelaje=None, patas=None):
        super(). __init__(self,nombre,edad, habitat,genero,)
        self._pelaje=pelaje
        self._patas= patas
        Mamifero._listado.append(self)
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
        
    @classmethod
    def crearCaballo(cls,nombre,edad,genero,):
        cls.caballos+=1
        return Mamifero(nombre,edad,"selva",genero,True,4)
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones=+1
        animalito=Mamifero(nombre,edad,"selva",genero,True,4)
        return animalito
    
    @classmethod
    def  getListado(cls):
        return cls.listado
    @classmethod
    def setListado(cls,listado):
        cls._listado = listado
    def isPelaje(self):
        return self._pelaje
    def setPelaje(self,pelaje):
        self._pelaje = pelaje
    def getPatas(self):
        return self._patas
    def setPatas(self,patas):
        self._patas = patas