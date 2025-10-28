print("Exercicio 1")
asignaturas=("matemáticas", "lengua", "física")
notas = []

for i in asignaturas:
    nota=str(input("Introduce la nota que sacaste en " + i + ": "))
    notas.append(nota)

print("Tus notas:")
for i,j in enumerate(asignaturas):
    print(j, notas[i]) #muestra la nota asignada basandose en el indice generado por el enumerate

print("Ejercicio 2")
num_ganadores=[]
while True:
    num=int(input("Introduce numeros ganadores (0 para salir)"))

    if num == 0:
        break #sale del bucle infinito
    else:
        num_ganadores.append(num)

num_ganadores=sorted(num_ganadores) #ordena de menor a mayor
print(num_ganadores)

print("Ejercicio 3")
lista=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(lista)-1,-1,-1): #desde la longitud-1 de la lista (osea 9) hasta -1 (sin coger el -1, es decir de queda en 0) y que reste de 1 en 1
    print(lista[i])

print("Ejercicio 4")
asignaturas2=("matemáticas", "lengua", "física")
asignaturas_suspensas=[]

for i in asignaturas2:
    nota2=int(input("Introduce la nota que sacaste en " + i + ": "))

    if nota2 < 5:
        asignaturas_suspensas.append(i)

print(asignaturas_suspensas)

print("Ejercicio 5")
abecedario = list("abcdefghijklmnopqrstuvwxyz")
resultado=[]

for i in range(len(abecedario)): #se comprueban si son múltiplos de 3
    if (i + 1) % 3 != 0: #i + 1 porque i empieza desde 0 y no desde 1
        resultado.append(abecedario[i])

print(resultado)

print("Ejercicio 6")
palabra=str(input("Introduce palabra: "))
if palabra == palabra[::-1]:
    palindromo=True
else:
    palindromo=False

if palindromo == True:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

print("Ejercicio 7")
vocales="aeiou"
conta=0
conte=0
conti=0
conto=0
contu=0

palabra7=str(input("Introduce palabra: "))
for i in palabra7:
    for j in vocales:
        if i == j:
            if j == "a":
                conta+=1
            elif j == "e":
                conte+=1
            elif j == "i":
                conti+=1
            elif j == "o":
                conto+=1
            else:
                contu+=1

print("a", conta)
print("e", conte)
print("i", conti)
print("o", conto)
print("u", contu)

print("Ejercicio 8")
precios=[50,70,46,22,80,65,8]
menor=99999
mayor=-999999
for i in precios:
    if i < menor:
        menor = i

    if i > mayor:
        mayor = i

print(menor, mayor)

print("Ejercicio 9")
vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]

producto_escalar = 0
for i in range(len(vector1)):
    producto_escalar += vector1[i] * vector2[i] #suma la multiplicacion de los dos vectores a la variable

print(producto_escalar)


print("Ejercicio 10")
a=[(1,2,3),(4,5,6)]
b=[(-1,0),(0,1),(1,1)]

prod_a=0
prod_b=0
for i in a:
    for j in i:
        prod_a+=j

for i in b:
    for j in i:
        prod_b+=j

print(prod_a, prod_b)

print("Ejercicio 11")
nums11=[]
while True:
    num11=int(input("Introduce numeros(999 para salir):"))
    if num11 == 999:
        break
    else:
        nums11.append(num11)

sumatotal=0
for i in nums11:
    sumatotal+=i

media = sumatotal/len(nums11) #no pongo -1 en el len porque no me interesa la posición, me interesa la cantidad de valores

print(media)