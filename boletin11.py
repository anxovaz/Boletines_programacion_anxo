#Excepciones boletín 10

#Ejercicio 1
'''
1.  Dadas as clases mostradas no diagrama UML (Persoa, Deportista), codificar os métodos setter para que si o crear o obxecto do tipo persoa se introduce un DNI non válido xere unha excepción do tipo DniNonValido.
Codificar o metodo setLicenza para que verifique que o formato da licenza sexa  correcto. O formato da licenza (aaaadddnnnnnn)  é  da seguinte maneira :
aaaa, 4 números que representan o ano en curso.
ddd, abreviatura do deporte (fut fútbol, bal balocesto, etc).
nnnnnn, 6 números do número único de licenza.

'''

class Persona():
    def __init__(self,nombre,direccion,dni):
        self.setNombre(nombre)
        self.setDireccion(direccion)
        self.setDni(dni)

    #setters y getters

    def setNombre(self,nombre):
        if isinstance(nombre,str):
            self.nombre = nombre
        else:
            raise TypeError("Nombre debe ser una cadena de texto")

    def setDireccion(self,direccion):
        if isinstance(direccion,str):
            self.direccion = direccion
        else:
            raise TypeError("Direccion debe ser una cadena de texto")

    def setDni(self,dni):
        if isinstance(dni,str):
            if len(dni) == 9 and dni[-1].upper() in ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X","B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]:
                self.dni = dni
            else:
                raise ValueError("El dni debe contener 9 caracteres y el último un caracter")
        else:
            raise TypeError("DNI debe ser una cadena de texto")

    def getNombre(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def getDni(self):
        return self.dni


    nombre = property(getNombre,setNombre)
    direccion = property(getDireccion,setDireccion)
    dni = property(getDni,setDni)