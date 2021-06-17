class For:
    def __init__(self):
        pass

    #!For: ciclo repetitivo de incrementos o decrementos, se ejecuta por verdadero.
    def usoFor(self):
        datos = ["Ronny",19,True]
        numeros = (1,2,3,4,5)
        docente = {"Nombre":"Ronny","Edad":19,"Fac":"Faci"}
        listanotas = [(30,40),[20,40],(50,40)]
        #! Range([inicio=0], limite,[inc/dec=1]). Genera un rango de valores desde un valor inicial a un valor final.
        #* Se ejecuta desde el inicio
        # for i in range(5): #rango[0,1,2,3,4]
        #     print("i = {}".format(i))
    
        # for i in range(2,10): #rango[2,3,4,5,6,7,8,9]
        #     print("i = {}".format(i))
    
        # for i in range(4,10,2): #rango[4,6,8]
        #     print("i = {}".format(i),end="   ")
    
        # for i in range(12,3,-3): #rango[12,9,6]
        #     print("i = {}".format(i),end="   ")
    
        longintud = len(datos)-1
        # print(datos[0])
        # print(datos[1])
        # print(datos[2])
        # j = 0
        # while j < longintud:
        #     print("While",datos[j])
        #     j = j + 1 

        # for i in range(longintud,-1,-1):
        #     print("For",datos[i])

        # for i,dato in enumerate(numeros):
        #     print("For",i,dato)        
        # dato toma cada elemento de la colección(cadena,lista,tupla)
        # for dato in numeros:
        #     print(dato)
        
        # for dato in ["h","o","l","a","que","tal"]:
        #     print(dato)   

        # print("\nDiccionario de notas")
        # for clave,valor in docente.items():
        #     print(clave,":",valor,end="  ")
        
        
        # listaNotas = [(30,40),[20,40,20],(50,40,20,10)]
        # acum = 0
        # long = 0
    
        # for notas in listaNotas: 
        #     acum2 = 0

        #     for nota in notas:  
        #         print(nota)
        #         long= long + 1
        #         acum = acum + nota
        #         acum2 += nota
        #     promParcial = acum2/len(notas)
        #     print("Notas parciales : {}  -  Promedio Parcial: {} ".format(acum2,promParcial))

        # prom = acum / long
        # print("El total de notas es de: {}   -   Número de notas: {}   -   El promedio es: {} ".format(acum,long,prom))
        # listaalumnos = [{"Nombre":"Ronny","Final":70},{"Nombre":"Teffy","Final":60},{"Nombre":"Javier","Final":90}]
        # acumAlum = 0
        # contAlum = 0 
        # for alumnos in listaalumnos:
        #     print("\n",alumnos)
            
        #     for clave,valor in alumnos.items():
        #         print(clave,":",valor,end = "\n ")
            
        #         if clave == "Final":acumAlum = acumAlum + valor
        #     contAlum += 1    
        # print("\nPromemdio General",acumAlum/contAlum)
        
        #!METODO 1
        frase = "Hola que haces"
        # vocales = []
        # for car in frase:
        #     if car in ("a","e","i","o","u"):
        #         vocales.append(car)
        # print(vocales)

        #!METODO 2
        print( [car for car in frase if car in ("a","e","i","o","u")])

bucle1 = For() 
bucle1.usoFor()
