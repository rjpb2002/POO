class Calculadora:
    def __init__(self,numero1,numero2):
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
    def __init__(self,numero,numero1, numero2):
            super().__init__(numero1,numero2)
            self.numero= numero

    def mutiplicacion(self):
        return self.num1 * self.num2

    def exponente(self):
        return self.num1 ** self.num2

    def valorAbsoluto(self):
        if self.numero < 0:
            self.numero = self.numero*-1
        else:
            self.numero = self.numero
        return self.numero


class CalCientifica(Calculadora):
    PI = 3.1416 
    def __init__(self,numero1, numero2,radio,lado):
        super().__init__(numero1,numero2)
        self.radio=radio
        self.lado=lado

    def circunferencia(self):
        return 2 * CalCientifica.PI * self.radio
    
    def areaCirculo(self):
        return CalCientifica.PI * (self.radio*self.radio)
    
    def areaCuadrado(self):
        return self.lado * self.lado

