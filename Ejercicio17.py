#17.-Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros 
# y a continuación escribir en un vector A todos los números negativos 
# y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores.
class vector:
    def calificaciones(self):
        A=[]
        B=[]
        j=0
        k=0
        num=[]

        for i in range (0,20,1):
            n=int(input("Ingrese un número entero:"))
            num.append(n)
            if num[i] < 0:
                A.insert(j,num[i])                
                j = j + 1

            else:
                B.insert(k,num[i])
                k = k + 1

        print("")   
        for i in range(0,j,1):
              print("El vector A tiene el valor de {}".format(A[i]))
        print("")   
        for i in range (0,k,1):
              print("El vector B tiene el valor de {}".format(B[i]))
         
dato = vector()
dato.calificaciones()