class Cargo:
    secuencia=0 
    def __init__(self,des="Sin cargo"):
        Cargo.secuencia = Cargo.secuencia + 1
        self.codigo = Cargo.secuencia
        self.descripcion = des
if __name__=="_main__":
    #!Caso1
    cargo1 = Cargo()
    print(cargo1.codigo,cargo1.descripcion)
    #!Caso2
    cargo2 = Cargo()
    cargo2.descripcion = "Director"
    print(cargo2.codigo,cargo2.descripcion)
    #!Caso3
    cargo3 = Cargo("Analiste")
    print(cargo3.codigo,cargo3.descripcion)
    #print(Cargo.secuencia)
    #print(cargo1.secuencia)
    #print(cargo2.secuencia)
    #print(cargo3.secuencia)