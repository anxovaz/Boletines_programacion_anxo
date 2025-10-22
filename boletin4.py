import math
print("Ejercicio 1")
ej1=700
if ej1<=100:
    print("bajo")
elif ej1>100 and ej1<=500:
    print("medio")
elif ej1>500 and ej1<=1000:
    print("alto")
else: #cualquier otro caso siempre sería >1000
    print("primera necesidad")

print("Ejercicio 2")
control2=False
while control2==False:
    print("Escoje una opción:\n1.Cuadrado\n2.Triangulo\n3.Círculo")
    opcion=input()
    if opcion=="1":
        l=int(input("Introduce lado:"))
        print("Área: ", l*l)
        control2=True
    elif opcion=="2":
        b=int(input("Introduce base: "))
        h=int(input("Introduce altura: "))
        print("Área: ", b*h)
        control2=True
    elif opcion=="3":
        r=int(input("Introduce r: "))
        print("Área: ", math.pi * (r*r))
        control2=True
    else: #incorrecta
        print("Error, opción incorrecta")
        #control2 sigue siendo false

print("Ejercicio 3")
num3=int(input("Introduce número: "))
print(abs(num3)) #ABSoluto

print("Ejercicio 4")
num4=int(input("Introduce num: "))
if num4 == 1:
    print("uno")
if num4 == 2:
    print("dos")
if num4 == 3:
    print("tres")
else:
    print("Otro número")

print("Ejercicio 5")
dni=int(input("Introduce dni sin letra: "))
nletra=dni%23
if nletra==0:
    print("T")
elif nletra==1:
    print("R")
elif nletra==2:
    print("W")
elif nletra==3:
    print("A")
elif nletra==4:
    print("G")
elif nletra==5:
    print("M")
elif nletra==6:
    print("Y")
elif nletra==7:
    print("F")
elif nletra==8:
    print("P")
elif nletra==9:
    print("D")
elif nletra==10:
    print("X")
elif nletra==11:
    print("B")
elif nletra==12:
    print("N")
elif nletra==13:
    print("J")
elif nletra==14:
    print("Z")
elif nletra==15:
    print("S")
elif nletra==16:
    print("Q")
elif nletra==17:
    print("V")
elif nletra==18:
    print("H")
elif nletra==19:
    print("L")
elif nletra==20:
    print("C")
elif nletra==21:
    print("K")
elif nletra==12:
    print("E")
else:
    print("DNI INCORRECTO")






