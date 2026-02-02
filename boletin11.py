#Ficheros boletín 11

'''Ejercicio 1
Crear un programa xestor de notas persoais, que permita ao usuario gardar e consultar notas.
O usuario pode engadir unha nova nota (texto libre).


As notas gárdanse nun ficheiro de texto (notas.txt), unha por liña.


O programa pode listar todas as notas gardadas.


O usuario pode buscar notas que conteñan unha palabra clave.
'''

def ejercicio1():
    with open('./archivos_boletin11/ejercicio1.txt',"w") as f:
        inputUsuario = str(input("Ingrese su nota: "))
        f.write(inputUsuario)
        f.close()

ejercicio1()
