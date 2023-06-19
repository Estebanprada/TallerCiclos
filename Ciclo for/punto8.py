lista=[ ]
suma=0
for i in range(5):
  lista.insert(i,nota)
  nota=int(input("Ingrese las notas del estudiante: "))
  suma=suma+lista[i]
promedio=suma/5

print("Su nota final es: ",promedio)