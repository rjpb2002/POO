 #7.Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras 
 # trabajadas en una empresa, sabiendo que cuando las horas de trabajo exceden de 40, 
 # el resto  se consideran horas extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8;  
 # si las horas extras exceden de 8 se pagan las primeras 8 al  doble de lo que se paga por una hora normal 
 # y el resto al triple.

class trabajador:
    def dinero(self):
        horas = int(input("Ingrese las horas trabajadas: "))
        pago = float(input("Ingrese el pago por hora: $"))
        if horas > 40:
            extras = horas - 40
            if extras > 8:
                excedido = extras - 8
                pagoExtras = pago * 2 * 8 + pago * 3 * excedido
            else:
                pagoExtras = pago * 2 * extras
            pagoTrabajador = pago * 40 + pagoExtras
        else:
            pagoTrabajador = pago + horas

        print("El pago total de las horas trabajadas será de: ${:.2f}".format(pagoTrabajador))      

dato = trabajador()
dato.dinero()

