#4.-Dado como dato la calificación de un alumno en un examen, escriba “aprobado” 
# si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.

class alumno:
    def calificación(self):
        c = float(input("Ingrese la calificación del examen: "))
        if c >= 7:
            print("Aprobado")
        else:
            print("Reprobado")

dato = alumno()
dato.calificación()