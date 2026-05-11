#Excepciones boletín 10
#Ejercicio 1
class Persona():
    def __init__(self, nombre, direccion, dni):
        self.setNombre(nombre)
        self.setDireccion(direccion)
        self.setDni(dni)

    def setNombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise TypeError("Nombre inválido")

    def setDireccion(self, direccion):
        if isinstance(direccion, str):
            self.__direccion = direccion
        else:
            raise TypeError("Dirección inválida")

    def setDni(self, dni):
        if isinstance(dni, str):
            if len(dni) != 9 or (not dni[:8].isnumeric()) or (not dni[8:] in ["A", "B", "C", "D", "E", "F"]):
                raise ValueError("Introduce un dni válido")
            else:
                self.__dni = dni


    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getDni(self):
        return self.__dni

    nombre = property(getNombre, setNombre)
    direccion = property(getDireccion, setDireccion)
    dni = property(getDni, setDni)

class Deportista(Persona):
    def __init__(self, nombre, direccion, dni, deporte, club, licencia):
        super().__init__(nombre, direccion, dni)
        self.setDeporte(deporte)
        self.setLicencia(licencia)
        self.setClub(club)

    def setDeporte(self, deporte):
        if isinstance(deporte, str):
            self.__deporte = deporte
        else:
            raise TypeError("Valor no soportado")

    def setLicencia(self, licencia): #0000fut000000
        if isinstance(licencia, str):
            if len(licencia) == 13:
                if licencia[:4].isnumeric() and licencia[4:7] in ["fut", "bal", "ten", "tae"] and licencia[7:].isnumeric():
                    self.__licencia = licencia
                else:
                    raise ValueError("Formato incorreto")

            else:
                raise ValueError("Formato incorrecto")
        else:
            raise TypeError("Valor no soportado")

    def setClub(self, club):
        if isinstance(club, str):
            self.__club = club
        else:
            raise TypeError("Valor no soportado")


    def getDeporte(self):
        return self.__deporte
    def getLicencia(self):
        return self.__licencia
    def getClub(self):
        return self.__club

    def __str__(self):
        #se accede a los atributos mediante los getters
       return (f"Nombre: {self.nombre}, " f"Direccion: {self.direccion}, " f"Dni: {self.dni}, " f"Licencia: {self.licencia}, " f"Club: {self.club}, " f"Deporte: {self.deporte}")

    deporte = property(getDeporte, setDeporte)
    licencia = property(getLicencia, setLicencia)
    club = property(getClub, setClub)

#Ejercicio 2
class Data():
    def __init__(self, dia, mes, anho):
        self.setMes(mes)
        self.setAnho(anho)
        self.setDia(dia)

    def setAnho(self, anho):
        if isinstance(anho, int):
            self.__anho = anho
        elif isinstance(anho, str):
            if anho.isnumeric():
                self.__anho = int(anho)
            else:
                raise ValueError("Anho incorrecto")
        elif isinstance(anho, float):
            self.__anho = int(anho)
        elif isinstance(anho, list) or isinstance(anho, tuple):
            if len(anho) == 1 and anho[0].isnumeric():
                self.__anho = anho[0]
            else:
                raise ValueError("Anho incorrecto")
        else:
            raise TypeError("Anho incorrecto, tipo incorrecto")

    def setMes(self, mes):
        if isinstance(mes, str):
            if mes.isnumeric():
                self.__mes = int(mes)
            else:
                raise ValueError("Formato incorreto, los meses tienen que estar entre 1 y 12")
        elif isinstance(mes, int):
            if mes <= 12 and mes > 0:
                self.__mes = mes
            else:
                raise ValueError("Valor incorreto, los meses tienen que estar entre 1 y 12")
        elif isinstance(mes, float):
            if mes <= 12 and mes > 0:
                self.__mes = int(mes)
            else:
                raise ValueError("Valor incorreto, los meses tienen que estar entre 1 y 12")
        elif isinstance(mes, list) or isinstance(mes, tuple):
            if len(mes) == 1:
                self.__mes = int(mes[0])
            else:
                raise ValueError("Valor incorreto, los meses tienen que estar entre 1 y 12")
        else:
            raise TypeError("Tipo de dato incorrecto para mes")

    def setDia(self, dia):
        if isinstance(dia, str):
            if dia.isnumeric():
                posibleDia = int(dia)
            else:
                raise ValueError("Dia incorrecto, introduce un número")
        elif isinstance(dia, int):
            posibleDia = dia
        elif isinstance(dia, float):
            posibleDia = int(dia)
        elif isinstance(dia, list) or isinstance(dia, tuple):
            if len(dia) == 1:
                posibleDia = int(dia[0])
            else:
                raise ValueError("Dia incorrecto, introduce un número")
        else:
            raise TypeError("Tipo de dato incorrecto para dia")

        if self.__mes in [1,3,5,7,8,10,12]: #31 dias
            if posibleDia <= 31 and posibleDia > 0:
                self.__dia = posibleDia
            else:
                raise ValueError("Dia incorrecto")
        elif self.__mes in [4,6,9,11]: #30 dias
            if posibleDia <= 30 and posibleDia > 0:
                self.__dia = posibleDia
            else:
                raise ValueError("Dia incorrecto")
        else: #febrero
            if self.__esBisiesto(self.__anho):
                if posibleDia <= 29 and posibleDia > 0:
                    self.__dia = posibleDia
                else:
                    raise ValueError("Dia incorrecto para febrero")
            else:
                if posibleDia <= 28 and posibleDia > 0:
                    self.__dia = posibleDia
                else:
                    raise ValueError("Dia incorrecto para febrero")

    def __esBisiesto(self, anho):
        return (self.__anho % 4 == 0 and self.__anho % 100 != 0) or (self.__anho % 400 == 0)

    def getDia(self):
        return self.__dia
    def getMes(self):
        return self.__mes
    def getAnho(self):
        return self.__anho

    def __str__(self):
        return f"Dia: {self.__dia}, Mes: {self.__mes}, Anho: {self.__anho}"

    dia = property(getDia, setDia)
    mes = property(getMes, setMes)
    anho = property(getAnho, setAnho)

if __name__ == '__main__':
    print("--- Ejercicio 1 ---")
    persona = Deportista("Paco", "Calle imaginaria 1", "11111111A", "futbol", "club1", "1111fut111111")
    print(persona)

    print("--- Ejercicio 2 ---")
    dia = Data(29.9, "2", 2024)
    print(dia)




