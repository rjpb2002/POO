#6.-Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% 
# si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

class empleado:
    def sueldo(self):
        se = float(input("Ingrese su sueldo básico: $"))
        if se < 600:
            nuevo = se + se * 0.1
            print("El nuevo sueldo será de: ${:.2f}".format(nuevo))
        else:
            nuevo = se               
            print("El sueldo no tendrá aumento será de: ${:.2f}  ".format(nuevo))

dato = empleado()
dato.sueldo()
