class Ciclos:
    def __init__(self, num1=0):
        self.numero = num1

    def usoWhile(self):
        #Ciclo repetitivo que se ejecuta con verdadero y sale por falso
        car = input("Ingrese una vocal: ")
        car = car.lower()
        while car not in("a","e","i","o","u"):
            car=input("Ingrese una vocal").lower()
        print("Felicitaciones el caracter: {} es una vocal".format(car))

ciclo1 = Ciclos()
ciclo1.usoWhile()


