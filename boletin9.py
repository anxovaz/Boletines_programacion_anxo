"""
Ejercicio 1
Crea unha clase chamada Libro que conteña os seguintes atributos:
titulo autor ano numPaginas valoracion

A clase debe de ter o método de inicialización.
Establecer os métodos de acceso para todos os atributos (geters). 
Crear os métodos de asignación dos atributos (seters)
Establecer as propiedades de forma que só se poida acceder os atributos mediante os métodos adicados a elo (geters e seters).
Codificar o metodo amosarLibro, que devolte unha cadea e visualiza tódalas característica dun libro. 
Crear unha clase Principal co método main. Crear un libro con cada construtor e mostrar por consola a súa información. 
"""

class Libro:
    def __init__(self,titulo,autor, anho,numPaginas,valoracion):
        self.setTitulo(titulo)
        self.setAutor(autor)
        self.setAnho(anho)
        self.setNumPaginas(numPaginas)
        self.setValoracion(valoracion)

    #setters
    def setTitulo(self,titulo):
        if isinstance(titulo,str):
            self.__titulo = titulo
        else:
            self.__titulo = None

    def setAutor(self,autor):
        if isinstance(autor,str):
            self.__autor = autor
        else:
            self.__autor = None

    def setAnho(self,anho):
        if (isinstance(anho,str) and anho.isnumeric()) or isinstance(anho,int) or isinstance(anho, float): #comprueba si es un string y si es un string que contenga únicamente números, o que sea int o float
            self.__anho = int(anho) #lo combierte a int
        else:
            self.__anho = None

    def setNumPaginas(self,numPaginas):
        if (isinstance(numPaginas, str) and numPaginas.isnumeric()) or isinstance(numPaginas, int) or isinstance(numPaginas, float):
            self.__numPaginas = int(numPaginas)
        else:
            self.__numPaginas = None

    def setValoracion(self,valoracion):
        if isinstance(valoracion, float):
            self.__valoracion = float(valoracion) #las valoraciones generalmente llevan decimales, ej: 7.5/10
        else:
            self.__valoracion = None

    #getters
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getAnho(self):
        return self.__anho
    def getNumPaginas(self):
        return self.__numPaginas
    def getValoracion(self):
        return self.__valoracion

    #métodos
    def amosarLibro(self):
        return self.__str__()

    def __str__(self):
        return "Libro: " + str(self.__titulo) + "\nAutor: " + str(self.autor) + "\nAño: " + str(self.__anho) + "\nNúmero de páginas: " + str(self.__numPaginas) + "\nValoración: " + str(self.__valoracion)


    #aqui se asignan los seters y getters
    titulo = property(getTitulo,setTitulo)
    autor = property(getAutor,setAutor)
    anho = property(getAnho,setAnho)
    numPaginas = property(getNumPaginas,setNumPaginas)
    valoracion = property(getValoracion,setValoracion)


"""
Ejercicio 2
Implementa unha clase consumo, que forma parte da centralita electrónica dun coche e ten as seguintes características :
Atributos :
km kilómetros percorridos polo coche
litros Litros de combustible consumidos
vMed velocidade media 
pGas Prezo da gasolina

Metodos :
Un método que inicializa os valores dos atributos
getTempo Indica o tempo empregado en realizar a viaxe
consumoMedio consumo medio do vehículo (en litros cada 100 km )
consumoEuros consumo medio (en € cada 100 km )
setKms modifica o valor dos km
setLitros actualiza a cantidade de litros
setvMed actualiza o valor da vMed
setPGas actualiza o valor do pGas
Na clase principal :
Crea un obxecto, de tipo consumo.
Dalle a litros o valor 50 e a prezo da gasolina 1.57
Crea un obxecto, tipo consumo, utilizando o constructor con tódolos parámetros 
Visualiza, a través do 2º obxecto, o consumo medio 
Varia o valor dos litros consumidos do 2º obxecto.
Visualiza a velocidade media do 2º obxecto
"""

class Consumo():
    def __init__(self,km,litros,vMed,pGas):
        self.setKms(km)
        self.setLitros(litros)
        self.setvMed(vMed)
        self.setPGas(pGas)

    #funcion para comprobar los tipos de variables
    def __comprobarTipoVariable(self,variable):
        if isinstance(variable,float) or isinstance(variable,int) or (isinstance(variable,str) and variable.isnumeric()):
            return True
        else:
            return False
    #setters
    def setKms(self,km):
        if self.__comprobarTipoVariable(km):
            self.__km = km
        else:
            self.__km = None

    def setLitros(self,litros):
        if self.__comprobarTipoVariable(litros):
            self.__litros = litros
        else:
            self.__litros = None

    def setvMed(self,vMed):
        if self.__comprobarTipoVariable(vMed):
            self.__vMed = vMed
        else:
            self.__vMed = None

    def setPGas(self,pGas):
        if self.__comprobarTipoVariable(pGas):
            self.__pGas = pGas
        else:
            self.__pGas = None

    #getters
    def getKms(self):
        return self.__km
    def getLitros(self):
        return self.__litros
    def getvMed(self):
        return self.__vMed
    def getPGas(self):
        return self.__pGas

    def getTempo(self):
        #t=distancia/vel media
        return self.__km/self.__litros

    def consumoMedio(self):
        #__km ------ litros
        #100  ------ x
        return (100 * self.__litros)/self.__km

    def consumoEuros(self):
        return self.consumoMedio() * self.__pGas



if __name__ == "__main__":
    print("---- Ejercicio 1 ----")
    libro1 = Libro("Titulo1","autor1","2025", 200, 2.5)
    print(libro1.amosarLibro())
    print("\n")
    libro1.autor = 1234
    print(libro1.amosarLibro())

    print("---- Ejercicio 2 ----")
    consumo1 = Consumo(60,5,80, 1.5)
    print(consumo1.consumoMedio())
    print(consumo1.consumoEuros())




