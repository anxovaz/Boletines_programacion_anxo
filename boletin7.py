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
def ej12a(cadena,caracter):
    cadena=cadena.replace(" ", caracter)
    return cadena

def ej12b(cadena,caracter):
    lista=[]
    for i in cadena:
        lista.append(i)
    cadena_separada=""
    for i in lista:
        cadena_separada+=i
        cadena_separada+=caracter

    return cadena_separada[:-1] #le quita el último caracter

def ej12c(cadena,caracter):
    longitud=len(cadena)
    return longitud*caracter

def ej12d(cadena,caracter):
    contador=0
    nueva_cadena=""
    for i in cadena:
        contador += 1
        if contador == 3:
            nueva_cadena+=i
            nueva_cadena+=caracter
            contador=0
        else:
            nueva_cadena+=i


    return nueva_cadena

print(ej12a("a a","a"))
print(ej12b("abcde",","))
print(ej12c("aaaa","!"))
print(ej12d("aaabbbcccddd",","))


print("Ejercicio 13")
def ej13a(cadena,caracter,max):
    contador=0
    for i in cadena:
        if i == " " and contador < max:
            cadena+=caracter
            contador += 1
        cadena+=caracter
    return cadena

def ej13b(cadena,caracter,max):
    contador=0
    lista=[]
    for i in cadena:
        lista.append(i)
    cadena_separada=""
    for i in lista:
        if contador < max:
            cadena_separada+=i
            cadena_separada+=caracter
            contador+=1

    return cadena_separada[:-1] #le quita el último caracter

def ej13c(cadena,caracter,max):
    return (caracter*max)+cadena[max:]


def ej13d(cadena,caracter,max):
    contador=0
    nueva_cadena=""
    maximo=0
    for i in cadena:
        contador += 1
        if contador == 3 and maximo < max:
            nueva_cadena+=i
            nueva_cadena+=caracter
            contador=0
            maximo+=1
        else:
            nueva_cadena+=i


    return nueva_cadena

print(ej13a("a a","a",1))
print(ej13b("abcde",",",1))
print(ej13c("aaaa","!",1))
print(ej13d("aaabbbcccddd",",",1))

print("Ejercicio 14")
def ej14(cadena):
    cadena=str(cadena)
    cadena=cadena[::-1] #invirte
    contador=0
    cadena_nueva=""
    for i in cadena:
        cadena_nueva+=i
        contador += 1
        if contador == 3:
            cadena_nueva+="."

    return cadena_nueva[::-1] #invierte otra vez

print(ej14(12345))

print("Ejercicio 15")
def ej15(cadena):
    split=[]
    split=cadena.split(" ")
    iniciales=""
    empieza_a=""
    for i in split:
        iniciales+=i[0] #guarda primera letra
        if i.startswith("a") or i.startswith("A"):
            empieza_a+=i
            empieza_a+=" "


    print(iniciales)
    print(iniciales.upper())
    print(empieza_a[:-1]) #que no recoja el último espacio

ej15("Antes de abrir")

print("Ejercicio 16")
def ej16_cons(cadena):
    vocales=["a","e","i","o","u"]
    cadena_sin_vocales=""
    for i in cadena:
        if not i in vocales:
            cadena_sin_vocales+=i

    print(cadena_sin_vocales)

def ej16_vocales(cadena):
    vocales = ["a", "e", "i", "o", "u"]
    cadena_con_vocales = ""
    for i in cadena:
        if i in vocales:
            cadena_con_vocales += i

    print(cadena_con_vocales)

def ej16_cambio_vocales(cadena):
    vocales = ["a", "e", "i", "o", "u"]
    cadena_con_vocales_cambiada = ""
    for i in cadena:
        cadena_con_vocales_cambiada += i
        for j,v in enumerate(vocales):
            if i == v:
                cadena_con_vocales_cambiada = cadena_con_vocales_cambiada[:-1]  # le quita la ultima letra si es una vocal
                if v == "u":
                    cadena_con_vocales_cambiada += vocales[0] #u=a
                    break
                else:
                    cadena_con_vocales_cambiada+=vocales[j+1]
                    break


    print(cadena_con_vocales_cambiada)

ej16_vocales("abecedario")
ej16_cons("abecedario")
ej16_cambio_vocales("abecedariu")

print("Ejercicio 17")
palabra17="prueba"
if palabra17 == palabra17[::-1]: #inverso
    palindromo=True
else:
    palindromo=False

if palindromo == True:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

print("Ejercicio 18")
def ej18_a(cadena1,cadena2):
    subcadena=False
    if cadena2 in cadena1:
        subcadena=True

    return subcadena

def ej18_b(cadena1,cadena2):
    abecedario="abcdefghijklmnopqrstuvwxyz"
    pos_cadena1=-1
    pos_cadena2=-1
    for i,v in enumerate(abecedario):
        if cadena1[0] == v:
            pos_cadena1=i
        if cadena2[0] == v:
            pos_cadena2=i

    if pos_cadena1>pos_cadena2:
        return cadena2,cadena1
    else: #o si son iguales
        return cadena1, cadena2

print(ej18_a("cadena1","na1"))
print(ej18_b("gato","arena"))

print("Ejercicio 19")
def ej19(cadena_binaria):
    decimal=0
    long = len(cadena_binaria)
    for i in range(long):
        bit = cadena_binaria[i]
        if bit == '1':
            exponente = long - 1 - i
            decimal += 2 ** exponente
    return decimal

print(ej19("101"))

print("Ejercicio 20")
def ej20_i(cadena,caracter):
    nueva_cadena=""
    for i in cadena:
        if i == caracter:
            nueva_cadena+=i

    return nueva_cadena

def ej20_ii(cadena,caracter):
    nueva_cadena=""
    for i in cadena:
        if i == caracter:
            nueva_cadena+=i
        else:
            nueva_cadena+="-"
    return nueva_cadena

print(ej20_i("cadena","a"))
print(ej20_ii("cadena","a"))

print("Ejercicio 21")
def ej21(cadena):
    if len(cadena) < 8:
        return False
    mayuscula = False
    minuscula = False
    numero = False
    for c in cadena:
        if c.isupper():
            mayuscula = True
        elif c.islower():
            minuscula = True
        elif c.isdigit():
            numero = True

    if mayuscula==True and minuscula==True and numero==True:
        return True
    else:
        return False


print(ej21("123456Ab"))

print("Ejercicio 22")
def ej22(cadena):
    if cadena.startswith(" "):
        cadena=cadena[1:]
    if cadena.endswith(" "):
        cadena=cadena[:-1]

    cadena_nueva=""
    cadena_split=cadena.split(" ")
    for i in cadena_split:
        for j,v in enumerate(i):
            if j == 0 and v.islower():
                cadena_nueva+=v.upper()
            else:
                cadena_nueva+=v
        cadena_nueva+=" " #al hacer el split se pierde el espacio central

    return cadena_nueva[:-1] #le quito el ultimo espacio

print(ej22(" anxo vázquez"))

print("Ejercicio 23")
def ej23(cadena):
    split=cadena.split(" ")
    max=-1
    contador=0
    palabra_mas_larga=""
    for i in split:
        for j in i:
            contador+=1
        if contador>max:
            max=contador
            palabra_mas_larga=i
        contador=0

    return palabra_mas_larga

print(ej23("cad cade caden ca"))


