# 16.-Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N 
# y calcular el resultado de la siguiente serie:
# 1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. 

class numero:
    def entero(self):
        s = 0
        l = 1
        num = int(input("Ingrese un número entero: "))
        b = "T"
        while l < num:
            if b == "T":    
                s = s + (1/l)
                b = "F"
            else:
                s = s - (1/l)
                b = "T"
            l = l + 1

        print("El resultado de las series es de: {}".format(s))

dato = numero()
dato.entero()

