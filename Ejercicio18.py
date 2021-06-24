#18.-Sea un vector “Calificaciones” de 100 componentes:
class vector:
    def Calificaciones(self):
          calificaciones=[]
          j= 0
          c=1
          for i in range(100):
            calificaciones.append(i)
            j=j+1
          print("")
          for i in range (j):
            print("La calificación {}".format(calificaciones[i]+1))
            c=c+1

dato = vector()
dato.Calificaciones()



