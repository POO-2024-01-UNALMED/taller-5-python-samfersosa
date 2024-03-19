from zooAnimales.animal import Animal
class Reptil(Animal):
    iguanas=0
    serpientes=0
    _listado=[]
    def __init__(self, nombre, edad, habitat, genero, colorEscamas,largoCola):
        super(). __init__(nombre, edad, habitat, genero)
        self._largoCola = largoCola
        self._colorEscamas= colorEscamas
        Reptil._listado.append(self)
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "reptar"
    
    @classmethod
    def crearIguana(cls,nombre, edad, genero):
        cls.iguanas+=1
        animalito=Reptil(nombre, edad, "humedal" , genero, "verde",3)
        return animalito
    @classmethod    
    def crearSerpiente(cls,nombre, edad, genero):
        cls.serpientes+=1
        animalito= Reptil(nombre, edad, "jungla" , genero, "blanco",1)
        return animalito
    
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,color):
        self._colorEscamas=color
    
    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self,valor):
        self._largoCola=valor
    
    @classmethod
    def setListado(cls,lista):
        cls._listado=lista
    def getListado(cls):
        return cls._listado