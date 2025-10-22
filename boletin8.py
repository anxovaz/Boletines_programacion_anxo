print("Ejercicio 1") #pendiente de arreglar, si no empieza por 1 no va
tupla1=(1,2,3,4,5,6,7)
ordenado=True

for i in range(len(tupla1)):
    i+=1
    if i != tupla1[i-1]:
        ordenado = False
        break

if ordenado == False:
    print("No está ordenada")
else:
    print("Está ordenada")

print("Ejercicio 2")