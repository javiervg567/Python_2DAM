#Escriba un programa que lea un valor correspondiente a una distancia en millas marinas y
#escriba la distancia en metros. Sabiendo que una milla marina equivale a 1.852 metros.
try:
    millas_marinas = float(input("Introduce la distancia en millas marinas: "))
    if millas_marinas < 0:
        print("La distancia no puede ser negativa.")
    else:
        metros = millas_marinas * 1.852
        print(f"La distancia en metros es: {metros:.6f}")
except ValueError:
    print("Introduce un número válido.")