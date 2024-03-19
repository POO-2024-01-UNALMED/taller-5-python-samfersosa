from zooAnimales.animal import Animal
class Pez(Animal):
    salmones=0
    bacalaos=0
    _listado=[]
    def __init__(self, nombre, edad, habitat, genero, colorEscamas,cantidadAletas):
        super(). __init__(nombre, edad, habitat, genero)
        self._cantidadAletas = cantidadAletas
        self._colorEscamas= colorEscamas
        Pez._listado.append(self)
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls,nombre, edad, genero):
        cls.salmones+=1
        animalito=Pez(nombre, edad, "oceano" , genero, "rojo",6)
        return animalito
    @classmethod  
    def crearBacalao(cls,nombre, edad, genero):
        cls.bacalaos+=1
        animalito=Pez(nombre, edad, "oceano" , genero, "gris",6)
        return animalito
    
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,color):
        self._colorEscamas=color
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self,valor):
        self._cantidadAletas=valor
    
    @classmethod
    def setListado(cls,lista):
        cls._listado=lista
    def getListado(cls):
        return cls._listado