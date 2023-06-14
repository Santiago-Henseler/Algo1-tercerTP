# Importo librerias
import csv
import os
import funciones_auxiliares as faux

DELIMITER = ";"
 
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
    
    escritor = csv.writer(archivo_escritura, delimiter=DELIMITER)
    
    if entrada[1].isnumeric():
        print("El nombre elegido es invalido")
    elif not entrada[2].isnumeric():
        print("La cantidad de personas elegida es invalida, tiene que ser un valor numerico")
    elif not faux.hora_valida(entrada[3]):
        print("La hora elegida es invalida, tiene que estar en formato HH:MM (24:60)") 
    elif not faux.ubicacion_valida(entrada[-1]):
        print("La ubicacion elegida es invalida")
    else:
        datos = []

        datos.append(len(archivo_lectura.readlines())+1)
        for i in entrada[1:]:
            datos.append(i)

        escritor.writerow(datos)

        print("Se agrego la reserva!") 

    archivo_escritura.close()
    archivo_lectura.close()

def listar(entrada):
    try:
        archivo_lectura = faux.abrir_archivo(faux.LECTURA, faux.ARCHIVO_ORIGINAL)
    except:
        print("error al abrir el archivo: datos.csv en formato de lectura")
        return
    
    lector = csv.reader(archivo_lectura, delimiter=DELIMITER)
    
    if  len(entrada) == 3 and not(entrada[1].isnumeric() and entrada[2].isnumeric()):
        print("Se debe especificar desde donde hasta donde con valores numericos")
        archivo_lectura.close()
        return
    
    for i in lector:
        if len(entrada) == 3:
            if int(i[0]) >= int(entrada[1]) and int(i[0]) <= int(entrada[2]):
                faux.mostrar_por_pantalla(i)  
        else:
            faux.mostrar_por_pantalla(i)

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
    
    escritor_aux = csv.writer(archivo_escritura_aux, delimiter=DELIMITER)
    lector = csv.reader(archivo_lectura, delimiter=DELIMITER)

    if not entrada[1].isnumeric():
        print("Error, el Id tiene que ser numerico")
        archivo_lectura.close()
        return
    else:
        existe_id = False
        for i in lector:
            if int(i[0]) != int(entrada[1]): 
                escritor_aux.writerow(i)
            if int(i[0]) == int(entrada[1]):
                existe_id = True
        if existe_id:      
            os.renames(faux.NOMBRE_ARCHIVO_AUXILIAR, faux.NOMBRE_ARCHIVO_ORIGINAL)
            print("Eliminado correctamete")
        else:
            os.remove(faux.NOMBRE_ARCHIVO_AUXILIAR)
            print("Id de reserva no existente")

    archivo_escritura_aux.close()
    archivo_lectura.close()

def modificar(entrada):
    try:
        archivo_lectura = faux.abrir_archivo(faux.LECTURA, faux.ARCHIVO_ORIGINAL)
    except:
        print("error al abrir el archivo: datos.csv en formato de lectura")
        return
    
    lector = csv.reader(archivo_lectura, delimiter=DELIMITER)

    if not entrada[1].isnumeric():
        print("Error, el Id tiene que ser numerico")
        archivo_lectura.close()
        return
    else:
        
        print("Parametros: nombre - acompañantes - hora - ubicacion")
        print("Que parametro desea modificar?(ademas agregar el valor)")
        valor_a_modificar = input()

        parametro = []

        parametro = valor_a_modificar.split(" ")
        
        if len(parametro) == 2: 
            if faux.parametro_modificar_validos(parametro[0]):
                try:
                    archivo_escritura_aux = faux.abrir_archivo(faux.ESCRITURA, faux.ARCHIVO_AUXILIAR)
                except:
                    archivo_lectura.close()
                    print("error al abrir el archivo: datos.csv en formato de escritura")
                    return

                escritor_aux = csv.writer(archivo_escritura_aux, delimiter=DELIMITER)
                
                existe_id = False

                for i in lector:
                    datos_modificados = i

                    if int(i[0]) == int(entrada[1]): 
                        if parametro[0] == faux.NOMBRE and not parametro[1].isnumeric():
                            datos_modificados.pop(1)
                            datos_modificados.insert(1, parametro[1])
                            print("Modificado correctamente")             
                        elif parametro[0] == faux.CANTIDAD_DE_PERSONAS and parametro[1].isnumeric():
                            datos_modificados.pop(2)
                            datos_modificados.insert(2, parametro[1])
                            print("Modificado correctamente")            
                        elif parametro[0] == faux.HORARIO and faux.hora_valida(parametro[1]):
                            datos_modificados.pop(3)
                            datos_modificados.insert(3, parametro[1])
                            print("Modificado correctamente")
                        elif parametro[0] == faux.UBICACION and faux.ubicacion_valida(parametro[1]):
                            datos_modificados.pop(4)
                            datos_modificados.insert(4, parametro[1])
                            print("Modificado correctamente")
                        else:
                            print("valor a modificar erroneo")

                    escritor_aux.writerow(datos_modificados)
                     
                    if int(i[0]) == int(entrada[1]):
                        existe_id = True

                if existe_id:
                    archivo_lectura.close()
                    archivo_escritura_aux.close()
                    os.renames(faux.NOMBRE_ARCHIVO_AUXILIAR, faux.NOMBRE_ARCHIVO_ORIGINAL)
                    return
                else:
                    print("Id seleccionado invalido")
                    archivo_lectura.close()
                    archivo_escritura_aux.close()
                    os.remove(faux.NOMBRE_ARCHIVO_AUXILIAR)
                    return

            else:
                archivo_lectura.close()
                print("Parametro inexistente, los parametros a usar son:")
                print("       -->nombre")
                print("       -->acompañantes")
                print("       -->hora")
                print("       -->ubicacion")
                return
        else:
            archivo_lectura.close()
            print("Cantidad de parametros erronea, se pide campo a modificar y valor a modificar")
            return         
    archivo_lectura.close()
    archivo_escritura_aux.close()

if __name__ == "__main__":
    print("####################################")
    print("###### Bibloteca: comandos.py ######")
    print("####################################")
    print("  -->Funciones:")
    print("       -->Agregar:")
    print("              * Pre condicion: Necesita recibir un vector con 5 valores")
    print("              * Post condicion: Añade la reserva al archivo datos.csv si es valida")
    print("       -->Listar:")
    print("              * Pre condicion: Necesita recibir un vector con 1 o 3 valores (el segundo y el tercero debe ser numericos)")
    print("              * Post condicion: Si se envia 3 valores, muestra por pantalla las reservas >= al valor 2 y <= al valor 3; sino, muestra todas por pantalla ")
    print("       -->Eliminar:")
    print("              * Pre condicion: Necesita recibir un vector con 2 valores (el segundo debe ser numerico)")
    print("              * Post condicion: Elimina del archivo datos.csv la reserva con el id indicado")
    print("       -->Modificar:")
    print("              * Pre condicion: Necesita recibir un vector con 2 valores (el segundo debe ser numerico)")
    print("              * Post condicion: Modifica un valor de una reserva")
    print("####################################")
    print("####################################")