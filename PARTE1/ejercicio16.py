#Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene
try:
    numero = int(input("Introduzca un número entre 0 y 99999: "))
    
    if 0 <= numero <= 99999:
        if numero < 10:
            cifras = 1
        elif numero < 100:
            cifras = 2
        elif numero < 1000:
            cifras = 3
        elif numero < 10000:
            cifras = 4
        else:
            cifras = 5
        
        print(f"El número {numero} tiene {cifras} cifra(s).")
    else:
        print("Error: El número tiene que estar entre 0 y 99999.")
except ValueError:
    print("Error: Ingresa un número válido.")