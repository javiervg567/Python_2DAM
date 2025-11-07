#Escriba un programa que recibe como datos de entrada una hora expresada en horas,
#minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
#transcurrido un segundo
try:
    horas = int(input("Introduce las horas (0-23): "))
    minutos = int(input("Introduce los minutos (0-59): "))
    segundos = int(input("Introduce los segundos (0-59): "))
    
    if not (0 <= horas < 24) or not (0 <= minutos < 60) or not (0 <= segundos < 60):
        print("Error: La hora, minutos y segundos deben estar en los rangos correctos.")
        raise SystemExit(1)
    
    segundos += 1
    if segundos == 60:
        segundos = 0
        minutos += 1
        if minutos == 60:
            minutos = 0
            horas += 1
            if horas == 24:
                horas = 0
    
    print(f"La hora después de un segundo será: {horas:02}:{minutos:02}:{segundos:02}")
except ValueError:
    print("Error: Introduce números válidos para horas, minutos y segundos.")