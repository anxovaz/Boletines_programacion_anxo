class Tarea:
    def __init__(self, fecha, hora, duracion, nombreTarea, descripcion, estado):
        self.fecha = fecha
        self.hora = hora
        self.duracion = duracion
        self.nombreTarea = nombreTarea
        self.estado = estado
        self.descripcion = descripcion

    @property
    def fecha(self):
        return self.__fecha
    @property
    def hora(self):
        return self.__hora
    @property
    def duracion(self):
        return self.__duracion
    @property
    def nombreTarea(self):
        return self.__nombreTarea
    @property
    def estado(self):
        return self.__estado
    @property
    def descripcion(self):
        return self.__descripcion


    @fecha.setter
    def fecha(self, fecha):
        if isinstance(fecha, str):
            self.__fecha = fecha
        else:
            raise TypeError('Fecha no valida')
    @hora.setter
    def hora(self, hora):
        if isinstance(hora, str):
            self.__hora = hora
        elif isinstance(hora, int) or isinstance(hora, float):
            if hora >= 0 and hora <= 23:
                self.__hora = str(hora)
            else:
                raise ValueError('Hora no valida')
        else:
            raise TypeError('Hora no valida')
    @duracion.setter
    def duracion(self, duracion):
        if isinstance(duracion, str) or isinstance(duracion, int) or isinstance(duracion, float):
            self.__duracion = int(duracion)
        else:
            raise TypeError("Duracion no valida")
    @nombreTarea.setter
    def nombreTarea(self, nombreTarea):
        if isinstance(nombreTarea,str):
            self.__nombreTarea = nombreTarea
        else:
            raise TypeError('Nombre no valida')
    @estado.setter
    def estado(self, estado):
        if isinstance(estado, str):
            if estado.lower() == "completada" or estado.lower() == "no completada":
                self.__estado = estado.lower()
            else:
                raise ValueError('Estado no valida')
        else:
            raise TypeError('Estado no valida')

    @descripcion.setter
    def descripcion(self, descripcion):
        if isinstance(descripcion, str):
            self.__descripcion = descripcion
        else:
            raise TypeError('Descripcion no valida')


    def __str__(self):
        return f"Nombre Tarea:{self.__nombreTarea}\nFecha:{self.__fecha}\nHora:{self.__hora}\nDuracion:{self.__duracion}\nEstado:{self.__estado}\nDescripcion:{self.__descripcion}"

#Tests
if __name__ == '__main__':
    tarea1 = Tarea("11/1/2001","3", 10,"tarea1","Descripcion tarea 1","No completada")
    print(tarea1)