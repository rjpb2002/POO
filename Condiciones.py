class Condicion:
    contador = 0 #variables de clases (opcional)
    #__init__ metodo-constructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
    #e inicializar los atributos de la clase. self es un objeto que representa la clase creada

    def __init__(self, num1=0, num2=1):
        self.numero1 = num1 #variables de instancia
        self.numero2 = num2 #variables de instancia
        numero= num1 + num2
        self.numero3 = numero


    def usoIf(self):
        # if........ elif.......... else.......... permiten condicionar la ejecucion de una o mas bloques.
        # de sentancia al cumplimiento de un o varias condiciones.
        if self.numero1 == self.numero2:
            print("num1:{}, num2:{}: son iguales".format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3:
            print("num1:{}, num3:{}: son iguales".format(self.numero1,self.numero3))

        else:
            print("No son iguales")


#Usar la clase
#cond1 = Condicion()
#print(cond1.numero1)
#print(cond1.numero2)

cond2 = Condicion(10,20)
cond2.usoIf() # Llamada a un método
print("************************************************************************************************************************")
print(cond2.numero1) # Llamada a un atributo de la clase
