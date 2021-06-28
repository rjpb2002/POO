#10.-Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2.
#El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado
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
