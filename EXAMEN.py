#EJERCICIOS EXAMEN  - RONNY PEÑARANDA BAJAÑA

#?Dado el siguiente método fin_encontrar() de la clase Cadena.
#?El método tiene que retornar la posición de un caracter buscado en la cadena. 
#?indique que linea o lineas estan con error y que hacen que el método no funcione correctamente.

# class Cadena():
    
#     def __init__(self,cadena):
#         self.cadena = cadena
#         self.__listMin = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
#         self.__listMayus =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#     def fin_encontrar(self,buscar):
#         for i, v in enumerate(self.cadena):
#             if v == buscar:
#                 return i
#         return -1

# cadena = input("Ingrese una cadena: ")
# dato= Cadena(cadena)
# buscar = input("Que valor desea buscar? ")
# print(dato.fin_encontrar(buscar))


#?Dado el siguiente método invertirCadena() de la clase Examen.
#?El método recibe como parametro una cadena. 
#?El método tiene que retornar la cadena recibida como parametro de manera invertida. 
#?indique que linea o lineas estan con error y que hacen que el método no funcione correctamente.

# class Examen:

#     def __init__(self,lista=[]):
#         self.lista=lista
    
#     def invertirCadena(self,cadena):
#         invertida = ""
#         cont = len(cadena)
#         indice = -1
#         while cont >= 1:
#             invertida += cadena[indice]
#             indice = indice - 1
#             cont -=1
#         return invertida
# dato = Examen()
# print(dato.invertirCadena("ronny"))
# respuesta= "ynnor"

#?Dado el siguiente método decimalBinario() de la clase Ejercicios.
#?El método tiene que retornar un numero binario a partir de un numero decimal. 
#?indique que linea o lineas estan con error y que hacen que el método no funcione correctamente.

# class Ejercicios:
#     def decimalBinario(self,decimal):
#         binario = " "
#         while decimal // 2 != 0:
#             binario = str(decimal%2)+binario
#             decimal = decimal // 2
#         return str(decimal) + binario

# ejer = Ejercicios()
# print(ejer.decimalBinario(5))
# respuesta= 101


#?El siguiente código guarda en un diccionario en la clave "pares" 
#?una lista de numeros pares y en la clave impares guarda en una lista los numeros impares.

# class Calculos:
#     def __init__(self,numero):
#         self.numero=numero
    
#     def paresEimpares(self):
#         dicc = {"pares":[],"impares":[]}
#         for num in range(self.numero):
#             if num % 2 == 0:
#                 dicc["pares"].append(num)
#             else:
#                 dicc["impares"].append(num)
#         return dicc
    
# n=int(input("Escribir la cantidad de números: "))
# dato = Calculos(n)
# print(dato.paresEimpares())


#?El siguiente método realiza el calculo de un numero factorial:
#?El factorial de un numero resulta de multiplo todos los números enteros que hay entre ese número y el 1.
#?Ejemplo= 4! = 4*3*2*1=24

# def fact_1(n):
#     factorial_total = 1
#     while n > 1:
#         factorial_total *= n
#         n -= 1
#     return factorial_total

# print(fact_1(6))


#?Dado el método insertarPos() de la clase Ordenar
#?El método tiene que insertar un valor en la posicion indicada.
#?indique que linea o lineas estan con error y que hacen que el método no funcione correctamente.

# class Ordenar:

#     def __init__(self,lista):
#         self.lista = lista

#     def insertarPos(self,pos,valor):
#         auxlista=[]
#         if len(self.lista) <= pos:
#             self.lista.append(valor)
#         else:
#             for indice,ele in enumerate(self.lista):
#                 if indice == pos:
#                     auxlista.append(valor)
#                 auxlista.append(ele)
#             self.lista = auxlista       
#         return self.lista

# dato= Ordenar([1,2,3,4])
# print(dato.insertarPos(4,5))


#?Dado el siguiente método ListaMenor() de la clase Examen
#?El método tiene que retornar una lista de todos los números menores a un número que se recibe
#?como parametro.   

# class Examen:
#     def __init__(self,lista=[]):
#         self.lista = lista

#     def ListaMenor(self,num):
#         listaMenor=[]
#         for menor in self.lista:
#             if menor < num:
#                 listaMenor.append(menor)
#         return listaMenor


# exa = Examen([2,5,20,16])
# print(exa.ListaMenor(13))  
# respuesta = [2, 5]


#?Dado el siguiente método listaMultiplo() de la clase Examen
#?El método recibe como parametro un número. El método tiene que retornar una lista de todos
#?los elementos del atributo lista de la clase que son multiplos del parametro numero del método.
#?indique que linea o lineas estan con error y que hacen que el método no funcione correctamente.

# class Examen:
#     def __init__(self,lista=[]):
#         self.lista=lista

#     def listaMultiplo(self,numero):
#         lista=[]
#         for num in self.lista:
#             if not(num % numero !=0):
#                 lista.append(num)
#         return lista

# exa = Examen([2,5,8,10,20])
# print(exa.listaMultiplo(5))
# respuesta=[5,10,20]

#?El siguiente código comprueba si un número es abundante ingresado es un numero abundante:
#?Se dice que un numero es abundante, cuando la suma de sus divisores incluidos  el 1 y excluidos
#?el propio numero es mayor que el.


# def numero_Abundante(n):
#     count=1
#     suma= 0
#     while (count<n):
#         if (n% count ==0):
#             suma+= count
#         count = count + 1
#     if (suma > (n)):
#         return True
#     else:
#         return False

# print(numero_Abundante(12))


#?El siguiente código verifica si una frase es palindroma. Una frase es palindroma si se lee de
#?igual forma de derecha a izquierda como de izquierda a derecha. Ejemplo: anita lava la tina
#?indique que linea o lineas estan con error y que hacen que el método no funcione correctamente.

# class Cadena:
#     def __init__(self,cad=""):
#         self.__cadena = cad
    
#     def palindroma(self):
#         invertir = self.__cadena[::-1]
#         invertir = invertir.replace(" ","")
#         original = self.__cadena.replace(" ","")
#         if original.lower() == invertir.lower():
#             return "Palindroma"
#         else:
#             return "No es palindroma"
    

# ca = Cadena("anita lava la tina")
# print(ca.palindroma())


#?Dado el siguiente método obtenerVuelto() de la clase Vuelto
#?El método tiene que calcular el vuelto restante el pago-costo y luego este vuelto lo retornará
#?en una lista donde cada elemento será un diccionario donde la clave será la cantidad de billetes
#?y el valor el tipo de nominación del billete mayor a menor numeración.

# class Vuelto:
#     def __init__(self,costo,pago):
#         self.__costo = costo
#         self.__pago = pago
#         self.__billetes = [50,20,10,5,1]
    
#     def obtenerVuelto(self):
#         vuelto = self.__pago - self.__costo
#         vueltos=[]
#         for moneda in self.__billetes:
#             if vuelto >= moneda:
#                 billete= vuelto//moneda
#                 vuelto = vuelto % moneda
#                 vueltos.append({billete:moneda})
#         return vueltos

    
# vue = Vuelto(53,100)
# print(vue.obtenerVuelto())
# respuesta= [{2: 20}, {1: 5}, {2: 1}] 

