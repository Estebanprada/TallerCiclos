n = int(input("Ingrese un número entero: "))
suma_pares = 0
numero = 0

while numero <= n:
    if numero % 2 == 0:
        suma_pares += numero
    numero += 1

print("La suma de los números pares desde 0 hasta", n, "es:", suma_pares)