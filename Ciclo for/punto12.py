n= int(input("Ingrese el numero de estudiantes: "))
notas_totales = []
suma_total = 0
for i in range(n):
    print("Estudiante", i + 1)
    notas = []

    for j in range(4):
        nota= float(input("Ingrese la nota: ".format(j + 1)))
        notas.append(nota)
        suma_total += nota
    notas_totales.append(notas)

print("\nResultados:")

for i in range(n):
    notas_estudiante = notas_totales[i]
    nota_maxima = max(notas_estudiante)
    nota_minima = min(notas_estudiante)
    promedio = sum(notas_estudiante) / len(notas_estudiante)
    print("Estudiante", i + 1)
    print("Nota más alta:", nota_maxima)
    print("Nota más baja:", nota_minima)
    print("el promedio es:", promedio)
  