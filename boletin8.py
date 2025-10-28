import math #ej6

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
def ej2(ficha1,ficha2):
    encajan = False
    for i in ficha1:
        for j in ficha2:
            if i == j:
                encajan=True
                break

    return encajan

print(ej2((2,6),(4,3)))

print("Ejercicio 3")
def ej3(tupla):
    for i in tupla:
        print("Estimado don/dona", i) #pone el espacio del medio solo

ej3(("nombre1","nombre2"))

print("Ejercicio 4")
def ej4(tupla,pi,pf):
    for i in range(pi,pf):
        print("Estimado don/dona", tupla[i])  # pone el espacio del medio solo

ej4(("nombre1","nombre2", "nombre3"),1,3)

print("Ejercicio 5")
def ej5(tupla,pi,pf):
    for i in range(pi,pf):
        if tupla[i].endswith("a"):
            print("Estimada dona", tupla[i])  # pone el espacio del medio solo
        elif tupla[i].endswith("o"):
            print("Estimado don", tupla[i])  # pone el espacio del medio solo
        else:
            print("Estimado don/dona", tupla[i])  # pone el espacio del medio solo

ej5(("paco","manolo", "elena","carlos"),1,4)

print("Ejercicio 6")
def analizar_numeros(numeros):
    primos = []
    for numero in numeros:
        if numero < 2:
            continue
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(numero)

    sumatorio = sum(numeros)
    if numeros:
        promedio = sumatorio / len(numeros)
    else:
        promedio = 0

    factoriais = []
    for numero in numeros:
        factoriais.append(math.factorial(numero))

    print("Primos:", primos)
    print("Sumatorio:", sumatorio)
    print("Promedio:", promedio)
    print("Factoriales:", factoriais)

numeros = [1, 2, 3, 4, 5, 6, 7]
analizar_numeros(numeros)

print("Ejercicio 7")
def ej7(lista,num):
    menores=[]
    mayores=[]
    iguales=[]
    for i in lista:
        if i<num:
            menores.append(i)
        elif i>num:
            mayores.append(i)
        else: #iguales
            iguales.append(i)

print("Ejercicio 8")
def ej8(lista_tuplas):
    resultado = []
    for apellido, nombre, inicial in lista_tuplas:
        cadena = nombre + " " + inicial + ". " + apellido
        resultado.append(cadena)
    return resultado

# Ejemplo de uso
personas = [
    ("Apellido 1", "Nombre1", "N"),
    ("Apellido2", "Nombre2", "N")
]

print(ej8(personas))

print("Ejercicio 9")

def ej9(tupla):
    v_act = -999
    cant_act = 0
    orden=[]
    for i in tupla:
        if v_act == -999:
            v_act=i

        if i == v_act:
            cant_act+=1
        else:
            tupla_interna=(v_act,cant_act)
            orden.append(tupla_interna)
            cant_act=1 #la declaro en 1 porque ya se acaba de encontrar otro numero
            v_act=i
    orden.append((v_act, cant_act))
    print(orden)

ej9(([1, 1, 1, 3, 5, 1, 1, 3, 3]) )

print("Ejercicio 10")
def ej10_suma(matriz1, matriz2):
    suma=[]
    for i in matriz1:
        suma.append(i)
    for i in matriz2:
        suma.append(i)

    suma_total=0
    for i in suma:
        suma_total+=i

    print("La suma de los valores de las matrices", suma_total)

ej10_suma((1,2,3,4),(-2,1,3))

def ej10_producto(matriz1, matriz2):
    suma_m1=0
    suma_m2=0
    for i in matriz1:
        suma_m1+=i
    for i in matriz2:
        suma_m2+=i

    print("El producto es: ", suma_m1*suma_m2)

ej10_producto((1,2,3,4),(-2,1,3))

print("Ejercicio 11")
def ej11():
    texto=str(input("Introduce texto: "))
    lista=[]
    inicio=0
    for i,v in enumerate(texto):
        if v == "\n":
            lista.append(texto[inicio:i])
            inicio=i+1
    lista.append(texto[inicio:]) #agrega la ultima linea ya que no tiene uun salto de línea

    print(lista)

ej11()