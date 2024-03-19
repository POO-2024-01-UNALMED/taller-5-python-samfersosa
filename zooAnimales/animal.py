import zooAnimales

class Animal:
    totalAnimales=0
    def __init__(self,nombre=None, edad=None,habitat=None,genero=None,zona=None):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=zona
        Animal.totalAnimales +=1

    def movimiento(self):
        return "desplazarce"
    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos : "+str(zooAnimales.mamifero.Mamifero.cantidadMamiferos())+"\n"+"Aves : "+str(zooAnimales.ave.Ave.cantidadAves())+"\n"+"Reptiles : "+str(zooAnimales.reptil.Reptil.cantidadReptiles())+"\n"+"Peces : "+str(zooAnimales.pez.Pez.cantidadPeces())+"\n"+"Anfibios : "+str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())
    def toString(self):
       if self._zona!=None:
            return "Mi nombre es "+str(self._nombre)+", tengo una edad de "+str(self._edad)+", habito en "+str(self._habitat)+" y mi genero es "+str(self._genero)+", la zona en la que me ubico es "+str(self._zonas.getNombre())+", en el "+str(self._zonas.getZoo())
       else:
           return "Mi nombre es "+str(self._nombre)+", tengo una edad de "+str(self._edad)+", habito en "+str(self._habitat)+" y mi genero es "+str(self._genero)
    

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    
    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    
    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    
    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    
    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona