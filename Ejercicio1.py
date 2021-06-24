#1.-En ejemplos anteriores, 
# diseñamos un pseudocódigo para encontrar la superficie de un círculo para un radio cualquiera.
class Circulo:
    def superficie(self):
        pi= 3.1416
        r=float(input("Ingresa el radio del circulo: "))
        A=pi*r**2
        print("La superficie del circulo es: {:.2f}".format(A))

dato= Circulo()
dato.superficie()