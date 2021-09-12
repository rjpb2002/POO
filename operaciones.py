class operaciones:
    def __init__(self,n1,n2):
        self.numero1=n1
        self.numero2=n2
    
    def suma(self):
        suma= self.numero1 + self.numero2
        return suma
    
    def resta(self):
        # if self.numero1 >= self.numero2:
        #     return  self.numero1 - self.numero2
        return self.numero1 - self.numero2
    
    def multiplicacion(self):
        return self.numero1 * self.numero2
         
    def division(self):
        if self.numero2 != 0: return self.numero1 / self.numero2
        return 0 
    def divisionEntera(self):
        if self.numero2 != 0: return self.numero1 // self.numero2
        return 0
    
    def residuo(self):    
        return self.numero1 % self.numero2

    def exponente(self):
        return self.numero1 ** self.numero2

    def mostrar(self):
        print("Operando1={}, Operando2={}".format(self.numero1,self.numero2))

print("\n1)Suma  \n2)Resta  \n3)Multiplicación  \n4)Division  \n5)División Entera  \n6)Residuo  \n7)Exponente  \n8)Salir")
opcion=0
while opcion != "8":
    opcion= input("Elija opción[1....8]: ")
    if opcion    or opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6" or opcion == "7":
        n1= int(input("Ingrese número 1: "))
        n2= int(input("Ingrese número 2: "))
        dato= operaciones(n1,n2)
    if opcion == "1":
        print("La suma de {} + {} es = {}".format(dato.numero1,dato.numero2,dato.suma()))
    elif opcion == "2":
        print("La resta de {} + {} es = {}".format(dato.numero1,dato.numero2,dato.resta()))
    elif opcion == "3":
        print("La multiplicación de {} * {} es = {}".format(dato.numero1,dato.numero2,dato.multiplicacion()))
    elif opcion == "4":
        print("La división de {} / {} es = {}".format(dato.numero1,dato.numero2,dato.division()))
    elif opcion == "5":
        print("La división Entera de {} / {} es = {}".format(dato.numero1,dato.numero2,dato.divisionEntera()))
    elif opcion == "6":
        print("El residuo de {} / {} es = {}".format(dato.numero1,dato.numero2,dato.residuo()))
    elif opcion == "7":
        print("El exponente de {} ** {} es = {}".format(dato.numero1,dato.numero2,dato.exponente()))
    else:
        print("Gracias por su visita!!")

