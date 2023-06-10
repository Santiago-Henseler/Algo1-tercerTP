# Importo librerias
import csv
import os
import funciones_auxiliares as faux
 
def agregar(entrada):
    try:
        archivo_escritura = faux.abrir_archivo(faux.ESCRITURA, faux.ARCHIVO_ORIGINAL)
    except:
        print("error al abrir el archivo: datos.csv en formato de escritura")
        return
    try:
        archivo_lectura = faux.abrir_archivo(faux.LECTURA, faux.ARCHIVO_ORIGINAL)
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
        archivo_lectura = faux.abrir_archivo(faux.LECTURA, faux.ARCHIVO_ORIGINAL)
    except:
        print("error al abrir el archivo: datos.csv en formato de lectura")
        return
    
    minimo = 0
  # maximo = len(archivo_lectura.readlines()) #tirar error aca anda a saberr

    lector = csv.reader(archivo_lectura, delimiter=";")

    if len(entrada) == 3:
        minimo = int(entrada[1])
        maximo = int(entrada[2])

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
    archivo_lectura.close()

def eliminar(entrada):
    try:
        archivo_lectura = faux.abrir_archivo(faux.LECTURA, faux.ARCHIVO_ORIGINAL)
    except:
        print("error al abrir el archivo: datos.csv en formato de lectura")
        return
    try:
        archivo_escritura_aux = faux.abrir_archivo(faux.ESCRITURA, faux.ARCHIVO_AUXILIAR)
    except:
        archivo_lectura.close()
        print("error al abrir el archivo: datos.csv en formato de escritura")
        return
    
    escritor_aux = csv.writer(archivo_escritura_aux, delimiter=";")
    lector = csv.reader(archivo_lectura, delimiter=";")

    ids = []

    for i in lector:
        ids.append(int(i[0]))

    if not entrada[1].isnumeric():
        print("Error, el Id tiene que ser numerico")
    elif int(entrada[1]) in ids:
        for i in lector:   # error aca
            if int(i[0]) != int(entrada[1]):  
                escritor_aux.writerow(i)
        #os.renames("aux.csv", "datos.csv")
        print("Eliminado correctamete")
    else:
        print("Id de reserva no existente")

    archivo_escritura_aux.close()
    archivo_lectura.close()

def modificar():
    pass

if __name__ == "__main__":
    print("####################################")
    print("###### Bibloteca: comandos.py ######")
    print("####################################")
    print("  -->Funciones:")
    print("       -->Agregar:")
    print("              * Pre condicion: Necesita recibir un array con 5 elementos")
    print("              * Post condicion: Añade la reserva al archivo datos.csv si es valida")
    print("       -->Listar:")
    print("              * Pre condicion:")
    print("              * Post condicion:")
    print("       -->Eliminar:")
    print("              * Pre condicion:")
    print("              * Post condicion:")
    print("       -->Modificar:")
    print("              * Pre condicion:")
    print("              * Post condicion:")
    print("####################################")
    print("####################################")