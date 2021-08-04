class Basico:
    def __init__(self,numero=0):
        self.num = numero 
    
    def numerosN(self):
        for i in range(self.num-1):
            print(str(i+1),end="  ")
        return self.num
    
    def suma(self):
        acum = 0
        for i in range (1,self.num+1):
            acum = acum +i
        return acum
    
    def multiplos(self,multiplo):
        if  multiplo % self.num == 0:
            return True
        else:
            return False

    def DivisoresNumero(self):
        contador = 0
        print("\nLos divisores de {}".format(self.num), "son: ")
        for divisor in range(1,self.num+1):
            if (self.num % divisor) == 0 :
                print(divisor,"es divisor de {}".format(self.num))
                contador += 1
        return contador

    def primo(self):
        for n in range(2,self.num):
            if self.num % n == 0 and self.num != 2:
                
                return "{} No es primo".format(self.num)
        if self.num == 1:
            
            return "{} No es primo".format(self.num)
        return "{} Es primo".format(self.num)

    def perfecto(self):
        perfect = 0
        numero2 = 1
        while numero2 < self.num:
            if (self.num % numero2 == 0):
                perfect = perfect + numero2
            numero2 = numero2 + 1
        return perfect
    
class Intermedio(Basico):
    def _init_(self,numero=0,num2=0):
        super().__init__(numero)
        self.num2=num2

    def suma(self):
        acum = 0
        for i in range (1,self.num+1):
            acum = acum +i
        return "La suma acumulada será: {}".format(acum)
  
    def factorial(self):
        fact = 1
        if self.num != 0:
            for i in range(1,self.num +1):
                fact = fact * i
        return fact
    
    def fibonacci(self):
        a, b = 0,1
        for i in range(self.num):
            print(a, end="  ")
            a, b = b, a + b
        return i

    def primosgemelos(self,num2):
        dato = Basico(self.num)
        print(dato.primo())
        dato=dato.primo()
        dato1 = Basico(num2)
        print(dato1.primo())
        dato1=dato1.primo()
        resul = 0
        if dato == "{} Es primo".format(self.num) and dato1 == "{} Es primo".format(num2):
            if self.num > num2:
                resul= self.num - num2
                print("\nPara ser primos gemelos el resultado deber ser igual a 2")
                print("La resta es: {} - {} = {}".format(self.num,num2,resul))
            else:
                resul = num2 - self.num
                print("\nPara ser primos gemelos el resultado deber ser igual a 2")
                print("La resta es: {} - {} = {}".format(num2,self.num,resul))
        
        if resul == 2:
            print("\nEntonces los numeros {} y {} son primos gemelos ".format(self.num,num2))
        else:
            print("\nEntonces los numeros {} y {} no son primos gemelos ".format(self.num,num2))


    def amigos(self,num2):
        dato = Basico(self.num)
        dato=dato.perfecto()
        dato1 = Basico(num2)
        dato1=dato1.perfecto()

        if dato == dato1:
            print("La suma de los divisores(exceptuando el mismo número) de los dos números deben ser iguales.")
            print("La suma de los divisores de '{}' es {}".format(self.num,dato))
            print("La suma de los divisores de '{}' es {}".format(num2,dato1))
            print("{} es igual a {}".format(dato,dato1))
            print("\nEntonces los numeros '{}' y '{}' son números amigos ".format(self.num,num2))
        else:
            print("La suma de los divisores(exceptuando el mismo número) de los dos números deben ser iguales.")
            print("La suma de los divisores de '{}' es {}".format(self.num,dato))
            print("La suma de los divisores de '{}' es {}".format(num2,dato1))
            print("{} no es igual a {}".format(dato,dato1))
            print("\nEntonces los numeros '{}' y '{}' no son números amigos".format(self.num,num2))

