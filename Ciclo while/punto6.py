n= int(input("Ingrese la cantidad de notas: "))
total = 0
contador = 0

while contador < n:
    nota = float(input("Ingrese la nota: ".format(contador + 1)))
    total += nota
    contador += 1

promedio = total / n
print("El promedio de las notas es:", promedio)
