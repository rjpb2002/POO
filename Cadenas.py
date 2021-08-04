class Cadena:
    def __init__(self, cadena):
        self.cadena = cadena

    def recorrerCadena(self):
        for x in self.cadena:
            print(x)

    def buscarCaracter(self,buscado):
        c=0
        for palabra in self.cadena:
            if buscado in palabra:
                c +=1
        
        if len(buscado) !=  1:
            print("Solo un carácter.")
        else:
            if buscado in self.cadena:
                print("La cantidad de veces que se encontró el carácter '{}' es de: {}".format(buscado,c)) 
        if buscado not in self.cadena:
            print("El carácter no se encuentra.")    

        
    def  listaPosiciones(self,caracter):
        l=[]
        pos=0
        for letra in self.cadena:
            if letra == caracter:
                l.append(pos)
            pos+=1
        if len(caracter) !=  1:
                print("Solo un carácter.")
        else:
            if caracter in self.cadena:
                print("El carácter '{}' se encuentra en la posición: {}".format(caracter,l)) 
        if caracter not in self.cadena:
            print("El carácter no se encuentra.")    

    def listaPalabras(self):
        lp = self.cadena.split()
        
        return "\nLa lista de palabras será: {}".format(lp)

    def cadenaLista(self):
        ca= " ".join(self.cadena)
        return "La cadena de caracteres será: {} ".format(ca)

    def insertarDato(self,buscado,posicion):
        try:
            if posicion <= len(self.cadena):
                iz= self.cadena[:posicion]
                de= self.cadena[posicion:]
            return " ".join("\nLa nueva cadena es: {} {} {}".format(iz,buscado,de).split())

        except:
            return "La posición donde se quiere insertar el texto no existe."
        
    def eliminarOcurrencias(self,buscado):
        self.cadena = "".join( i for i in self.cadena if i not in buscado)

        return "La cadena sin las ocurrencias de '{}' será: {}".format(buscado,self.cadena)

    def retornaValor(self,posicion):
        try:
            if posicion <= len(self.cadena)-1:
                for i in self.cadena[:posicion+1]:
                    d=i
                iz=self.cadena[:posicion]
                de=self.cadena[posicion+1:]
                texto=iz+de
            print("\nEl carácter retornado es: '{}'".format(d))
            return  "La nueva cadena será: {}".format(texto)    
        except:
            return "La posición donde se quiere retonar el carácter no existe."

    def concatenarCadena(self,dato):
        return "La cadena concatenada será: {} {}".format(self.cadena,dato)