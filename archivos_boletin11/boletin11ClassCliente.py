class Cliente:
    def __init__(self, id, nombre, telefono):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def telefono(self):
        return self.__telefono

    @id.setter
    def id(self, id):
        if isinstance(id, str):
            if len(id) == 4:
                self.__id = id
            else:
                raise ValueError
        else:
            raise TypeError

    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise TypeError

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):
        return f"Nombre:{self.__nombre}\nTelefono:{self.__telefono}\nid:{self.__id}"