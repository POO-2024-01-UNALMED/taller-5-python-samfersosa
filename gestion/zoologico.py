class Zoologico:
    _zonas=[]
    def __init__(self,nombre=None,ubicacion=None):
        self._nombre=nombre
        self._ubicacion=ubicacion
    

    @classmethod    
    def agregarZonas(self,zona):
        self._zonas.append(zona)
        zona.setZoo(self)
    def cantidadTotalAnimales(self):
        Animalitos=0
        for i in self._zonas:
            Animalitos+=i.cantidadAnimales()
        return Animalitos
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre= nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion
    
    def getZona(self):
        return self._zonas
    
    def setZona(self,zonas):
        self._zonas=zonas