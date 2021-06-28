#2.-En una tienda se ofrece un descuento del 15% sobre el total de la compra
# y un cliente desea saber cuánto deberá pagar finalmente por su compra.

class descuento:
    def compra(self):
        TotalCompra = float(input("Ingrese el precio total de la compra: $"))
        Des = TotalCompra * 0.15
        TotalPagar = TotalCompra - Des
        print("El precio total a pagar será de: ${:.2f}".format(TotalPagar))

dato = descuento()
dato.compra()
