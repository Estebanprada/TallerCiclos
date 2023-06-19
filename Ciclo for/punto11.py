cantidad_temperaturas = int(input("Ingrese la cantidad de temperaturas: "))
temperaturas = []

for i in range(cantidad_temperaturas):
    temperatura = float(input("Ingrese la temperatura: ".format(i + 1)))
    temperaturas.append(temperatura)

temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)
temperatura_promedio = sum(temperaturas) / len(temperaturas)

print("\nTemperatura más alta:", temperatura_maxima)
print("Temperatura más baja:", temperatura_minima)
print("Temperatura promedio:", temperatura_promedio)

