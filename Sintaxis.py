

class Sintaxis:
    instancia = 0 #variables de clases (opcional)
    #__init__ metodo-constructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
    #e inicializar los atributos de la clase. self es un objeto que representa la clase creada

    def __init__(self, dato ='Inicializacion'):
        self.frase = dato #variables de instancia
        #Sintaxis.instancia = Sintaxis.instancia+1


    def usoVariables(self):
        edad,_peso = 19, 74
        nombres = 'Ronny Peñaranda'
        Tipo_sexo = 'M'
        civil = True
        print(nombres,edad)
print("************************************************************************************************************************")
#Tuplas = () son colecciones de datos de cualquier tipo inmutables
usuario = ()
usuario = ("rjpb",2002,"rjpb2002@gmail.com")
#usario[3]="Naranjito"
materias = []
materias = ["Programacion Web","PHP","POO"]
materias[1] ="Python"
materias.append("GO")

#Diccionarios = {} colecciones de objetos clave: valor tipo json
docente = {}
docente = {"Nombre":"Ronny","Edad": 50,"Fac":"Faci"}
docente["carrera"] = "CS"
#Presentacion con format
#print("""Mi nombre es {}, tengo {} añps""".format(nombres,edad))
#print(usuario,materias,docente)
#print(usuario,usuario[0],usuario[0:2],usuario[-1])
#print(materias,materias[2:],materias[:3],materias[:],materias[-2:])
print(docente,docente["Nombre"])

ejer1 = Sintaxis() #Se crea un objeto que es una instancia de la clase
print("************************************************************************************************************************")
ejer1.usoVariables()
print("************************************************************************************************************************")
print(ejer1.frase)
print("************************************************************************************************************************")
