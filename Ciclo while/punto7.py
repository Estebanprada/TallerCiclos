sumatoria = 0
numero = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))

while numero != 0:
    sumatoria += numero
    numero = int(input("Ingrese otro número entero (ingrese 0 para finalizar): "))

print("La sumatoria de los números ingresados es:", sumatoria)