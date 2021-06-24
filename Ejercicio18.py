#18.-Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos. Los datos sobre estos exámenes se proporcionan de la siguiente manera:
# Cal1,1 Cal1,2 ............ Cal1,6
# Cal2,1 Cal2,2 ............ Cal2,6
# .......................
# Cal30,1 Cal30,2 ........ Cal30,6

# Donde Cali,j es una variable real que expresa la calificación que obtuvo el alumno i en el examen j. 
#   1 £ i £ 30, 1£ j £ 6

# Calcular lo siguiente:

# a)    el promedio de calificaciones de cada uno de los 6 exámenes
# b)    el promedio de cada alumno
# c)    el tipo (número) de examen que tuvo el mayor promedio de calificación. Escriba también dicho promedio
class Arreglo:  
    def Dosdimensiones(self):
        Cal=[]
        promE=[]
        for f in range(3):
            Cal.append([])
            for c in range(3):
                Cal[f].append(None)
                Cal[f][c] = float(input("Ingresar calificacion que obtuvo el alumno {} en el examen {}: ".format(f+1,c+1)))
        
        print("")
        for f in range(3):
            for c in range(3):
                print(Cal[f][c],end=" ")
            print() 
        
        print("")
        #!Cálculo del promedio de calificaciones de cada uno de los exámenes
        for c in range(3):
            sum=0
            
            for f in range(3):
                sum=sum + Cal[f][c]
            promE.append(sum/len(Cal))
            print("El promedio del examen {} : {:.2f}".format(c+1,sum/len(Cal)))

        print("")
        #!cálculo del promedio de cada alumno
        for f in range(3):
            sum=0
            for c in range(3):
                sum=sum + Cal[f][c]
            print("El promedio del alumno {} : {:.2f}".format(f+1,sum/len(Cal)))

        print("")
        #!cálculo del tipo de examen que tuvo el mayor promedio de calificación.
        exam=0
        pmayor= promE[1]
        for c in range(3):    
            if pmayor < promE[c]:
                pmayor = promE[c]
                exam=c

        print("El examen {} obtuvo el mayor promedio siendo este: {}".format(exam+1,pmayor))



dato= Arreglo()
dato.Dosdimensiones()
