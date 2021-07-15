class logica:
    def __init__(self,lista=None):
        self.__lista = lista
        
    
    @property
    def lista(self):
        return self.__lista
    
    @lista.setter
    def lista(self,valor):
        self.__lista = valor    
    
    def parImpar(self,numero):
        if numero % 2 == 0:
            print("El número {} es Par".format(numero))
        else:
            print("El número {} es Impar".format(numero))

    def perfecto(self,numero):
        acum=0
        for i in range (1,numero):
            if numero % i == 0:
                acum += i
        if numero == acum:
            print("El {} es perfecto".format(numero))
        else:
            print("El {} es no perfecto".format(numero))


# ejer= logica([2,4,6])
# print(ejer.lista)

# num=int(input("Ingrese número: "))
# ejer.parImpar(num)


class Ejercicio(logica):
    def __init__(self,lista,numeros):
        super().__init__(lista)
        self.dato = numeros 

    def sumar(self,n1,n2):
        return n1 + n2
    
    def parImpar(self,numero):
        super().parImpar(numero)
        return numero % 2

ejer = Ejercicio([1,3,5], 40)
if ejer.parImpar(6) == 0:
    print("Par")
else:
    print("Impar")
print(ejer.lista)
ejer.perfecto(6)
# print(ejer.sumar(4,8))