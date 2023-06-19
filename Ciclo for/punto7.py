tabla = int(input("Ingrese el número de la tabla de multiplicar que desea ver: "))
print("Tabla de multiplicar del", tabla)

for i in range(11):
    resultado = tabla * i
    print(tabla, "x", i, "=", resultado)
