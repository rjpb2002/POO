#17.-Calcular el factorial de N números enteros leídos de teclado.
# El problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número.

class factorial:
    def numero(self):
        num = int(input("Ingrese la cantidad de veces: "))
        a=1
        for a in range (num):
            n = int(input("Ingrese un número entero: "))
            fac = 1
            for b in range(1, n+1):
                fac *= b
            
            print("El factorial del número {} es: {}".format(n,fac))

dato = factorial()
dato.numero()
