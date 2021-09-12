#RONNY JAVIER PEÑARANDA BAJAÑA
#!UT4
class UT4:
        def __init__(self):
            pass

        def valor_aritmetica(self):
            v1=27 % 4 + 15 / 4
            v2=37 /4 + 4 + (-7)
            v3=9 + 2 / 3 * 25 * 3
            v4=(7 * 3 - 4) - 45
            return v1,v2,v3,v4

        def resul_relacionales(self):
            v1=(27 % 4) + 15 / 4 <= 7 + (-7) 
            v2=9 + (2/3) > 3 * (25*-3)
            v3=(7 * 3 % 45) - 45 != 2/3 
            v4= "a" < "z"
            v5= "Juan" == "Juan"
            return v1,v2,v3,v4,v5

        def expresiones_logicas(self):
            v1= 25 <= 7 and not (7 >= 2)
            v2= not ("Juan_" < "pepe" and (37 < 4 + (-7))) or ("3" < "z")
            v3= 24 < 5 and 10 >= 10 or 10 == 5
            v4= (not (6 / 3 > 3)or 7) <  7 and (3 >= 9 / 2 or 2 + 3 <= 7 / 2)

            return v1,v2,v3,v4
        
        def evaluar_aritmeticas(self):
            v1= 6 - 3 * 4 / 4 + 5 * 2
            v2= (2 * 3 + (6 // 3 - 1)**2)
            v3= 6 % 3 - 9 / 4 * 2 + 1

            return v1,v2,v3
        
        def insertar(self):
            pass
            #((a // b) * (c % e)) - (f * g)
            #a - (b * (c / d)) + (e * f)
            #a * (b + c) + abs(d * e / f) - (g * (h + i / j)) 


        def eliminar(self):
            pass
            #((a % b) / c) * d + e
            #(a / b) * c – d
            # a + (b * (c + d )) – (( e + f ) / g * h)

        def condicionales(self):
            v1=(5 / 2 * 3 - 1) == 4 // 2 % 2
            v2=(7 // 3) > (3 / 4) ** 2 * (2 + 10 % 5)
            v3=10 <= 3 + 4 - 2
            return v1,v2,v3
        
        def ex_ari_rel_log(self):
            v1= not ( 15 >= 7 ** 2) or (43 - 8 * 2 // 4 != 3 * 2 // 2)
            v2= (15 >= 7 * 3 ** 2 and 8 > 3 and 15 > 6) or not ( 7 * 3 < 5 + 12 * 2 // 3 ** 2)
            v3= not (( 7 * 3 // 2 * 4 < 20) or (15 / 2 * 6 <= 15 * 2 / 17 )) 
            return v1,v2,v3

# dato= UT4()
# print(dato.valor_aritmetica())
# dato= UT4()
# print(dato.resul_relacionales())
# dato= UT4()
# print(dato.expresiones_logicas())
# dato= UT4()
# print(dato.evaluar_aritmeticas())
# dato= UT4()
# print(dato.condicionales())
# dato= UT4()
# print(dato.ex_ari_rel_log())

#!UT5
class UT5:
    def __init__(self):
        pass
    
    def ejemplo1(self):
        #1. Leer un número y mostrar por la salida estándar si dicho número es o no es par.
        num=int(input("Ingresar número: "))
        if num%2 == 0:
            print("El número {} es par".format(num))
        else:
            print("El número {} es impar".format(num))

    def ejemplo2(self):
        #2. Leer 2 números y mostrar el producto de ellos.
        n1=int(input("Ingresar número: "))
        n2=int(input("Ingresar número: "))
        mul=n1*n2
        print("El producto de {} * {} = {}".format(n1,n2,mul))

    def ejemplo3(self):
        #3. Leer 2 números y determinar el mayor de ellos.
        n1=int(input("Ingresar número: "))
        n2=int(input("Ingresar número: "))
        if n1 > n2:
            print("El número {} es mayor.".format(n1))
        else:
            print("El número {} es mayor.".format(n2))

    def ejemplo4(self):
        #4. Leer 3 números y mostrar el mayor de ellos.
        n1=int(input("Ingresar número 1: "))
        n2=int(input("Ingresar número 2: "))
        n3=int(input("Ingresar número 3: "))
        if n1 > n2 and n1 > n3:
            print("El número {} es mayor.".format(n1))
        elif n2 > n1 and n2 > n3:
            print("El número {} es mayor.".format(n2))
        else:
            print("El número {} es mayor.".format(n3))

    def ejemplo5(self):
        #5. Leer un número y mostrar su tabla de multiplicar.
        num=int(input("Ingresar número: "))
        for i in range(1,13):
            t=num*i
            print("{} * {} = {}".format(num,i,t))
    
    def ejemplo6(self):
        #6. Leer una secuencia de 30 números y mostrar la suma y el producto de ellos.
        suma=0
        prod=1
        for i in range(1,31):
            suma=suma+i
            prod=prod*i

        print("La suma total {}".format(suma))
        print("El producto total {}".format(prod))


# dato1=UT5()
# dato1.ejemplo1()
# dato1=UT5()
# dato1.ejemplo2()
# dato1=UT5()
# dato1.ejemplo3()
# dato1=UT5()
# dato1.ejemplo4()
# dato1=UT5()
# dato1.ejemplo5()
# dato1=UT5()
# dato1.ejemplo6()
