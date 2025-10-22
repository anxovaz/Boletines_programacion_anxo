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