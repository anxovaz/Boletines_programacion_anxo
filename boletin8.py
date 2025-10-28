print("Ejercicio 1") #pendiente de arreglar, si no empieza por 1 no va
tupla1=(-1,2,3,4,5,5,6,9)
ordenado=True

num_anterior=-999999
for i in tupla1:
    if i < num_anterior:
        ordenado=False
        break
    else:
        num_anterior=i

if ordenado==True:
    print("La lista está ordenada")
else:
    print("La lista está desordenada")

print("Ejercicio 2")