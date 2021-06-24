#3.-Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen, 
# escriba “Aprobado” en caso que esa calificación fuese mayor o igual que 7.

class alumno:
    def calificación(self):
        c = float(input("Ingrese la calificación del examen: "))
        if c >= 7:
            print("Aprobado")

dato = alumno()
dato.calificación()
