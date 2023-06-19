numero = int(input("Ingrese un número: "))

if numero > 10:
    resultado = 1
    i = 1
    while i <= 10:
        resultado *= i
        i += 1
    print("El resultado de la multiplicación de los 10 primeros números es:", resultado)
else:
    resultado = 0
    i = 1
    while i <= numero:
        resultado += i
        i += 1
    print("El resultado de la suma de los números desde 1 hasta", numero, "es:", resultado)
