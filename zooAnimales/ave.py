from zooAnimales.animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = []
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas=None):
        super(). __init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    
    def movimiento(self):
        return "volar"
    
    @classmethod
    def crearHalcon(cls,nombre, edad, genero):
        cls.halcones+=1
        animalito=Ave(nombre, edad, "montanas" , genero, "cafe glorioso")
        return animalito
    @classmethod
    def crearAguila(cls,nombre, edad, genero):
        cls.aguilas+=1
        animalito=Ave(nombre, edad, "montanas" , genero, "blanco y amarillo")
        return animalito

    
    @classmethod
    def  getListado(cls):
        return cls.listado
    @classmethod
    def setListado(cls,listado):
        cls._listado = listado
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self,color):
        self._colorPlumas=color