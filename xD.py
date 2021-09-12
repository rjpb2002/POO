# def mayuscula(oracion):
#     nueva = oracion.()#1
#     for i,v in enumerate(oracion):
#         if i != 0:#2 
#             if oracion [i-1] == " ":#3
#                 nueva += v.upper()#4
#             else:
#                 nueva += v #5
#     return nueva
# frase = "examen de programacion"
# print(mayuscula(frase))

# respuesta = "Examen De Programacion"   

# class Calculos:
#     def __init__(self,numero):
#         self.numero = numero
    
#     def binarioDecimal(self):
#         decimal= 0 #1
#         for pos, num in enumerate(self.numero[::-1]):#2
#             num=int(num)#3
#             decimal +=(2**pos)*num#4

#         return decimal

# ejer=Calculos("101")
# print(ejer.binarioDecimal())
# def mayuscula(oracion):
#     nueva = oracion[0]
#     for i,v in enumerate(oracion):
#         if i != 0:
#             if oracion[i-1] == " ":
#                 nueva += v.upper()
#             else:
#                 nueva += v
#     return nueva
# frase = "examen de programacion"
# print(mayuscula(frase))



# class Lista:
#     def __init__(self,datos):
#         self.coleccion = datos

#     def diccionario(self):
#         diccionario2 = [] #1
#         for clave, valor in enumerate(self.coleccion):#2
#             diccionario2[clave] = valor#3
#         return diccionario2 #4


# lista= Lista(["a","e","i","o","u"])
# print(lista.diccionario())

# tupla = (2, 4, 6, 8, ('Pares', 12, 14), 16, ('Impares', 20), 7, 9, 10)

# print(tupla[4:8])


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


# class Ordenar:

#     def __init__(self,lista):
#         self.lista = lista

#     def top(self):
#         auxlista=[]
#         for pos in range(1,len(self.lista)):
#             auxlista.append(self.lista[pos])
#         self.lista = auxlista       
#         return self.lista[0]

# op= Ordenar([1,2,3,4])
# print(op.top())


class Ejercicios:
     def decimalBinario(self,decimal):
        binario=""
        while decimal // 2 != 0:
            binario = str(decimal%2) + binario
            decimal = decimal // 2
        return decimal + binario

ejer = Ejercicios()
print(ejer.decimalBinario("5"))
respuesta = 101
