#Ficheros boletín 11
'''Ejercicio 1
Crear un programa xestor de notas persoais, que permita ao usuario gardar e consultar notas.
O usuario pode engadir unha nova nota (texto libre).


As notas gárdanse nun ficheiro de texto (notas.txt), unha por liña.


O programa pode listar todas as notas gardadas.


O usuario pode buscar notas que conteñan unha palabra clave.
'''
from archivos_boletin11.boletin11ClassTarea import Tarea
import pickle

def ejercicio1():
    with open('./archivos_boletin11/ejercicio1.txt',"a") as f:
        inputUsuario = str(input("Ingrese su nota: "))
        f.write("\n" + inputUsuario)

    with open('./archivos_boletin11/ejercicio1.txt',"r") as f:
        for i in f.readlines():
            print(i)

ejercicio1()

print("-------------------------------")

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
print("-------------------------------")
def ejercicio3():
    def readFile():
        with open("./archivos_boletin11/tarefas.dat", "rb") as f:
            return pickle.load(f)
    listaTareas = readFile()
    def updateFile(): #guarda la lista tareas en tarefas.dat
        with open("./archivos_boletin11/tarefas.dat", "wb") as f:
            pickle.dump(listaTareas, f)

    def agregarTarea(tarea):
        if not isinstance(tarea, Tarea):
            raise TypeError("La tarea tiene que ser una instancia de la clase Tarea")
        else:
            listaTareas.append(tarea)
            updateFile()
    def borrarTarea(tarea):
        if not isinstance(tarea,Tarea):
            raise TypeError("La tarea tiene que ser Tarea()")
        else:
            if tarea in listaTareas:
                listaTareas.remove(tarea)
                updateFile()
            else:
                raise ValueError("Tarea no encontrada")

    def modificarTarea(indice, tareaNueva):
        if not isinstance(tareaNueva,Tarea):
            raise TypeError("La(s) tarea(s) tiene(n) que ser Tarea()")
        else:
            listaTareas[indice] = tareaNueva
            updateFile()


    print("Ejercicio3:\n1.Agregar unha nova tarefa.\n2.Borrar Tarea\n3.Modificar tarefa\n4.Listar tarefas")
    opcion = int(input("Ingrese su opcion: "))
    match opcion:
        case 1:
            nombre=str(input("Ingrese nombre tarea: "))
            fecha=str(input("Ingrese fecha de la tarefa: "))
            hora=str(input("Ingrese hora de la tarefa: "))
            duracion=str(input("Ingrese duracion de la tarefa: "))
            descripcion=str(input("Ingrese descripcion de la tarefa: "))
            estado=str(input("Ingrese estado de la tarefa(completada/no completada): "))
            tarea = Tarea(fecha,hora,duracion,nombre,descripcion,estado)
            agregarTarea(tarea)
        case 2:
            for indice, tarea in enumerate(listaTareas):
                print(f"{indice} - {tarea.nombreTarea}")
            indice = int(input("Ingrese indice de la tarea para borrar: "))
            borrarTarea(listaTareas[indice])
        case 3:
            for indice, tarea in enumerate(listaTareas):
                print(f"{indice} - {tarea.nombreTarea}")
            indice = int(input("Ingrese indice de la tarea para modificar: "))
            print("----")
            print("Crea una nueva Tarea:")
            nombre = str(input("Ingrese nombre tarea: "))
            fecha = str(input("Ingrese fecha de la tarefa: "))
            hora = str(input("Ingrese hora de la tarefa: "))
            duracion = str(input("Ingrese duracion de la tarefa: "))
            descripcion = str(input("Ingrese descripcion de la tarefa: "))
            estado = str(input("Ingrese estado de la tarefa(completada/no completada): "))
            tarea = Tarea(fecha, hora, duracion, nombre, descripcion, estado)
            modificarTarea(indice,tarea)
        case 4:
            for i in listaTareas:
                print("  ---  ")
                print(i)





ejercicio3()