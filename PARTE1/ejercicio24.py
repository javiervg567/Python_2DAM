#Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
#de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
#Visualizar el descuento y el total a pagar por la compra.
try:
    total_compra = float(input("Ingrese el total de la compra: "))
    dia_semana = input("Ingrese el día de la semana: ").strip().lower()
    
    if dia_semana in ["martes", "jueves"]:
        descuento = total_compra * 0.15
        total_a_pagar = total_compra - descuento
        print(f"Descuento aplicado: ${descuento:.2f}")
    else:
        descuento = 0
        total_a_pagar = total_compra
        print("No hay descuento aplicado.")
    
    print(f"Total a pagar: ${total_a_pagar:.2f}")
except ValueError:
    print("Error: Introduce el total de la compra válido.")