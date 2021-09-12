from datetime import date
class Empresa:
    def __init__(self,nom="El mejor",ruc="09156",tel="0939375202",dir="Calle Colon"):
        self.nombre = nom
        self.ruc = ruc
        self.telefono = tel
        self.direccion= dir

    def mostrarEmpresa(self):
        print("Empresa: {:20}  Ruc: {}".format(self.nombre,self.ruc))

class Cliente:
    def __init__(self,nom,ced,tel):
        self.nombre = nom
        self.cedula = ced
        self.telefono = tel

    def mostrarCliente(self):
        print(self.nombre,self.cedula,self.telefono)


class ClienteCorporativo(Cliente):
    def __init__(self,nom,ced,tel,contrato):
        super().__init__(nom, ced, tel)
        self.__contrato = contrato

    @property
    def contrato(self): #!getter: obtener el valor del atributo privado 
        return self.__contrato
    @contrato.setter
    def contrato(self,value): #!setter: asigna ub valor al atributo privado
        if value:
            self.__contrato = value
        else:
            self.__contrato = "Sin Contrato"

    def mostrarCliente(self):
        print(self.nombre,self.__contrato)


class ClientePersonal(Cliente):
    def __init__(self,nom,ced,tel,promocion=True):
        super().__init__(nom, ced, tel)
        self.__promocion=promocion

    @property
    def promocion(self): #!getter: obtener el valor del atributo privado
        if self.__promocion == True:
            return "10% de descuento"
        else:
            return "No hay Promocion"

    def mostrarCliente(self):
        print("Cliente: {:13}Cédula: {}".format(self.nombre,self.cedula))


class Articulo:
    secuencia=0
    iva=0.12
    def __init__(self,des,pre,stock):
        Articulo.secuencia += 1
        self.codigo = Articulo.secuencia
        self.descripcion = des
        self.precio = pre
        self.stock = stock

    def mostrarArticulo(self):
        print(self.codigo,self.descripcion)
    

class DetalleVenta:
    linea=0
    def __init__(self,articulo,cantidad):
        DetalleVenta.linea += 1
        self.lineaDetalle= DetalleVenta.linea
        self.articulo = articulo
        self.precio = articulo.precio
        self.cantidad= cantidad


class CabVenta:
    def __init__(self,fac,fecha,cliente,tot=0):
        self.factura=fac
        self.fecha=fecha
        self.cliente=cliente
        self.total=tot
        self.detalleVen=[]

    def agregarDetalle(self,articulo,cantidad):
        detalle= DetalleVenta(articulo,cantidad)
        self.total += detalle.precio * detalle.cantidad
        self.detalleVen.append(detalle)

    def mostrarVenta(self,empNombre,empRuc):
        print("Empresa: {:17} Ruc: {}".format(empNombre,empRuc))
        print("Factura# {:13} Fecha: {}".format(self.factura,self.fecha))
        self.cliente.mostrarCliente()
        print("Linea Articulo      Precio Cantidad Subtotal")
        for det in self.detalleVen:
            print("{:5} {:15} {} {:6} {:7}".format(det.linea,det.articulo.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))
        print("Total Venta: {:26}".format(self.total))


empresa= Empresa()

cli=ClientePersonal("Ronny","0982949404","09895684684",True)

art1= Articulo("Aceite",3,100)
art2= Articulo("Coca Cola",2,100)

today=date.today()
fecha=date(2021,8,15)

venta=CabVenta("F0001",date.today(),cli)
venta.agregarDetalle(art1,3)
venta.agregarDetalle(art2,2)
venta.mostrarVenta(empresa.nombre,empresa.ruc)




