#Escriba un programa que pida la edad por teclado y nos muestra el mensaje de “Eres mayor
#de edad”, si y solamente si lo somos.
try:
    edad = int(input("Introduce tu edad: "))
except ValueError:
    print("Edad no válida")
else:
    if edad >= 18:
        print("Eres mayor de edad")