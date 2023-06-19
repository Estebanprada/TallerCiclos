n= int(input("Ingrese un número: "))
suma_impares = 0
cantidad_impares = 0

for i in range(1, n + 1, 2):
    suma_impares += i
    cantidad_impares += 1

print("La suma de los números impares es:", suma_impares)
print("La cantidad de números impares es:", cantidad_impares)
