numero = int(input("Ingrese un número entero mayor que cero: "))
while numero <= 0:
    print("El número ingresado debe ser mayor que cero. Intente nuevamente.")
    numero = int(input("Ingrese un número entero mayor que cero: "))

divisor = 1
print("Los divisores de", numero, "son:")
while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
    divisor += 1
