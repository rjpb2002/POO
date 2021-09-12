from datetime import date

class Empresa:
    def __init__(self,nom="TheBros",ruc="018899529641",dir="Av.Los Paperos",tel="0913358268"):
        self.departamento = []
        self.empleado = []
        self.nombre = nom
        self.direccion = dir 
        self.telefono = tel
        self.ruc = ruc
    
    def mostrarEmpresa(self):
        print("Empresa: {:30} Ruc: {} \nDirección: {:28} Telefono: {}".format(self.nombre,self.ruc,self.direccion,self.telefono))
    
    def agregarDepa(self,id,empleado,descrip):
        depa=Departamento(id,empleado,descrip)
        self.departamento.append(depa)
    
    def agregarEmple(self,id,nom,ced,dir,tel,fi,sueldo):
        emple=Empleado(id,nom,ced,dir,tel,fi,sueldo)
        self.empleado.append(emple)

    def mostrarEmpleDepa(self):
        print("EMPLEADO")
        for i in self.empleado:
            print("Nombre: {:31} Cédula: {} \nDirección: {:28} Telefóno: {}".format(i.nombre,i.cedula,i.direccion,i.telefono))
        for j in self.departamento:
            print("Departamento: {}".format(j.descripcion))
        

class Empleado:
    def __init__(self,id,nom,ced,dir,tel,fi,sueldo): 
        self.__id = id
        self.nombre = nom
        self.cedula = ced  
        self.direccion = dir
        self.telefono = tel
        self.fecha_ingreso = fi
        self.sueldo = sueldo

    def mostrarEmpleado(self):
        print("Nombre: {} Cédula: {} Dirección: {} Telefóno: {} \nFecha Ingreso: {} Sueldo: {}".format(self.nombre,self.cedula,self.direccion,self.telefono,self.fecha_ingreso,self.sueldo,self.comision))

class Oficinista(Empleado): 
    def __init__(self,id,nom,ced,dir,tel,fi,sueldo,comision): 
        super().__init__(id,nom,ced,dir,tel,fi,sueldo) 
        self.comision = comision
    
    def mostrarEmpleado(self):
        print("Nombre: {} Cédula: {} Dirección: {} Telefóno: {} \nFecha Ingreso: {} Sueldo: {} Comisión: {}".format(self.nombre,self.cedula,self.direccion,self.telefono,self.fecha_ingreso,self.sueldo,self.comision))

class Obrero(Empleado):    
    def __init__(self,id,nom,ced,dir,tel,fi,sueldo,sindi,contr): 
        super().__init__(id,nom,ced,dir,tel,fi,sueldo)
        self.sindicato = sindi
        self.contratoColectivo = contr
    
    def mostrarEmpleado(self):
        print("Nombre: {} Cédula: {} Dirección: {} Telefóno: {} \nFecha Ingreso: {} Sueldo: {} Sindicato: {} Contrato Colectivo: {}".format(self.nombre,self.cedula,self.direccion,self.telefono,self.fecha_ingreso,self.sueldo,self.sindicato,self.contratoColectivo))

class Departamento:
    def __init__(self,id,empleado,descrip): 
        self.__id = id
        self.empleado = empleado 
        self.descripcion = descrip

    def mostrarDepa(self):
        print("Departamento: {}".format(self.descripcion))


class Prestamo:
    def __init__(self,id,empleado,fecha,valor,npagos,saldo,cuotas,estado=True):
        self.__id = id
        self.empleado = empleado
        self.fecha = fecha
        self.valor = valor
        self.npagos = npagos
        self.saldo = saldo
        self.cuotas = cuotas
        self.estado = estado

    def mostrarPrestamo(self):
        print("Empleado: {} Fecha: {} Valor: {} Número Pagos: {} Saldo: {} Cuotas: {} Estado: {}".format(self.empleado.nombre,self.fecha,self.valor,self.npagos,self.saldo,self.cuotas,self.Estado()))
 

class SobreTiempo:
    def __init__(self,id,empleado,ht,he,fecha,estado):
        self.id = id
        self.empleado = empleado
        self.horasTrabajadas = ht
        self.horasExtras = he
        self.fecha = fecha
        self.estado = estado

class Deducciones:
    def __init__(self,id,iess,comision,antiguedad):
        self.__id = id
        self.iess = iess        
        self.comision = comision
        self.antiguedad = antiguedad
        
class Pago_nomina:
    def __init__(self,id,empresa,sobretiempo=0,prestamo=0,fecha="",sueldo=0,comision=0,antiguo=0,totIngre=0,iess=0,totDescu=0,liquidacion=0):
        self.id = id
        self.empresa = empresa
        self.sobretiempo = sobretiempo
        self.prestamo = prestamo        
        self.fecha = fecha
        self.sueldo = sueldo
        self.comision = comision
        self.antiguo = antiguo
        self.totIngre = totIngre
        self.iess = iess
        self.totDescu = totDescu
        self.LiquiRecibir= liquidacion

    def calculo(self,deduiess,deducomision,deduantiguedad):
        valor_hora=self.sueldo/240
        self.sobretiempo = valor_hora *(self.sobretiempo.horasTrabajadas*0.50 + self.sobretiempo.horasExtras)
        self.comision = deducomision*(self.sueldo+self.sobretiempo)
        self.antiguo = deduantiguedad
        self.iess = deduiess*(self.sueldo+self.sobretiempo)
        self.prestamo = self.prestamo.cuotas
        self.totIngre = self.sueldo+self.sobretiempo+self.comision+self.antiguo
        self.totDescu = self.iess - self.prestamo
        self.LiquiRecibir = self.totIngre - self.totDescu

    def mostrarPagoNomina(self):
        print("-----------------------------------------------------------------------------------------------------")
        print("Fecha de Nomina: {}".format(self.fecha))
        print("-----------------------------------------------------------------------------------------------------")
        self.empresa.mostrarEmpresa()
        print("-----------------------------------------------------------------------------------------------------")
        self.empresa.mostrarEmpleDepa()
        print("-----------------------------------------------------------------------------------------------------")
        print("Pago Sobretiempo: ${}".format(self.sobretiempo))
        print("-----------------------------------------------------------------------------------------------------")
        print("Pago Comision: ${}".format(self.comision))
        print("-----------------------------------------------------------------------------------------------------")
        print("Pago Antiguedad: {}".format(self.antiguo))
        print("-----------------------------------------------------------------------------------------------------")
        print("Cobro Iess: ${}".format(self.iess))
        print("-----------------------------------------------------------------------------------------------------")
        print("Prestamo: ${}".format(self.prestamo))
        print("-----------------------------------------------------------------------------------------------------")
        print("Total Ingreso: ${}".format(self.totIngre))
        print("-----------------------------------------------------------------------------------------------------")
        print("Total Descuento: ${}".format(self.totDescu))
        print("-----------------------------------------------------------------------------------------------------")
        print("Liquidación: ${}".format(self.LiquiRecibir))
        print("-----------------------------------------------------------------------------------------------------")


emp = Empresa()
emple=Empleado("01","Ronny Peñaranda","0982949404","Av.Pollo Hornado","09895684684","12:50",480)

emp.agregarEmple("01","Ronny Peñaranda","0982949404","Av.Pollo Hornado","09895684684","12:50",480)
emp.agregarDepa("1",emple,"Social")

pres=Prestamo("1",emple,date.today(),1000,10,1000,100,20)
sobre=SobreTiempo("1",emple,8,10,date.today(),True)
dedu=Deducciones("1",10,50,2)
pago=Pago_nomina("1",emp,sobre,pres,date.today(),emple.sueldo)

pago.calculo(dedu.iess,dedu.comision,dedu.antiguedad)
pago.mostrarPagoNomina()
