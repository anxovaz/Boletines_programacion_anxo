print("Ejercicio 1")
num1_1=int(input("Introduce num: "))
if num1_1>=0: #el 0 también es positivo
    print("Es positivo")
else:
    print("No es positivo")

print("Ejercicio 2")
num2_1=int(input("num1: "))
num2_2=int(input("num2: "))
if num2_1 >= num2_2: #si es mayor o igual
    print(num2_1 - num2_2)
else: #cualquier otro caso es menor
    print(num2_1+num2_1)

print("Ejercicio 3")
num3_1=int(input("Introduce num: "))
if num3_1 > 0: #si es mayor que 0
    print("+")
elif num3_1 < 0: #si es menor de 0
    print("-")
else: #0
    print(0)

print("Ejercicio 4")
nombre1=input("Introduce nombre1: ")
peso1=int(input("Introduce peso1: "))
nombre2=input("Introduce nombre2: ")
peso2=int(input("Introduce peso2: "))

if peso1 > peso2: #si persona 1 pesa más
    print(nombre1, " pesa más por ", peso1 - peso2, " kg")
elif peso2 > peso1: # si persona 2 pesa más
    print(nombre2, " pesa más por ", peso2 - peso1, " kg")
else: #igual
    print("Pesan igual")

print("Ejercicio 5")
#declaración de números
num1 = 5
num2 = 7
num3 = 8

#calcular el mayor
if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
