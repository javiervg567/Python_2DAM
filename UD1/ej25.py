"""
Dibuja un ordinograma que lea una calificación numérica entre 0 y 10 y la transforme en la
calificación alfabética, escribiendo el siguiente resultado.
• De 0 a < 3 Muy Deficiente.
• De 3 a < 5 Insuficiente.
• De 5 a < 6 Suficiente.
• De 6 a < 7 Bien.
• De 7 a <9 Notable.
• De 9 a 10 Sobresaliente.
"""
try:
    nota = float(input("Introduce la calificación (0-10): ").strip())
except ValueError:
    print("Entrada no válida: debe ser un número.")
    raise SystemExit(1)

if not (0 <= nota <= 10):
    print("Calificación no válida: debe estar entre 0 y 10.")
    raise SystemExit(1)

match True:
    case _ if 0 <= nota < 3:
        print("Muy Deficiente")
    case _ if 3 <= nota < 5:
        print("Insuficiente")
    case _ if 5 <= nota < 6:
        print("Suficiente")
    case _ if 6 <= nota < 7:
        print("Bien")
    case _ if 7 <= nota < 9:
        print("Notable")
    case _ if 9 <= nota <= 10:
        print("Sobresaliente")