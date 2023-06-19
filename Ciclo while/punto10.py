n= int(input("Ingrese la cantidad de estudiantes: "))
contador_estudiantes = 0
notas_mas_altas = []
notas_mas_bajas = []
suma_notas = 0

while contador_estudiantes < n:
    print("Ingrese las notas del estudiante", contador_estudiantes + 1)
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    # Calcular la nota más alta
    nota_mas_alta = max(nota1, nota2, nota3)
    notas_mas_altas.append(nota_mas_alta)

    # Calcular la nota más baja
    nota_mas_baja = min(nota1, nota2, nota3)
    notas_mas_bajas.append(nota_mas_baja)

    # Calcular la suma de las notas
    suma_notas += nota1 + nota2 + nota3

    contador_estudiantes += 1

promedio = suma_notas / (n * 3)
print("La nota más alta es:", max(notas_mas_altas))
print("La nota más baja es:", min(notas_mas_bajas))
print("El promedio de las notas es:", promedio)