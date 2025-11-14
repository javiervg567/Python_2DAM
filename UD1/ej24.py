"""
Dibuja un ordinograma de un programa que calcule y escriba la suma y el producto de los
10 primeros números naturales.
"""
suma = 0
producto = 1
for i in range(10):
    suma += i
    producto *= i
print("La suma de los 10 primeros números naturales es:", suma)
print("El producto de los 10 primeros números naturales es:", producto)