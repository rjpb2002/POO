class calificacion:
    def mayor(self):
        n1=float(input("Ingrese la nota del primer examen: "))
        n2=float(input("Ingrese la nota del segundo examen: "))
        if n1 >=80 and n2 >=80:
            print("\nUsted ha sido Aceptado owo")
        else:
            print("\nUsted ha sido Rechazado")

dato= calificacion()
dato.mayor()
