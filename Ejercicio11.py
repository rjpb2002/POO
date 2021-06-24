#11.-Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.

class suma:
    def cuadrados(self):
        sum = 0
        for enteros in range(1,100):
            sum = sum + enteros*enteros
        print("La suma total de los primeros 100 enteros es: {}".format(sum))

dato = suma()
dato.cuadrados()
