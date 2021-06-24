#11.-Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, 
# utilizando un bucle controlado por el usuario.

class calcular:
    def sp(self):
        sum = 0
        produc = 1
        res = input("Desea realizar el calculo de suma y el producto?S/N): ")
        while res != "N" and res != "n":
            nu = int(input("Ingrese número: "))
            sum = sum + nu
            produc = produc * nu
            res=input("Desea continuar con el calculo?(S/N): ")
        print("\nLa suma total del calculo es: {}".format(sum))
        print("El producto total del calculo es: {}".format(produc))

dato = calcular()
dato.sp()
