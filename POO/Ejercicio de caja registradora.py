def cajero():
    print("***************************************************************************************")
    print("La siguiente es la lista de códigos de productos a introducir para calcular la compra")
    print("***************************************************************************************")
    print("galletitas_dulces = 9456 // costo = 50\ngalletitas_saladas = 9545 // costo = 45\nyerba = 9555 // costo = 55\ntomate = 8554 // costo = 80\nlechuga = 8445 // costo = 50\ncarne = 7885 // costo = 150\nleche = 6859 // costo = 60\nyogur = 6857 // costo = 85")
    print("***************************************************************************************")
    print("Por favor indique los productos a añadir a la lista de compra. Una vez que haya\n terminado indique 'Fin'")
    print("***************************************************************************************")

    precios = {"9456": 50, "9545": 45, "9555": 55, "8554": 80, "8445": 50, "7885": 150, "6859": 60, "6857": 85}

    subtotal = []
    total = []

    compra = input("Por favor introduzca el código: ")
    while compra != "Fin":
        if compra in precios:
            subtotal.append(compra)
            print(f"Su carrito contiene {subtotal}")
            compra = input("Producto añadido al carrito. ¿Desea comprar algo más? Para salir indique 'Fin': ").title()
        else:
            compra =  input("Por favor solo indique los códigos válidos o 'Fin' para salir: ").title()


    for items in subtotal:
        total.append(precios[items])
    total_a_pagar = sum(total)
    print("Su total a pagar es de: ", total_a_pagar)

    descuento = str(input("¿Posee tarjeta de descuentos? Indique 'Silver', 'Platinum' o 'No': ")).title()
    while descuento != "No":
        if descuento == "Silver":
            total_a_pagar = total_a_pagar - ((total_a_pagar * 5)/100)
            print("Por su categoría Silver se ha hecho un descuento del 5%, el total a pagar es:", total_a_pagar)
            break
        elif descuento == "Platinum":
            total_a_pagar = total_a_pagar - ((total_a_pagar * 10) / 100)
            print("Por su categoría Platinum se ha hecho un descuento del 10%, el total a pagar es:", total_a_pagar)
            break
        else:
            print("Su total a pagar es: ", total_a_pagar)
            break

    pago = int(input("Indique la cantidad de dinero con que se realiza el pago: "))
    while pago < total_a_pagar:
        pago = int(input("No es suficiente dinero, por favor ingrese un total superior o igual a su compra: "))
    vuelto = pago - total_a_pagar
    print("Su pago fue de", pago, "por una compra total de", total_a_pagar, ". Su vuelto es: ", vuelto)
    print("Muchas gracias por su compra")

cajero()

def nueva_compra():
    pregunta = input("¿Desea realizar una nueva compra? Indique 'S/N': ").upper()
    if pregunta == "S":
        cajero()
    else:
        print("Muchas gracias, por utilizar este código para el curso de Python de la Universidad Austral")

nueva_compra()
