#Ronny Javier Peñaranda Bajaña
#Ingeniería en Software

#EJEMPLO DE UNA CLASE EN PYTHON
class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador
    def show(self):
        print(self.num, "/", self.den)

x = Fraccion(1,2)
y = Fraccion(2,3)
print(x.show())
print(y.show())
print("************************************************************************************************************************")

#VARIABLES DE PYTHON
#Numericos
edad, _peso = 50, 70.5

#String
nombres = 'Daniel Vera'
dirDomiciliaria = "Chile y Guayaquil"
Tipo_sexo = 'M'

#Boolean
civil = True

#Colecciones
usuario = ('dchiki','1234','chiki@gmail.com')
materias = ['Programacion Web','PHP','POO']
docente = {'nombre':'Daniel','edad':50,'fac':'faci'}

#Imprimir
print("""Mi nombre es {}, tengo {} años """.format(nombres,edad))
print(usuario,materias,docente)
print("************************************************************************************************************************")

#ESTRUCTURAS DE CONTROL DE PYTHON - IF
x = int(input("Ingresar un numero entero:"))
if x < 0:
    x = 0
    print('Negativo cambiando a cero')
elif x == 0:
    print('Cero')
elif x == 1:
    print('Uno')
else:
    print('Ninguna opcion')
print("Ok") if type(x) == int else print("-")
print("************************************************************************************************************************")

#ESTRUCTURAS DE CONTROL DE PYTHON - WHILE
#Uso de While infinito(LO DEJÉ COMO COMENTARIO SINO AL CORRER QUEDABA EN EL BUCLE)
#c = 1
#while True:
#    print(c)

#While validacion
vocal = input("Ingrese una vocal: ")
while vocal not in ('a','e','i','o','u'):
    if vocal == '.':
        break
    vocal = input("Vocal: ")
print('Su vocal o punto es: {}'.format(vocal))
print("************************************************************************************************************************")

#ESTRUCTURAS DE CONTROL DE PYTHON - FOR
#For range(v) - range(vi,vf) - range(vi,vf,inc)
frase = input("Ingrese una frase: ")
for indice in range(len(frase)):
    print(indice,'-',frase[indice])

#For in candena - in(tupla) - in[lista]
cvoc= 0
for car in frase:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cvoc = cvoc + 1
print('La cantidad de vocales es de:{}'.format(cvoc))

#Comprehension - [var for var in datos condicion]
[car for car in['a','e','i','o','u']if car not in ('a','i','o')]
print("************************************************************************************************************************")

#FUNCIONES EN PYTHON - DEF
#Funciones sin retorno
def vocales(frase):
    for car in frase:
        if car in('a','e','i','o','u'):
            print(car)

#Llamada de funcion
oracion = input('Ingrese una oracion: ')
vocales(oracion.lower())

#Funcion con retorno de valor
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)

#llamada de funcion
listanotas = [2,4,6,8,10]
prom = promedio(listanotas)
print("\nPromedio: {} = {} ".format(listanotas,prom))
print("************************************************************************************************************************")

#FUNCIONES EN PYTHON - PREDEFINIDAS
#Funciones matematicas
import math
num1, num2, num, men = 12.572, 15.4, 4, '1234'
print(math.ceil(num1)),'\t', math.floor(num1)
print(round(num1,1),'\t', type(num),'\t', type(men))

#Funciones de cadenas
mensaje = 'Hola' + 'mundo' + 'Python'
men1 = mensaje.split()
men2 = ''.join(men1)
print()
print(mensaje[0], mensaje[0:4], men1, men2)
print(mensaje.find("mundo"), mensaje.lower())
print()

#Funciones de Fecha
from datetime import datetime,timedelta, date
hoy,fdia = datetime.now(), date.today()
futuro = hoy + timedelta(days=30)
dif,aa,mm,dd = futuro - hoy, hoy.year, hoy.month, hoy.day
fecha = date(aa,mm,dd+2)
print(hoy,fdia,futuro,dif,fecha)
print("************************************************************************************************************************")