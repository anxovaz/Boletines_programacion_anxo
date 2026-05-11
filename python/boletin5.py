print("Ejercicio 1")
for i in range(10,21):
    print(i)

print("Ejercicio 2")
celsius=int(input("Introduce grados C: "))
fahrenheit=9/5*celsius+32
print(fahrenheit)


print("Ejercicio 3")

for i in range(0,121,10):
    print(str(i) + "F = " + str(round((i-32)*5/9,2)) + "C") #redondeo a 2 cifras

print("Ejercicio 4")
num1=int(input("Introduce num1: "))
num2=int(input("Introduce num2: "))
for i in range(num1,num2 + 1):
    if i%2==0: #solo imprime los que se puedan dividir entre 2 y den exacto (pares)
        print(i)
    #si no son pares no se imprimen y se vuelve a ejecutar el bucle (a no ser que ya sea el último)

print("Ejercicio 5")
n=int(input("Introduce n: "))
sum=0
for i in range(1,n+1):
    sum+=i
    print(str(i) + " - " + str(sum))

print("Ejercicio 6")
condicion=False #variable de control
while condicion == False: #mientras sea false
    m=int(input("Introduce un numero:"))
    factorial=1 #inicio factorial a 1 ya que no afecta en el funcionamiento ya que el primer numero por el que se multiplica es 1, si escribiese 0 el resultado siempre seria 0 ya que estaria multiplicando constantemente por 0, ej: 0*1=0 0*2=0 0*3=0
    for i in range(1,m+1): #le sumo 1 a m para que coja hasta el numero especificado
        factorial=factorial*i #multiplico el factorial por el nuevo num(i)
    print("Su factorial es: " + str(factorial))
    r=input("Quieres continual calculando factoriales (S/N): ")
    if r == "N" or r == "n": #mayus o minus
        condicion=True #para salir del bucle, tmb valdria un break
        print("Saliendo...")


print("Ejercicio 7")
for i in range(1,7): #del 1 al 6
    for j in range(1, 7):
        print(str(i) + " | " + str(j))


print("Ejercicio 8")
n8=int(input("Introduce un num: "))
for i in range(1,n8+1):
    for j in range(1, n8+1):
        print(str(i) + " | " + str(j))

print("Ejercicio 9")
tupla9=(6,1,0,0,-3,0,1,19,-7,9)
negativos=0
positivos=0
ceros=0
for i in tupla9:
    if i<0:
        negativos+=1
    elif i>0:
        positivos+=1
    elif i==0:
        ceros+=1
    else:
        print("Error")
        break

print("Positivos: " + str(positivos))
print("Negativos: " + str(negativos))
print("Ceros: " + str(ceros))


print("Ejercicio 10")
control10=False
while control10==False:
    base10=int(input("Introduce base: "))
    altura10=int(input("Introduce altura: "))

    if base10<0 or altura10<0: #es negativo
        print("Datos incorrectos, por favor introduce una base y altura positiva positiva")
        continue

    else:
        control10=True

print("El área es: " + str(base10*altura10))

print("Ejercicio 11")
control11=False
while control11==False:
    num11=int(input("Introduce número para mostrar tabla multiplicar (0=salir): "))
    if num11==0:
        print("Saliendo...")
        control11=True #cambio variable, no es necesario un continue porque no ejecuta el else
    else: #no se ejecuta si es 0
        for i in range(1,11): #del 1 al 10
            print(str(num11) + " * " + str(i) + " = " + str(num11*i)) #imprime


print("Ejercicio 12")
control12=False #control
#contadores
bajos=0
medios=0
altos=0

while control12==False:
    sueldo=int(input("Introduce sueldo (0=salir): "))
    if sueldo == 0: # si es 0
        print("Saliendo...")
        control12=True #para que no vuelva a entrar al while
        continue #vuelve al bucle ignorando el resto
    if sueldo < 1000: #bajos
        bajos+=1
    elif sueldo >=1000 and sueldo <= 1750: #medios
        medios+=1
    else:#altos (si no es menor que 1000 ni esta entre 1000 y 1750 significa que si o si es mayor)
        altos +=1

print("<1000: ", bajos)
print("<=1000 and <=1750: ", medios)
print(">1750: ", altos)

print("Ejercicio 13")
#"*" * 3 = "***"
num13=int(input("Introduce num: "))
for i in range(1,num13+1):
    asteriscos="*" * i #genera esteríscos
    print(asteriscos)

print("Ejercicio 14")
control14=False
contador14=0 #contador del bucle
suma=0 #variable en la que se almacena la suma
while control14==False and contador14<10: #si la variable de control es false y el usuario no ha metido más de 10 números (<10 y no <=10 porque empieza desse 0)
    num14=int(input("Introduce num (999=terminar): "))
    if num14==999: #si es 999, no lo suma
        print("Saliendo...")
        control14=True #variable control while
        continue #vuelve al bucle
    suma+=num14 #
    print("La suma actual es: ", suma) #actual
    contador14+=1 #suma 1 al contador

print("La suma final es: ", suma) #muestra uma final al salir