"""
La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
control switch).
"""

print("--- Calculadora de Matrícula Universitaria ---")
    
try:
    nombre_postulante = input("Ingrese el nombre del postulante: ")
    facultad_ingresada = input("Ingrese la facultad a estudiar: ")

    facultad = facultad_ingresada.lower().strip()
    
    importe_matricula = None
    mensualidad = None
    
    match facultad:
        case "ing de sistemas":
            importe_matricula, mensualidad = 350, 650
        case "derecho":
            importe_matricula, mensualidad = 300, 550
        case "ing naviera" :
            importe_matricula, mensualidad = 300, 500
        case "ing pesquera":
            importe_matricula, mensualidad = 310, 460
        case "contabilidad":
            importe_matricula, mensualidad = 280, 490
        case "administración" | "administracion":
            importe_matricula, mensualidad = 360, 520
        case _:
            importe_matricula, mensualidad = None, None

    if importe_matricula is None:
        print(f"\nError: La facultad '{facultad_ingresada}' no se encuentra en la lista.")
        print("Facultades disponibles: Ing. de Sistemas, Derecho, Ing. Naviera, Ing. Pesquera, Contabilidad, Administración")
    else:
        igv = (importe_matricula + mensualidad) * 0.18
        monto_final = importe_matricula + mensualidad + igv
        
        print("\n--- Resumen de Pagos ---")
        print(f"Postulante: {nombre_postulante}")
        print(f"Facultad: {facultad_ingresada}")
        print(f"Importe de Matrícula: S/ {importe_matricula:.2f}")
        print(f"Mensualidad: S/ {mensualidad:.2f}")
        print(f"IGV (18%): S/ {igv:.2f}")
        print("---------------------------------")
        print(f"Monto Final a Pagar: S/ {monto_final:.2f}")

except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")