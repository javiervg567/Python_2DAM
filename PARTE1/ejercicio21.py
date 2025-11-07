# Escriba un programa que calcula el salario neto semanal de un trabajador en función del
# número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
#   Las primeras 35 horas se pagan a tarifa normal.
#   Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
#   Las tasas de impuesto son:
#    Los primeros 500€ son libres de impuestos.
#   Los siguientes 400€ tiene un 25% de impuesto.
#   Los restantes un 45% de impuesto.
# Escribe el nombre del trabajador, salario bruto, tasas y salario neto.
try:
    nombre = input("Introduce el nombre del trabajador: ").strip()
    horas_trabajadas = float(input("Introduce el número de horas trabajadas en la semana: "))
    tarifa_hora = float(input("Introduce la tarifa por hora (€): "))
    
    if horas_trabajadas < 0 or tarifa_hora < 0:
        print("Error: Las horas trabajadas y la tarifa por hora deben ser valores positivos.")
        raise SystemExit(1)
    
    # Calcular el salario bruto
    if horas_trabajadas <= 35:
        salario_bruto = horas_trabajadas * tarifa_hora
    else:
        salario_bruto = (35 * tarifa_hora) + ((horas_trabajadas - 35) * tarifa_hora * 1.5)
    
    # Calcular los impuestos
    impuestos = 0
    if salario_bruto > 500:
        if salario_bruto <= 900:
            impuestos += (salario_bruto - 500) * 0.25
        else:
            impuestos += 400 * 0.25
            impuestos += (salario_bruto - 900) * 0.45
    
    salario_neto = salario_bruto - impuestos
    
    print(f"\nResumen para {nombre}:")
    print(f"Salario Bruto: €{salario_bruto:.2f}")
    print(f"Impuestos: €{impuestos:.2f}")
    print(f"Salario Neto: €{salario_neto:.2f}")
except ValueError:
    print("Entrada no válida. Introduce números válidos para horas y tarifa.")