#16.-Sea un vector “Calificaciones” de 100 componentes:
class vector:
    def Calificaciones(self):
          calificaciones=[]
          j= 0
          c=1
          for i in range(0,100,1):
            cal=float(input("Escriba la calificación: "))
            calificaciones.append(cal)
            j=j+1
          print("")
          for i in range (0,j,1):
            print("La calificación {} es {:.2f}".format(c,calificaciones[i]))
            c=c+1

dato = vector()
dato.Calificaciones() 




