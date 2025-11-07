#Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
#contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
#incorrecto
try:
    usuario_correcto = "admin"
    contrasena_correcta = "1234"
    
    usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("Inicio de sesión correcto")
    elif usuario != usuario_correcto:
        print("Nombre de usuario incorrecto")
    else:
        print("Contraseña incorrecta")
except Exception as e:
    print("Ocurrió un error:", e)