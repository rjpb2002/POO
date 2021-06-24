#15.-Determinar si un número entero proporcionado por el usuario es primo. 
# Un número primo es un entero que no tiene más divisores que él mismo y la unidad.

class numero:
    def primo(self):
        prim = "V"
        div = 2
        n = int(input("Ingrese un número entero: "))
        while div < n and prim == "V":
            r = n % div
            if r == 0:
                prim = "F"
            div = div + 1
        if prim == "V":
            print("El número {} es primo".format(n))
        else:
            print("El número {} no es primo".format(n))

dato = numero() 
dato.primo()    
    
