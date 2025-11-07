#Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre
#el porcentaje de descuento realizado.
try:
    precio_articulo = float(input("Introduce el precio del artículo: "))
    precio_venta = float(input("Introduce el precio de venta real: "))
    if precio_articulo < 0 or precio_venta < 0:
        print("Los precios no pueden ser negativos.")
    elif precio_venta > precio_articulo:
        print("El precio de venta no puede ser mayor que el precio del artículo.")
    else:
        descuento = ((precio_articulo - precio_venta) / precio_articulo) * 100
        print(f"El porcentaje de descuento realizado es: {descuento:.2f}%")
except ValueError:
    print("Introduce números.")