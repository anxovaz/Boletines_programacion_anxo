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




if __name__ == '__main__':
    print("--- Ejercicio 1 ---")
    persona = Deportista("Paco", "Calle imaginaria 1", "11111111A", "futbol", "club1", "1111fut111111")
    print(persona)

    print("--- Ejercicio 2 ---")




