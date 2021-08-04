class Calculadora:
    def __init__(self,numero1=0,numero2=0):
        self.num1=numero1
        self.num2=numero2

    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicación(self):
        multi = self.num1 * self.num2
        print("{} * {} = {}".format(self.num1,self.num2,multi))
    
    def división(self):
        return self.num1 / self.num2
    

class CalEstandar(Calculadora):
    def __init__(self,numero1=0, numero2=0):
            super().__init__(numero1,numero2)

    def mutiplicacion(self):
        return self.num1 * self.num2

    def exponente(self):
        return self.num1 ** self.num2

    def valorAbsoluto(self,numero):
        if numero < 0:
            numero = numero*-1
        else:
            numero = numero
        return numero


class CalCientifica(Calculadora):
    PI = 3.1416 
    def __init__(self,numero1=0, numero2=0):
        super().__init__(numero1,numero2)

    def circunferencia(self,radio):
        return 2 * CalCientifica.PI * radio
    
    def areaCirculo(self,radio):
        return CalCientifica.PI * (radio*radio)
    
    def areaCuadrado(self,lado):
        return lado * lado

