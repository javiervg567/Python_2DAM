filas = 5
for i in range (1, filas +1):
    if i == 1:
        print("4" + " ")
    elif i == filas:
        print("4" * filas)
    else:
        print("4" + " " * (i -2) + "4")