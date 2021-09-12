archivo, f = 'dato.txt',""
docentes = [{'nombre':'Ronny','edad':19,'fac':'Ingenieria'},
{'nombre':'Teffy','edad':22,'fac':'Salud'},
{'nombre':'Belu','edad':22,'fac':'Administrativo'}]

#Escribir archivo: w - a: write - writeline
with open(archivo,'w') as writer:
    for i in range(len(docentes)):
        linea=''
        for clave, valor in docentes[i].items():
            if clave == 'fac':
                linea = linea + (str(valor) if type(valor) == int else valor) + ""
            else:
                linea = linea + (str(valor) if type(valor) == int else valor) + ""
        writer.writelines(linea)

#Leer archivo: r: read - readline : realines - in 
try:
    f=open(archivo,"r")
    for linea in f:
        print(linea[:-1])
except Exception as e:
    print('Error de archivo: '+str(e))
finally:
    f.close()
