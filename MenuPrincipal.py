from Calculadora import CalCientifica, CalEstandar
from Numeros import Basico,Intermedio
from Listas import Lista
from Cadenas import Cadena
import os
#RONNY
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
            #! MENU CALCULADORA
            os.system("cls")
            dato1=Menu("Menu Calculadora",["1)Suma","2)Resta","3)Multiplicación","4)División","5)Exponente","6)Valor Absoluto","7)Circuferencia","8)Area Circulo","9)Area Cuadrado","10)Salir"])
            opc1= dato1.menu()
            #? SUMA
            if opc1 == "1":
                try:
                    os.system("cls")
                    print("Suma de dos números")
                    n1=int(input("\nIngrese el primer número: "))
                    n2=int(input("Ingrese el segundo número: "))
                    calEst = CalEstandar(n1,n2)
                    sumar= calEst.suma()
                    print("\n{} + {} = {}".format(n1,n2,sumar))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? RESTA
            elif opc1 == "2":
                try:
                    os.system("cls")
                    print("Resta de dos números")
                    n1=int(input("\nIngrese el primer número: "))
                    n2=int(input("Ingrese el segundo número: "))
                    cal = CalEstandar(n1,n2)
                    restar= cal.resta()
                    print("\n{} - {} = {}".format(n1,n2,restar))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó una letra...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? MULTIPLICACIÓN
            elif opc1 == "3":
                try:
                    os.system("cls")
                    print("Multiplicación de dos números")
                    n1=int(input("\nIngrese el primer número: "))
                    n2=int(input("Ingrese el segundo número: "))
                    cal = CalEstandar(n1,n2)
                    multi= cal.mutiplicacion()
                    print("\n{} x {} = {}".format(n1,n2,multi))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? DIVISIÓN
            elif opc1 == "4":
                try:
                    os.system("cls")
                    print("División de dos números")
                    n1=int(input("\nIngrese el primer número: "))
                    n2=int(input("Ingrese el segundo número: ")) 
                    if n2 != 0:
                        cal = CalEstandar(n1,n2)
                        div= cal.división()
                        print("\n{} / {} = {:.2f}".format(n1,n2,div))
                        input("\nPresione la tecla 'Enter' para continuar...")
                    else:
                        print("No es posible la división para 0")
                        input("\nPresione una tecla para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #?EXPONENTE
            elif opc1 == "5":
                try:
                    os.system("cls")
                    print("Exponente")
                    n1=int(input("\nIngrese número base: "))
                    n2=int(input("Ingrese el exponente : "))
                    cal = CalEstandar(n1,n2)
                    exp= cal.exponente()
                    print("\n{} ^ {} = {}".format(n1,n2,exp))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #?VALOR ABSOLUTO            
            elif opc1 == "6":
                try:
                    os.system("cls")
                    print("Valor absoluto de un número")
                    n=int(input("\nIngrese el número base: "))
                    cal = CalEstandar()
                    va= cal.valorAbsoluto(n)
                    print("\nEl valor absoluto de {} es: {}".format(n,va))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("Presione la tecla 'Enter' para regresar al menú anterior...")
            #?CIRCUFERENCIA
            elif opc1 == "7":
                try:
                    os.system("cls")
                    print("La Circuferencia de un Circulo")
                    r=float(input("\nIngrese el radio del circulo: "))
                    cal = CalCientifica()
                    cir= cal.circunferencia(r)
                    print("\nLa circuferencia de {} es: {:.2f} cm".format(r,cir))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("Presione la tecla 'Enter' para regresar al menú anterior...")
            #?ARENA CIRCULO
            elif opc1 == "8":
                try:
                    os.system("cls")
                    print("El Area de un Circulo")
                    r=float(input("\nIngrese el radio del circulo: "))
                    cal = CalCientifica()
                    area= cal.areaCirculo(r)
                    print("\nEl Area de {} es: {:.2f} cm2".format(r,area))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("Presione la tecla 'Enter' para regresar al menú anterior...")
            #?AREA CUADRADO
            elif opc1 == "9":
                try:
                    os.system("cls")
                    print("El Area de un Cuadrado")
                    l=float(input("\nIngrese el lado del Cuadrado(cm): "))
                    cal = CalCientifica()
                    lado= cal.areaCuadrado(l)
                    print("\nEl Area de {} es: {:.2f} cm2".format(l,lado))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("\nNo se Digitó un número...")
                    input("Presione la tecla 'Enter' para regresar al menú anterior...")
            #?SALIR
            else:
                pass
  
    elif opc == "2":
        opc2=""
        os.system("cls")
        while opc2 != "11":
            #! MENU OPERACIÓN NÓMEROS
            os.system("cls")
            dato2=Menu("Menu Operación Números",["1) Presentar los números de 1 a n","2) Sumar los números de 1 a n","3) Múltiplo de cualquier numero","4) Presentar los divisores de un numero","5) Numero Primo",
            "6) Factorial de cualquier numero","7) Fibonacci de una serie de n números","8) Perfecto","9) Primos gemelos","10) Números amigos","11) Salir"])
            opc2= dato2.menu()
            #? PRESENTAR NUMERO
            if opc2 == "1":
                try:
                    os.system("cls")
                    print("Presentar número")
                    n=int(input("\nIngrese hasta que número quiere presentar: "))
                    dato= Basico(n)
                    print("\nLos números a presentar son:")
                    print(dato.numerosN())
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? SUMAR ACUMULADO
            elif opc2 == "2":
                try:
                    os.system("cls")
                    print("Sumar Acumulado")
                    n = int(input("\nIngrese un numero: "))
                    dato=Basico(n)
                    acum =dato.suma()
                    print("\nLa suma del numero 1 hasta el numero {} dio: {}".format(n,acum)) 
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? MULTIPLO NUMERO
            elif opc2 == "3":
                try:
                    os.system("cls")
                    print("Multiplo Número")
                    n1=int(input("\nIngrese un numero: "))
                    n2=int(input("Ingrese el multiplo: "))
                    dato=Basico(n1)
                    res = dato.multiplos(n2)
                    if res == True:
                        print("\nEl numero {} Si es múltiplo de {}".format(n2,n1))
                    else:
                        print("\nEl numero {} No es múltiplo de {}".format(n2,n1))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? DIVISORES NUMERO
            elif opc2 == "4":
                try:
                    os.system("cls")
                    print("Divisores Número")
                    divis = int(input("\nIngrese un número: "))
                    dato=Basico(divis)
                    contador =dato.DivisoresNumero()
                    print("\nEl número total de divisores que tiene {} son {} divisores".format(divis,contador))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? NUMERO PRIMO
            elif opc2 == "5":
                try:
                    os.system("cls")
                    print("Número Primo")
                    n = int(input("\nIngrese un numero: "))
                    dato = Basico(n)
                    print("\n{}".format(dato.primo()))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? FACTORIAL NUMERO
            elif opc2 == "6":
                try:
                    os.system("cls")
                    print("Factorial Número")
                    cant = int(input("\nIngrese un numero: "))
                    dato= Intermedio(cant)
                    fact=dato.factorial()
                    print("\nEL factorial del numero {} es: {} ".format(cant,fact))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? FIBONACCI SERIE
            elif opc2 == "7":
                try:
                    os.system("cls")
                    print("Fibonacci Serie")
                    fib = int(input("\nIngrese número de términos para la sucesión: "))
                    dato= Intermedio(fib)
                    print("\nLa serie de las sucesiones son:")
                    print(dato.fibonacci())
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? PERFECTO
            elif opc2 == "8":
                try:
                    os.system("cls")
                    print("Número Perfecto")
                    numPerfect=int(input("\nIngrese el número: "))
                    dato= Basico(numPerfect)
                    perfect=dato.perfecto()
                    if perfect == numPerfect:
                        print("\nEl numero {}".format(numPerfect),"si es perfecto")
                    else:
                        print("\nEl numero {}".format(numPerfect),"no es perfecto")
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? PRIMOS GEMELOS
            elif opc2 == "9":
                try:
                    os.system("cls")
                    print("Primos Gemelos")
                    num1 = int(input("\nIngrese primer número: "))
                    num2= int(input("Ingrese segundo número: "))
                    os.system("cls")
                    dato = Intermedio(num1)
                    print("Los números son:")
                    dato.primosgemelos(num2)
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? NUMEROS AMIGOS
            elif opc2 == "10":
                try:
                    os.system("cls")
                    print("Números Amigos")
                    num1 = int(input("\nIngrese primer número: "))
                    num2= int(input("Ingrese segundo número "))
                    os.system("cls")
                    dato = Intermedio(num1)
                    dato.amigos(num2)
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? SALIR
            else:
                pass

    elif opc == "3":
        opc3=""
        os.system("cls")
        while opc3 != "11":
            #! MENU TRATAMIENTO LISTAS
            os.system("cls")
            dato3=Menu("Menu Listas",["1) Recorrer y presentar los datos de una lista","2) Buscar un valor en una lista","3) Retornar una lista con los factoriales","4) Retornar una lista de números primos",
            "5) Recorrer una lista de diccionario con notas de alumnos","6) Insertar un dato en una Lista dada lo Posición","7) Eliminar todas las ocurrencias en una Lista","8) Retornar cualquier valor de una lista eliminándolo",
            "9) Copiar cada elemento de una tupla en una lista","10 Dar el vuelto a varios clientes","11) Salir"])
            opc3= dato3.menu()
            #? PRESENTAR LISTA
            if opc3 == "1":
                try:
                    os.system("cls")
                    print("Presentar Lista")
                    l=[]
                    t=int(input("\nIngrese el tamaño de la lista: "))
                    for i in range(t):
                        v=input("Ingrese el valor {} : ".format(i+1))
                        l.append(v)
                    os.system("cls")
                    print("La lista es: {}".format(l))
                    li = Lista(l)
                    print("\nEl recorrido de la lista será:")
                    li.presentarLista()
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó una letra...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #?BUSCAR LISTA
            elif opc3 == "2":
                try:
                    os.system("cls")
                    print("Buscar Lista")
                    l=[]
                    t=int(input("\nIngrese el tamaño de la lista: "))
                    for i in range(t):
                        v=input("Ingrese el valor {} : ".format(i+1)).title()
                        l.append(v)
                    print("\nLa lista es: {}".format(l))
                    nv=input("Que valor desea buscar de la lista? ").title()
                    li = Lista(l)
                    print("\nLas posiciones serán desde [0 hasta {}]".format(len(l)-1))
                    li.buscarLista(nv)
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #?LISTA FACTORIAL
            elif opc3 == "3":
                try:
                    os.system("cls")
                    print("Lista Factorial")
                    l=[]
                    t=int(input("\nIngrese la cantidad de factoriales: "))
                    for i in range(t):
                        v=int(input("Ingrese el factorial {} : ".format(i+1)))
                        l.append(v)
                    print("\nLa lista de factoriales ingresados son: {}".format(l))
                    li = Lista(l)
                    print(li.listaFactorial())
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #?LISTA PRIMO
            elif opc3 == "4":
                try:
                    os.system("cls")
                    print("Lista Primo")
                    l=[]
                    t=int(input("\nIngrese la cantidad de números: "))
                    for i in range(t):
                        v=int(input("Ingrese número {} : ".format(i+1)))
                        l.append(v)
                    print("\nLa lista de números son: {}".format(l))
                    li = Lista(l)
                    print(li.listaPrimo())
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #?LISTA NOTA
            elif opc3 == "5":
                try:
                    os.system("cls")
                    print("Diccionario con Notas de Alumnos")
                    lisAlum = {}
                    opcion = ""
                    n=int(input("\nLa cantidad de Alumnos: "))
                    for i in range(n):
                        notas=[]
                        nombre = input("\nNombre del Alumno: ").title()
                        while nombre in lisAlum:
                            print("El nombre ya se encuentra en la lista.")
                            print("\nIngrese nuevamente..")
                            nombre = input("Nombre del Alumno: ").title()
                        n2=int(input("Ingrese la cantidad de notas: "))
                        for i in range (n2):
                            numero = input("Ingrese la nota {}: ".format(i+1))
                            notas.append(numero)
                            lisAlum[nombre]=notas
                    os.system("cls")
                    l=Lista()
                    print("El recorrido del diccionario será:")
                    l.listaNotas(lisAlum)
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #?INSERTAR LISTA
            elif opc3 == "6":
                try:
                    os.system("cls")
                    print("Insertar dato en Lista")
                    l=[]
                    t=int(input("\nIngrese el tamaño de la lista: "))
                    for i in range(t):
                        v=input("Ingrese el valor {} : ".format(i+1)).title()
                        l.append(v)
                    os.system("cls")
                    print("La lista es: {}".format(l))
                    nv=(input("Que valor desea insertar? ")).title()
                    print("\nLas posiciones posibles son desde [0 hasta {}]".format(len(l)))
                    pos=int(input("Que posición desea? "))
                    li = Lista(l)
                    print(li.insertarLista(nv,pos))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #?ELIMINAR LISTA
            elif opc3 == "7":
                try:
                    os.system("cls")
                    print("Eliminar Ocurrencia en Lista")
                    l=[]
                    t=int(input("\nIngrese el tamaño de la lista: "))
                    for i in range(t):
                        v=input("Ingrese el valor {} : ".format(i+1)).title()
                        l.append(v)
                    os.system("cls")
                    print("La lista es: {}".format(l))
                    valor=input("Que ocurrencia desea eliminar? ").title()
                    li = Lista(l)
                    print(li.eliminarLista(valor))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #?RETORNAR VALOR LISTA
            elif opc3 == "8":
                try:
                    os.system("cls")
                    print("Retonar un valor de una Lista")
                    l=[]
                    t=int(input("\nIngrese el tamaño de la lista: "))
                    for i in range(t):
                        v=(input("Ingrese el valor {} : ".format(i+1))).title()
                        l.append(v)
                    os.system("cls")
                    print("\nLa lista es: {}".format(l))
                    print("Las posiciones posibles son desde [0 hasta {}]".format(len(l)-1))
                    pos=int(input("Que posición desea? "))
                    li = Lista(l)
                    print(li.retornaValorLista(pos))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #?COPIAR TUPLA
            elif opc3 == "9":
                try:
                    os.system("cls")
                    print("Copia Tupla")
                    tupla=()
                    t=int(input("\nIngrese el tamaño de la lista: "))
                    for i in range(t):
                        v=tuple(input("Ingrese el valor {} : ".format(i+1)))
                        tupla+= tuple(v)
                    os.system("cls")
                    print("La tupla es: {}".format(tupla))
                    tup= Lista(None)
                    print(tup.copiarTuplaLista(tupla))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")

            #?VUELTO LISTA
            elif opc3 == "10":
                try:
                    os.system("cls")
                    print("Vuelto Lista")
                    lisVuelto = {}
                    opcion = ""
                    n=int(input("\nLa cantidad de Clientes: "))
                    for i in range(n):
                        v=[]
                        nombre = input("\nNombre del Cliente: ").title()
                        while nombre in lisVuelto:
                            print("El nombre ya se encuentra en la lista.")
                            print("\nIngrese nuevamente..")
                            nombre = input("\nNombre del Cliente: ").title()
                        vuelto = float(input("Ingrese el vuelto : $"))
                        v.append(vuelto)
                        lisVuelto[nombre]= v
                    os.system("cls")
                    l=Lista()
                    print("El recorrido del diccionario será:")
                    l.vueltoLista(lisVuelto)
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #?SALIR
            else:
                pass

    elif opc == "4":
        opc4=""
        os.system("cls")
        while opc4 != "10":
            #! MENU OPERACIONES DE CADENAS
            os.system("cls")
            dato4=Menu("Menú Operaciones de Cadenas",["1) Recorrer y presentar los datos de una cadena","2) Buscar un carácter en una cadena","3) Retornar una lista con la posición dado un carácter de la cadena","4) Lista Palabras",
            "5) Retornar una cadena a partir de una lista","6) Insertar un dato en una cadena dada lo Posición","7) Eliminar todas las ocurrencias en una cadena","8) Retornar cualquier valor de una cadena eliminándolo ","9) Concatenar Cadenas","10) Salir"])
            opc4= dato4.menu()
            #? RECORRER CADENA
            if opc4 == "1":
                try:
                    os.system("cls")
                    print("Recorrer Cadena")
                    ca=str(input("\nIngresar cadena: ")).lower()
                    os.system("cls")
                    dat= Cadena(ca)
                    print("La cadena recorrida:")
                    print("")
                    dat.recorrerCadena()
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó una letra...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? BUSCAR CARÁCTER
            if opc4 == "2":
                try:
                    os.system("cls")
                    print("Buscar Carácter")
                    ca=str(input("\nIngresar cadena: ")).lower()
                    bus=input("Que carácter desea buscar(solo una letra)? ").lower()
                    dat= Cadena(ca)
                    dat.buscarCaracter(bus)
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")
            #? LISTA POSICIONES
            elif opc4 == "3":
                try:
                    os.system("cls")
                    print("Lista Posiciones")
                    ca=str(input("\nIngresar cadena: ")).lower()
                    bus=str(input("Que carácter desea buscar(solo una letra)? ")).lower()
                    dat= Cadena(ca)
                    print("\nLa posición de caracteres será desde [0 hasta {}]".format(len(ca)-1))
                    dat.listaPosiciones(bus)
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")            
            #? LISTA PALABRAS
            elif opc4 == "4":
                try:
                    os.system("cls")
                    print("Lista Palabras")
                    ca=str(input("\nIngresar cadena: ")).lower()
                    dat= Cadena(ca)
                    print(dat.listaPalabras())
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...") 
            #? CADENA LISTA
            elif opc4 == "5":
                try:
                    os.system("cls")
                    print("Cadena Lista")
                    l=[]
                    t=int(input("\nIngrese el tamaño de la lista: "))
                    for i in range(t):
                        c=input("Ingrese la cadena {} : ".format(i+1))
                        l.append(c)
                    print("\nLa lista ingresada es:",l)
                    li = Cadena(l)
                    print(li.cadenaLista())
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")    
            #? INSERTAR DATO
            elif opc4 == "6":
                try:
                    os.system("cls")
                    print("Insertar Dato")
                    ca=str(input("\nIngresar cadena: ")).capitalize()
                    bus=str(input("Que texto desea ingresar? ")).capitalize()
                    print("\nLas posiciones de caracteres serán desde [0 hasta {}]".format(len(ca)))
                    pos=int(input("En que posición? "))
                    dat= Cadena(ca)
                    print(dat.insertarDato(bus,pos))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except:
                    print("No se Digitó una letra...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")               
            #? ELIMINAR OCURRENCIA
            elif opc4 == "7":
                try:
                    os.system("cls")
                    print("Eliminar Ocurrencia")                    
                    ca=str(input("\nIngresar cadena: ")).lower()
                    bus=str(input("Que ocurrencias desea eliminar? ")).lower()
                    dat= Cadena(ca)
                    print(dat.eliminarOcurrencias(bus))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except:
                    print("No se Digitó una letra...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")       
            #? RETORNAR VALOR
            elif opc4 == "8":
                try:
                    os.system("cls")
                    print("Retornar Valor")
                    ca=str(input("\nIngresar cadena: ")).lower()
                    print("\nPosición de Carácteres será desde: [0 hasta {}]".format(len(ca)-1))
                    pos=int(input("Que posición de carácter desea retornar y eliminar? ").lower())
                    dat= Cadena(ca)
                    print(dat.retornaValor(pos))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó un número...")
                    input("\nPresione la tecla 'Enter' para regresar al menú anterior...")    
            #? CONCATENAR DATO
            elif opc4 == "9":
                try:
                    os.system("cls")
                    print("Concatenar Dato")
                    ca=str(input("\nIngresar cadena: ")).lower()
                    dato=str(input("Ingresa otra cadena: ")).lower()
                    dat= Cadena(ca)
                    print(dat.concatenarCadena(dato))
                    input("\nPresione la tecla 'Enter' para continuar...")
                except ValueError:
                    print("No se Digitó una letra...")
                    input("\nPresione una tecla para regresar al menú anterior...") 

            #? SALIR
            else:
                 pass

    elif opc == "5":    
        print("\nGracias por usar el programa UwU")
    else:
        print("Opcion no valida v:")