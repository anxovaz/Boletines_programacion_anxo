#Ficheros boletín 11
'''Ejercicio 1
Crear un programa xestor de notas persoais, que permita ao usuario gardar e consultar notas.
O usuario pode engadir unha nova nota (texto libre).


As notas gárdanse nun ficheiro de texto (notas.txt), unha por liña.


O programa pode listar todas as notas gardadas.


O usuario pode buscar notas que conteñan unha palabra clave.
'''
from archivos_boletin11.boletin11ClassTarea import Tarea


def ejercicio1():
    with open('./archivos_boletin11/ejercicio1.txt',"a") as f:
        inputUsuario = str(input("Ingrese su nota: "))
        f.write("\n" + inputUsuario)

    with open('./archivos_boletin11/ejercicio1.txt',"r") as f:
        for i in f.readlines():
            print(i)

ejercicio1()

'''
Ler un ficheiro de texto e contar cantas veces aparece cada palabra.
Solicita ao usuario o nome dun ficheiro .txt.


Mostra a frecuencia de cada palabra (ignorando maiúsculas/minúsculas e signos de puntuación).


Gárdase un resumo nun novo ficheiro resumo_palabras.txt.


'''

def ejercicio2():
    print("Ejercicio2")
    #fich = str(input("Introduce ruta del archivo: "))
    fich = "./archivos_boletin11/ejercicio2.txt"
    splitFich = []
    with open(fich,"r") as f:
        for i in f.readlines():
            for j in i.split(" "):
                splitFich.append(j)


    palabras = []
    for i in splitFich:
        if ejercicio2_comprobar_palabra(i,palabras):
            input = []
            input.append(i)
            input.append(splitFich.count(i))
            palabras.append(input)



    return palabras


def ejercicio2_comprobar_palabra(palabra, lista):
    for i in lista:
        for j in i:
            if palabra == j:
                return False
            break #solo me interesa la primera posición que es en la que va el nombre del elemento
    return True

print(f"Ejercicio2: {ejercicio2()}")

def ejercicio3():
    tarea = Tarea()


ejercicio3()