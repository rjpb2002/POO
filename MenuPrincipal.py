from Calculadora import CalCientifica, CalEstandar
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
        os.system("cls")
        while opc1 != "10":
            os.system("cls")
            dato1=Menu("Menu Calculadora",["1)Suma","2)Resta","3)Multiplicación","4)División","5)Exponente","6)Valor Absoluto","7)Circuferencia","8)Area Circulo","9)Area Cuadrado","10)Salir"])
            opc1= dato1.menu()
            if opc1 == "1":
                os.system("cls")
                print("Suma de dos números")
                n1=int(input("Ingrese el primer número: "))
                n2=int(input("Ingrese el segundo número: "))
                calEst = CalEstandar(None,n1,n2)
                sumar= calEst.suma()
                print("{} + {} = {}".format(n1,n2,sumar))
                input("Presione una tecla para continuar...")
            elif opc1 == "2":
                os.system("cls")
                print("Resta de dos números")
                n1=int(input("Ingrese el primer número: "))
                n2=int(input("Ingrese el segundo número: "))
                calEst = CalEstandar(None,n1,n2)
                restar= calEst.resta()
                print("{} - {} = {}".format(n1,n2,restar))
                input("Presione una tecla para continuar...")
            elif opc1 == "3":
                os.system("cls")
                print("Multiplicación de dos números")
                n1=int(input("Ingrese el primer número: "))
                n2=int(input("Ingrese el segundo número: "))
                calEst = CalEstandar(None,n1,n2)
                multi= calEst.mutiplicacion()
                print("{} * {} = {}".format(n1,n2,multi))
                input("Presione una tecla para continuar...")
            elif opc1 == "4":
                os.system("cls")
                print("División de dos números")
                n1=int(input("Ingrese el primer número: "))
                n2=int(input("Ingrese el segundo número: ")) 
                if n2 != 0:
                    calEst = CalEstandar(None,n1,n2)
                    div= calEst.división()
                    print("{} / {} = {:.2f}".format(n1,n2,div))
                    input("Presione una tecla para continuar...")
                else:
                    print("No es posible la división para 0")
                    input("Presione una tecla para continuar...")
            elif opc1 == "5":
                os.system("cls")
                print("Potencia")
                n1=int(input("Ingrese número base: "))
                n2=int(input("Ingrese el exponente : "))
                calEst = CalEstandar(None,n1,n2)
                exp= calEst.exponente()
                print("{} ^ {} = {}".format(n1,n2,exp))
                input("Presione una tecla para continuar...")
            elif opc1 == "6":
                os.system("cls")
                print("Valor absoluto de un número")
                n=int(input("Ingrese el número base: "))
                calEst = CalEstandar(n,None,None)
                va= calEst.valorAbsoluto()
                print("El valor absoluto de {} es: {}".format(n,va))
                input("Presione una tecla para continuar...")
            elif opc1 == "7":
                os.system("cls")
                print("La Circuferencia de un Circulo")
                r=float(input("Ingrese el radio del circulo: "))
                calEst = CalCientifica(None,None,r,None)
                cir= calEst.circunferencia()
                print("La circuferencia de {} es: {:.2f} cm".format(r,cir))
                input("Presione una tecla para continuar...")
            elif opc1 == "8":
                os.system("cls")
                print("El Area de un Circulo")
                r=float(input("Ingrese el radio del circulo: "))
                calEst = CalCientifica(None,None,r,None)
                area= calEst.areaCirculo()
                print("El Area de {} es: {:.2f} cm2".format(r,area))
                input("Presione una tecla para continuar...")
            elif opc1 == "9":
                os.system("cls")
                print("El Area de un Cuadrado")
                l=float(input("Ingrese el lado del Cuadrado(cm): "))
                calEst = CalCientifica(None,None,None,l)
                lado= calEst.areaCuadrado()
                print("El Area de {} es: {:.2f} cm2".format(l,lado))
                input("Presione una tecla para continuar...")
            else:
                pass
  
    elif opc == "2":
        dato2=Menu("Menu Numero",["1) Perfecto","2) Salir"])



    elif opc == "3":
        print("Menu Listas""\nSuma""\nResta""\nSalir")



    elif opc == "4":
        print("Menu Cadenas""\nSuma""\nResta""\nSalir")



    elif opc == "5":    
        print("Gracias por su visita")
    else:
        print("Opcion no valida")


