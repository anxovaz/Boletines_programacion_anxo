#Ficheros boletín 11

'''Ejercicio 1
Crear un programa xestor de notas persoais, que permita ao usuario gardar e consultar notas.
O usuario pode engadir unha nova nota (texto libre).


As notas gárdanse nun ficheiro de texto (notas.txt), unha por liña.


O programa pode listar todas as notas gardadas.


O usuario pode buscar notas que conteñan unha palabra clave.
'''

def ejercicio1input():
    with open("./archivos_boletin11/ejercicio1.txt","a") as f:
        inputUsuario = str(input("Ingrese su nota: "))
        f.write(inputUsuario + "\n")
        f.close()

def ejercicio1output():
    with open("./archivos_boletin11/ejercicio1.txt","r") as f:
        for i in f.readlines():
            print(i)
        f.close()

#ejercicio1input()
#ejercicio1output()


'''
Ejercicio 2
Ler un ficheiro de texto e contar cantas veces aparece cada palabra.
Solicita ao usuario o nome dun ficheiro .txt.


Mostra a frecuencia de cada palabra (ignorando maiúsculas/minúsculas e signos de puntuación).


Gárdase un resumo nun novo ficheiro resumo_palabras.txt
'''

def ejercicio2():
    ruta = str(input("Ingrese ruta: "))
    palabra = str(input("Ingrese palabra: "))
    with open(ruta, "r") as f:
        contador = 0
        for i in f.readlines():
            split = i.split(" ")
            for j in split:
                if j == palabra:
                    contador += 1
        f.close()

    print(f"La palabra se ha encontrado {contador} veces.")

#ejercicio2()

'''
Ejercicio 3
Crear unha aplicación para anotar tarefas para facer. A tarefa terá unha data, hora, duración, Nome da tarefa, descrición,  estado (feita, non feita). Para iso crear unha clase Tarefa que manexe os datos relacionados coa tarefa.  O usuario poderá facer as seguintes operacións:
Agregar unha nova tarefa.
Borrar unha tarefa.
Modificar unha tarefa.
Listar o listado de tarefas. 
As tarefas se gardarán nun ficheiro binario chamado tarefas.dat.

'''

def ejercicio3():
    class Tarea:
        def __init__(self, nombre, hora, duracion, descripcion, estado):
            self.setNombre(nombre)
            self.setHora(hora)
            self.setDuracion(duracion)
            self.setDescripcion(descripcion)
            self.setEstado(estado)

        def setNombre(self, nombre):
            if isinstance(nombre, str):
                self.__nombre = nombre
            else:
                raise TypeError("Error de tipo para nombre")
        def setHora(self, hora):
            if isinstance(hora, str):
                self.__hora = hora
            else:
                raise TypeError("Error de tipo para hora")
        def setDuracion(self, duracion):
            if isinstance(duracion, str):
                self.__duracion = int(duracion)
            elif isinstance(duracion, int):
                self.__duracion = duracion
            elif isinstance(duracion, float):
                self.__duracion = int(duracion)
            else:
                raise TypeError("Error de tipo para duracion")
        def setDescripcion(self, descripcion):
            if isinstance(descripcion, str):
                self.__descripcion = descripcion
            else:
                raise TypeError("Error de tipo para descripcion")
        def setEstado(self, estado):
            if isinstance(estado, str):
                if estado == "feita" or estado == "non feita":
                    self.__estado = estado
                else:
                    raise ValueError("Error de valor para estado")
            else:
                raise TypeError("Error de tipo para estado")

        def getNombre(self):
            return self.__nombre
        def getHora(self):
            return self.__hora
        def getDuracion(self):
            return self.__duracion
        def getDescripcion(self):
            return self.__descripcion
        def getEstado(self):
            return self.__estado

        def agregarTarea(self, tarea):
            if isinstance(tarea, str):
                self.__tarea = tarea
                with open("./archivos_boletin11/ejercicio3.txt", "a") as f:
                    f.write(str(tarea))
                    f.close()

            else:
                raise TypeError("Error de tipo para tarea")

        def borrarTarea(self, tarea):
            if isinstance(tarea, str):
                self.__tarea = tarea
                with open("./archivos_boletin11/ejercicio3.txt", "w") as f:
                    for i in f.readlines():
                        split = i.split(" ")
                        for j in split:
                            if j == tarea:
                                f.write("")
                    f.close()
            else:
                raise TypeError("Error de tipo para tarea")

        def modificarTarea(self, tarea, tareaNueva):
            if isinstance(tarea, str):
                self.__tarea = tarea
                with open("./archivos_boletin11/ejercicio3.txt", "w") as f:
                    for i in f.readlines():
                        split = i.split(" ")
                        for j in split:
                            if j == tarea:
                                f.write(tareaNueva)
                    f.close()
            else:
                raise TypeError("Error de tipo para tarea")

        def listarTareas(self):
            with open("./archivos_boletin11/ejercicio3.txt", "r") as f:
                print(f.readlines())

        def __str__(self):
            return str(self.__nombre)

        nombre = property(getNombre,setNombre)
        hora = property(getHora,setHora)
        duracion = property(getDuracion,setDuracion)
        descripcion = property(getDescripcion,setDescripcion)
        estado = property(getEstado,setEstado)

#ejercicio3()
'''
    Crea a aplicación que permita gardar e recuperar os datos dos clientes dunha empresa. Para o cal, defina a clase Cliente, que teña os atributos: 
id, identificador de cliente
nome
teléfono
	Os obxectos Cliente se recollerán nunha lista.
	A aplicación terá un menú que posibilitará as seguintes opcións:
Engadir novo cliente
Modificar datos
Dar de baixa clientes.
Listar os clientes.
	A información se gardará nun ficheiro binario, que cargará en memoria o iniciar o programa e se gardará en disco, actualizado o rematar. 

    '''
def ejercicio4():
    class Cliente:
        def __init__(self, nombre, identificador, telefono):
            self.nombre = nombre
            self.identificador = identificador
            self.telefono = telefono

        def __str__(self):
            return str(self.nombre)

        def anhadirCliente(self):
            with open("./archivos_boletin11/ejercicio4.txt", "a") as f:
                f.write(str(f"{self.nombre} {self.telefono} {self.identificador}"))
                f.close()

        def modificarCliente(self, nombre, antiguoNombre):
            with open("./archivos_boletin11/ejercicio4","w") as f:
                for i in f.readlines():
                    split = i.split(" ")
                    for j in split:
                        if j == antiguoNombre:
                            f.write(nombre)
                f.close()

#ejercicio4()
'''
Ejercicio 5
Realizar un programa para a xestión de Inventario. O programa ten que facer as seguintes operacións sobre un ficheiro CSV:
Calculo do valor total do inventario: Dado un ficheiro produtos.csv (con columnas: id, nome, prezo, stock), o programa ten realizar o cálculo (prezo × stock).
Existencias baixas: Crea un novo ficheiro baixo_stock.csv que conteña só os produtos cun número de existencias inferior a 5 unidades.
'''

def ejercicio5():
    def calculoInventario():
        with open("./archivos_boletin11/ejercicio5_productos.csv", "r") as f:
            total = 0
            for i in f.readlines():
                split = i.split(", ")
                total += int(split[2]) * int(split[3])
            f.close()
            return total
    print(calculoInventario())

#ejercicio5()


