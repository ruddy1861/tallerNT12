class Cocteles:
    def __init__(self):
        self.__nombre=None
        self.__precio=None
        self.__gradosAlcohol=None
        self.__tipoCoctel=None
        self.__cantidad=None
        self.__añejamiento=None

    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato
        
    @property 
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, dato):
        self.__precio = dato
    
    @property 
    def gradosAlcohol(self):
        return self.__gradosAlcohol
    
    @gradosAlcohol.setter
    def gradosAlcohol(self, dato):
        self.__gradosAlcohol = dato

    @property 
    def tipoCoctel(self):
        return self.__tipoCoctel
    
    @tipoCoctel.setter
    def tipoCoctel(self, dato):
        self.__tipoCoctel = dato
        
    @property 
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, dato):
        self.__cantidad = dato

    @property 
    def añejamiento(self):
        return self.__añejamiento
    
    @añejamiento.setter
    def añejamiento(self, dato):
        self.__añejamiento = dato
    