numero = int(input("Ingrese un número: "))
if numero > 10:
    resultado = 1
    for i in range(1, 11):
        resultado *= i
    print("El resultado de la multiplicación de los 10 primeros números es:", resultado)
else:
    resultado = 0
    for i in range(1, numero + 1):
        resultado += i
    print("El resultado de la suma de los números desde 1 hasta", numero, "es:", resultado)
