print("Ejercicio 1")
print(len("Isto é Python!"))

print("Ejercicio 2")
for i in "Python":
    print(i)

print("Ejercicio 3")
texto="Python para todos"
print(texto[::-1])

print("Ejercicio 4")
cadena_nueva=""
for i in "Guido Van Rossum creou Python":
    if i != " ":
        cadena_nueva+=i

print(cadena_nueva)

print("Ejercicio 5")
vocales=0
consonantes=0
for i in "Python Python Python":
    if i in ["a","e","i","o","u"]:
        vocales+=1
    elif i != " ":
        consonantes+=1

print(vocales, consonantes)

print("Ejercicio 6")
texto6="www.phytonparatodos.com"
textos_divididos=[]
textos_divididos.append(texto6[:10])
textos_divididos.append(texto6[10:])
print(textos_divididos)
print(textos_divididos[0]+textos_divididos[1])

print("Ejercicio 7")
texto7 = " Phytoneros"
texto_may = texto7.upper()
print("Maiúsculas:", texto_may)

texto_minus = texto7.lower()
print("Minúsculas:", texto_minus)

print("Ejercicio 8")
if "Python" == "JavaScript":
    print("Son iguales")
else:
    print("No son iguales")

print("Ejercicio 9")
java=""
vocales_sin_a="eiou"
for i in "Jeve jeve Jeve":
    java+=i
    for j in vocales_sin_a:
        if i == j:
            java = java[:-1]
            java+="a"

print(java)

print("Ejercicio 10")
cadena="Ola, son alumno de DAM1, e son programador desde o 2025"
print("La cadena tiene: ", len(cadena), " caracteres")
espaciosblanco=0
digitos=0
for i in cadena:
    if i == " ":
        espaciosblanco+=1
    else:
        digitos+=1

print("Hay ", espaciosblanco, " espacios en blanco.")
print("La cadena tiene ", digitos, " digitos.")


print("Ejercicio 11")
def ej11apa(cadena):
    print(cadena[:2])

def ej11apb(cadena):
    longitud=len(cadena)
    print(cadena[longitud-3:])

def ej11apc(cadena):
    print(cadena[::2])

def ej11apd(cadena):
    print("normal: ", cadena)
    print("inversa: ", cadena[::-1])

ej11apa("aabb")
ej11apb("aabb")
ej11apc("aabbcc")
ej11apd("aabbcc")

print("Ejercicio 12")

