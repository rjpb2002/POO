class Persona:
    _siguiente=0
    def __init__(self,nombre="Invitado",activo=True):
        self.__codigo = self.siguiente()
        self.__nombre = self.__nombreMayuscula(nombre)
        self.activo = activo

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nom):
        self.__nombre= nom

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,cod):
        self.__codigo= cod

    def siguiente(self):
        Persona._siguiente = Persona._siguiente+1
        return Persona._siguiente

    def __nombreMayuscula(self, nombre=""):
        return nombre.upper()

    def mostrar_datos(self):
        return "Codigo: {} -  Nombre: {}  - Activo: {}".format(self.codigo,self.nombre,self.activo)

per1 = Persona()
print(per1.mostrar_datos())

per2 = Persona("Ronny",False)
print(per2.mostrar_datos())


class Empleado(Persona):
    def __init__(self,nombre="Invitado",activo=True,Sueldo=400):        
        Persona.__init__(self,nombre,activo)
        self.Sueldo = Sueldo

