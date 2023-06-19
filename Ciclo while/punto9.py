n= int(input("Ingrese la cantidad de temperaturas: "))

contador = 0
temperaturas = []
suma_temperaturas = 0

while contador < n:
    temperatura = float(input("Ingrese la temperatura {}: ".format(contador + 1)))
    temperaturas.append(temperatura)
    suma_temperaturas += temperatura
    contador += 1

temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)
promedio = suma_temperaturas / n

print("Temperatura máxima:", temperatura_maxima)
print("Temperatura mínima:", temperatura_minima)
print("Temperatura promedio:", promedio)
