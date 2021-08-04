from Numeros import Intermedio
class Lista(Intermedio):
    def __init__(self, lista= []):
        self.lis = lista 

    def presentarLista(self):
        for z in self.lis:
            print (z)
            
    def buscarLista(self,valor):
        bl= [i for i, x in enumerate(self.lis) if x ==valor]

        if valor in self.lis:
            print("El valor '{}' se encontró en la posición '{}'".format(valor,bl)) 

        if valor not in self.lis:
            print("El valor no se encuentra")

    def listaFactorial(self):
        lf=[]
        for i in self.lis:
            dato= Intermedio(i)
            f=dato.factorial()
            lf.append(f)
        return "El resultado será: {}".format(lf)

    def listaPrimo(self):
        lf=[]
        for i in self.lis:
            dato= Intermedio(i)
            p=dato.primo()
            lf.append(p)
        return "El resultado será: {}".format(lf)

    def listaNotas(self,listaNotasDiccionario):
        i=1
        for key in listaNotasDiccionario.keys():
            print("\nAlumno {}) Nombre: {}".format(i,key),end=" / ")
            i += 1
            j=1
            for nota in listaNotasDiccionario[key]:
                print("Nota {}: {}".format(j,nota),end=" / ")
                j +=1
            print(" ")

    def insertarLista(self,valor,posicion):
        try:
            if posicion <= len(self.lis):
                lista=[]+self.lis       
                lista.insert(posicion,valor)
            return "\nLa nueva lista será: {}".format(lista)
        except:
            return "La posición no existe."


    def eliminarLista(self,valor):
        try:
            lista=[]+self.lis
            c=lista.count(valor)
            for i in range(c):
                lista.remove(valor) 
            return "La lista será: {}".format(lista)
        except:
            return "No existe valor."   


    def retornaValorLista(self,posicion):
        try:
            if posicion <= (len(self.lis)-1):
                lista=[]+self.lis
                l=lista.pop(posicion)
            print("\nEl valor retornado es: {}".format(l))
            return "La nueva lista será: {}".format(lista)
        except:
            return "La posición no existe."


    def copiarTuplaLista(self,tupla):
        try:
            tuplas=()+tupla
            lista=list(tuplas)

            return "La lista será: {}".format(lista)
        except:
            return "No existe."
    
    def vueltoLista(self,listaClientesDiccionario):
        i=1
        for key in listaClientesDiccionario.keys():
            print("\nCliente {}) Nombre: {}".format(i,key),end=" / ")
            i += 1
            for nota in listaClientesDiccionario[key]:
                print("Vuelto: ${}".format(nota),end=" / ")
            print(" ")

