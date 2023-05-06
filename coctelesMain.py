from Cocteles import Cocteles

precioTotal=0
descuento =0
tipoCoctel= int(input("Que tipo de cotel desea, 1 de frutas, 2 shot: "))
if(tipoCoctel):
    coctel = Cocteles()
    if (tipoCoctel == 1):
        coctel.tipoCoctel=("Coctel de frutas")
        coctel.nombre = input("Digita el nombre del coctel: ")
        coctel.precio = int(input("Digita el precio del coctel: "))
        coctel.gradosAlcohol = input("Digita el grado de alcohol: ")
        coctel.cantidad = int(input("Digita cantidad: "))
        coctel.añejamiento = int(input("Digita cuantos dias tiene de añejamiento: "))
        if (coctel.añejamiento == 1):
            precioTotal = coctel.cantidad * coctel.precio
            print(f"El Total es de: {precioTotal}")
        elif (coctel.añejamiento == 2):
            precioTotal = (coctel.cantidad * coctel.precio)
            descuento = (coctel.cantidad * coctel.precio) * 0.2
            print(f"El Total es de: {precioTotal - descuento}")
        elif (coctel.añejamiento == 3):
            precioTotal = (coctel.cantidad * coctel.precio)
            descuento = precioTotal * 0.5
            print(f"El Total es de: {precioTotal - descuento}")
        elif ( coctel.añejamiento > 3):
            
            print("No se puede vender el trago")
        else:
            print("Digita numero valido")
    elif (tipoCoctel == 2):
       coctel.tipoCoctel=("Shot")
       coctel.nombre=input("Digita el nombre del shot: ")
       coctel.precio=int(input("Digita el precio del shot: "))
       coctel.gradosAlcohol=input("Digita el grado de alcohol: ")
       coctel.cantidad=int(input("Digita canrtidad: "))
       precioTotal = coctel.precio * coctel.cantidad 
       print(f"EL costo total es de {precioTotal}")


