import random

#En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
#en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
#Si los tres dados son seis, mostrar el mensaje “Excelente”
#Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
#Si un dado se obtiene seis, mostrar el mensaje “Regular”
#Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
# Lanzar tres dados
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)

print(f"Dados: {dado1}, {dado2}, {dado3}")
seis_count = sum([dado1 == 6, dado2 == 6, dado3 == 6])
match seis_count:
    case 3:
        print("Excelente")
    case 2:
        print("Muy bien")
    case 1:
        print("Regular")
    case 0:
        print("Pésimo")
        


