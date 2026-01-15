#Exceptions
print("Ejercicio 1")
class Persona():
    def __init__(self, nombre, direccion, dni):
        self.setNombre(nombre)
        self.setDireccion(direccion)
        self.setDni(dni)

    def setNombre(self, nombre):
        if isinstance(nombre, str):
            self.nombre = nombre
        else:
            raise TypeError("Nombre inválido")

    def setDireccion(self, direccion):
        if isinstance(direccion, str):
            self.direccion = direccion
        else:
            raise TypeError("Dirección inválida")

    def setDni(self, dni):
        if isinstance(dni, str):
            if len(dni) != 9:
                raise ValueError("Introduce un dni válido")


    def getNombre(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def getDni(self):
        return self.dni

    nombre = property(getNombre, setNombre)
    direccion = property(getDireccion, setDireccion)
    dni = property(getDni, setDni)
