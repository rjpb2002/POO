from Cargo import Cargo

class Empleado:
    secuencia=0
    def __init__(self,nombre,cedula,sueldo,cargos):
        self.codigo=self.generarCodigo()
        self.nombre=nombre
        self.cedula=cedula
        self.sueldo=sueldo
        self.cargo=cargos
    
    def mostrar(self):
        print("Codigo: {}  Nombre: {}  Cargo: {}-{}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion)) 
    
    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia + 1 
        return Empleado.secuencia

cargo1 = Cargo("Docente")
empleado1= Empleado("Ronny","0928067040",500,cargo1)
empleado1.mostrar()

cargo2 = Cargo("Analista")
empleado2= Empleado("Teffy","0921847925",500,cargo2)
empleado2.mostrar()
