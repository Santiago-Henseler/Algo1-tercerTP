# Importo librerias
import csv
import funciones_auxiliares as faux
 
def agregar(entrada):
    try:
        archivo_escritura = faux.abrir_archivo("a")
    except:
        print("error al abrir el archivo: datos.csv en formato de escritura")
        return
    try:
        archivo_lectura = faux.abrir_archivo("r")
    except:
        archivo_escritura.close()
        print("error al abrir el archivo: datos.csv en formato de lectura")
        return
    
    escritor = csv.writer(archivo_escritura, delimiter=";")

    if faux.ubicacion_valida(entrada[-1]) and faux.hora_valida(entrada[3]) and entrada[2].isnumeric() and not entrada[1].isnumeric():
        datos = []

        datos.append(len(archivo_lectura.readlines()))
        for i in entrada[1:]:
            datos.append(i)

        escritor.writerow(datos)

        print("Se agrego la reserva!")

    elif not faux.ubicacion_valida():
        print("La ubicacion elegida es invalida")
    elif not faux.hora_valida():
        print("La hora elegida es invalida") 
    elif not entrada[2].isnumeric():
        print("La cantidad de personas elegida es invalida")
    elif entrada[1].isnumeric():
        print("El nombre elegido es invalido") 

    archivo_escritura.close()
    archivo_lectura.close()

def listar(entrada):
    try:
        archivo_lectura = faux.abrir_archivo("r")
    except:
        print("error al abrir el archivo: datos.csv en formato de lectura")
        return
    
    lector = csv.reader(archivo_lectura, delimiter=";")

    if len(entrada) == 3:
        minimo = int(entrada[1])
        maximo = int(entrada[2])
    elif len(entrada) == 1:
        minimo = 0
        maximo = len(archivo_lectura.readlines())
        print(maximo)

    for i in lector:
        if int(i[0]) >= minimo and int(i[0]) <= maximo:
            print(f"ID: {i[0]}")
            print(f"Reserva a nombre de: {i[1]}")
            print(f"Cantidad de comensales: {i[2]}")
            print(f"Horario de la reserva: {i[3]}")
            print(f"Ubicacion de la mesa: {i[4]}")
            print("\n")
            print("<----------------------------------->")
            print("\n")


def eliminar():
    pass


def modificar():
    pass