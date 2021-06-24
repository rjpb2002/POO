#12.-Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, 
# utilizando un bucle controlado por centinela.

class calcular:
    def sp(self):
        sum = 0
        produc = 1
        nu = int(input("Ingrese un número diferente a -1 : "))
        while nu != -1:
            sum = sum + nu
            produc = produc * nu
            nu = int(input("Ingrese un número( Si desea salir ingrese -1): "))
        print("\nLa suma total del calculo es: {}".format(sum))
        print("El producto total del calculo es: {}".format(produc))

dato = calcular()
dato.sp()