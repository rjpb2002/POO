#7.-Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.

class numeros:
    def mayor(self):
        num1 = int(input("Ingrese el primer número : "))
        num2 = int(input("Ingrese el segundo número : "))
        num3 = int(input("Ingrese el tercer número : "))
        if num1 > num2 and num1 > num3:
            numy = num1
        else:
            if num2 > num3:
                numy = num2
            else:
                numy = num3
        print("El número mayor es: {}".format(numy))

dato = numeros()
dato.mayor()
