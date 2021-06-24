#2.-Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. 
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes
# y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.

class vendedor:
    def sueldo(self):
        SueldoBase = float(input("Ingrese su sueldo básico: $"))
        Venta1 = float(input("Ingrese el valor de la primera venta: $"))
        Venta2 = float(input("Ingrese el valor de la segunda venta: $"))
        Venta3 = float(input("Ingrese el valor de la tercera venta: $"))
        VT = Venta1 + Venta2 + Venta3
        CV = VT * 0.1
        Total = SueldoBase + CV
        print("El sueldo total a recibir con las comisiones será de: ${:.2f}".format(Total))

dato = vendedor()
dato.sueldo()
