#9.-Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, 
# obtenga el resultado de la siguiente función:

class variables:
    def enteros(self):
        v1 = int(input("Ingrese el primer valor entero: ")) 
        v2 = int(input("Ingrese el segundo valor entero: "))
        if v1 == 1:
            res = 100 * v2
        elif v1 == 2:
            res = 100 ** v2
        elif v1 == 3:
            res = 100 / v2
        else:
            res = 0
        print("El resultado es de: {:.2f}".format(res))

dato = variables()
dato.enteros()
