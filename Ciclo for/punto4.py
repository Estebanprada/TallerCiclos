numero = int(input("Ingresa un número: "))
suma = 0

for i in range(0, numero+1, 2):
    suma += i

print("La suma de los números pares desde 0 hasta", numero, "es:", suma)
