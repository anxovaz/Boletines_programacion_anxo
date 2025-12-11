"""
Ejercicio 1
Crea unha clase chamada Libro que conteña os seguintes atributos:
titulo autor ano numPaginas valoracion

A clase debe de ter o metodo de inicialización.
Establecer os métodos de acceso para todos os atributos (geters). 
Crear os métodos de asignación dos atributos (seters)
Establecer as propiedades de forma que só se poida acceder os atributos mediante os métodos adicados a elo (geters e seters).
Codificar o metodo amosarLibro, que devolte unha cadea e visualiza tódalas característica dun libro. 
Crear unha clase Principal co metodo main. Crear un libro con cada construtor e mostrar por consola a súa información.
"""

class Libro:
    def __init__(self,titulo,autor, anho,numPaginas,valoracion):
        #los setters se encargan de inicializar las variables
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

    def consumoEuros(self): #consumo medio * precio gasolina
        return self.consumoMedio() * self.__pGas

"""
class Coche: 
def __init__(self):
self.velocidade =0 


Engade a clase Coche os seguintes métodos:
getVelocidade() . Este método devolve a velocidade actual
acelerar (valor). Este método incrementa a velocidade na cantidade valor.
frenar (menos). Este método diminue a velocidade na cantidade menos.
Crea unha clase Boletin 9_3 para comprobar que o programa execútase ben, dandolle os valores que precises.

"""
class Coche():
    def __init__(self):
        self.velocidade = 0

    def getVelocidade(self): #devuelve la velocidad
        return self.velocidade
    def acelerar(self,incremento):
        self.velocidade += incremento
    def frenar(self,decremento):
        self.velocidade -= decremento

class Boletin9_3():
    def main(self):
        coche1 = Coche() #declaro coche sin nada, ya que el ejercicio no indica introducir una velocidad inicial en el __init__ de la clase
        coche1.acelerar(100)
        coche1.frenar(20)
        print(coche1.getVelocidade()) #da 80


"""4. Escribe unha clase Conta para representar unha conta bancaria. Os datos da conta son:
Atributos : 
Nome do cliente. 
Número de conta.
Tipo de interese.
Saldo.

A clase conterá os seguintes métodos:
Método inicializador.
Métodos setters/ getters para asignar e obter os datos da conta.
Establecer as propiedades de forma que só se poida acceder os atributos mediante os métodos adicados a elo (geters e seters).
Métodos de ingreso. Un ingreso consiste en aumentar o saldo na cantidade que se indique. 
Métodos de reintegro. Un reintegro consiste en diminuír o saldo nunha cantidade. A cantidade non pode ser negativa. 
Método transferencia que permita pasar diñeiro dunha conta a outra Exemplo de uso do método transferencia:
 contaOrigen.transferencia( contaDestino, importe),  que indica que queremos facer unha transferencia desde contaOrigen a contaDestino do importe indicado.
Proba o funcionamento da clase Conta na clase principal.
"""

class Cuenta():
    def __init__(self, nombre, numero, tipo, saldo):
        #los setters inicializan las variables
        self.setNombre(nombre)
        self.setNumero(numero)
        self.setTipo(tipo)
        self.setSaldo(saldo)
    def setNombre(self,nombre):
        if isinstance(nombre,str):
            self.__nombre = nombre
        else:
            self.__nombre = None

    def setNumero(self,numero):
        if isinstance(numero,str):
            self.__numero = numero
        else:
            self.__numero = None

    def setTipo(self,tipo):
        if isinstance(tipo,str) or isinstance(tipo,int):
            self.__tipo = float(tipo)
        elif isinstance(tipo,float):
            self.__tipo = tipo
        else:
            self.__tipo = None

    def setSaldo(self,saldo):
        if isinstance(saldo,str) or isinstance(saldo,int):
            self.__saldo = float(saldo)
        elif isinstance(saldo,float):
            self.__saldo = saldo
        else:
            self.__saldo = None

    def getNombre(self):
        return self.__nombre
    def getNumero(self):
        return self.__numero
    def getTipo(self):
        return self.__tipo
    def getSaldo(self):
        return self.__saldo

    def ingreso(self,cantidad):
        self.saldo += cantidad
    def reintegro(self,cantidad):
        if self.__saldo >= cantidad:
            self.saldo -= cantidad
            return True
        else: #no se puede restar ya que no puede quedar en negativo
            return False

    def transferencia(self,contaDestino,importe):
        if self.reintegro(importe): #comprueba que al usuario se le pueda sacar dinero de la cuenta y se lo quita si devuelve true
            contaDestino.ingreso(importe)#le agrega el dinero

    def __str__(self):
        return "Nombre: " + str(self.__nombre) + "\nNúmero de cuenta: " + str(self.__numero) + "\nSaldo: " + str(self.__saldo) + "\nTipo interés:" + str(self.__tipo)

    nombre = property(getNombre,setNombre)
    numero = property(getNumero,setNumero)
    tipo = property(getTipo,setTipo)
    saldo = property(getSaldo,setSaldo)

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

    print("---- Ejercicio 3 ----")
    Boletin9_3().main()

    print("---- Ejercicio 4 ----")
    cuenta1 = Cuenta("Nombre1","0000 0000 0000 0000", 5, 50)
    cuenta2 = Cuenta("Nombre2", "0000 0000 0000 0001", 5, 50)
    cuenta1.transferencia(cuenta2,50)
    print(cuenta1)
    print("---")
    print(cuenta2)

