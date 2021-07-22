from Calculadora import CalEstandar
import os

class Menu:
    def __init__(self,titulo="",opciones= []):
        self.titulo = titulo
        self.opciones = opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija opcion[1....{}]: ".format(len(self.opciones)))
        return opc

opc=""
while opc != "5":
    os.system("cls")
    dato = Menu("Menu Principal",["1) Calculadora","2) Numeros","3) Listas","4) Cadenas","5) Salir"])
    opc = dato.menu()
    if opc == "1":
        opc1=""
        while opc1 != "3":
            os.system("cls")
            dato1=Menu("Menu Calculadora",["1)Suma","2)Resta","3)Salir"])
            opc1= dato1.menu()
            if opc1 == "1":
                os.system("cls")
                print("Suma de dos números")
                n1=int(input("Ingrese n1: "))
                n2=int(input("Ingrese n2: "))
                calEst = CalEstandar(n1,n2)
                suma= calEst.suma()
            
                print("{} + {} = {}".format(n1,n2,suma))
                input("Presione una tecla para continuar...")

            
    elif opc == "2":
        dato2=Menu("Menu Numeros""\nPerfecto""\nSalir")

    elif opc == "3":
        print("Menu Listas""\nSuma""\nResta""\nSalir")
    elif opc == "4":
        print("Menu Cadenas""\nSuma""\nResta""\nSalir")
    elif opc == "5":    
        print("Gracias por su visita")
    else:
        print("Opcion no valida")
