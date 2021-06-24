#10.- Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100

class escribir:
    def numeros(self):
        n= 1
        while n <= 100:
            print(n,"/",end=" ")
            n = n + 1

dato = escribir()
dato.numeros()