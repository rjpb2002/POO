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
        pass
    
class CalEstandar(Calculadora):
    def __init__(self,numero1, numero2):
            super().__init__(numero1,numero2)
            

    
    def mutiplicacion():
        return self.num1 * self.num2

    def exponente():
        pass 

    def valorAbsoluto(numero):
        # if numero < 0:
        #     numero = numero*-1
        # return numero
        pass

class CalCientifica(Calculadora):
    PI = 3.1416 
    def __init__(self, numero1, numero2):
        super().__init__(numero1,numero2)
        pass


# n1 = int(input("Ingrese n1: "))
# n2 = int(input("Ingrese n2: "))


# cal = Calculadora(4,8)
# cal.multiplicación()
# calEst = CalEstandar(4,8)
# print(calEst.multiplicación())


