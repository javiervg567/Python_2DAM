#Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
#el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
#se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
#según sea el caso y el total a pagar de la compra
try:
    valor_compra = float(input("Ingrese el valor de compra: "))
    metodo_pago = input("Ingrese el método de pago (efectivo/tarjeta): ").strip().lower()
    
    if metodo_pago == "efectivo":
        descuento = valor_compra * 0.05
        total_a_pagar = valor_compra - descuento
        print(f"Descuento aplicado: ${descuento:.2f}")
    elif metodo_pago == "tarjeta":
        recargo = valor_compra * 0.03
        total_a_pagar = valor_compra + recargo
        print(f"Recargo aplicado: ${recargo:.2f}")
    else:
        print("Error: Método de pago no válido. Use 'efectivo' o 'tarjeta'.")
        raise SystemExit(1)
    
    print(f"Total a pagar: ${total_a_pagar:.2f}")
except ValueError:
    print("Error: Introduce un valor de compra válido.")