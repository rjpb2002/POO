class Ordenar:
    def __init__(self,lista):
        self.lista = lista
        
    def borbuja(self):
        for i in range(len(self.lista)):
            for j in range(i+1,len(self.lista)):
                if self.lista[i] > self.lista[j]:
                    aux = self.lista[i]
                    self.lista[i] = self.lista[j]
                    self.lista[j] = aux

    def insertar(self,valor):
        self.borbuja()
        auxLista = []
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele > valor:
                auxLista.append(valor)
                enc=True
                break 
            
        if enc: self.lista = self.lista[0:pos] + auxLista + self.lista[pos:]
        else: self.lista.append(valor)   
        return self.lista
    
    def insertar2(self,valor):
        self.borbuja()
        auxLista = []
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele > valor:
                    enc=True
                    break 
            
        if enc:
            for i in range(pos):
                auxLista.append(self.lista[i])
            auxLista.append(valor)
            for j in range(pos,len(self.lista)):
                auxLista.append(self.lista[j])
            self.lista = auxLista
        else:
            self.lista.append(valor)   
        return self.lista

ord1 = Ordenar([10, 15, 20, 60, 80])
print(ord1.insertar(50))

ord2 = Ordenar([5, 6, 7, 8, 9])
print(ord2.insertar2(10))

# ord1.borbuja()
# print(ord1.lista)
