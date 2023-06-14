# Declaracion de constantes
AFUERA = "F"
ADENTRO = "A"

ESCRITURA = "a"
LECTURA = "r"
ARCHIVO_ORIGINAL = "original"
NOMBRE_ARCHIVO_ORIGINAL = "datos.csv"
ARCHIVO_AUXILIAR = "aux"
NOMBRE_ARCHIVO_AUXILIAR = "aux.csv"

NOMBRE = "nombre"
CANTIDAD_DE_PERSONAS = "acompañantes"
HORARIO = "hora"
UBICACION = "ubicacion"

def ubicacion_valida(ubicacion):
    rta = False
    
    if ubicacion == ADENTRO or ubicacion == AFUERA:
        rta = True

    return rta

def hora_valida(horario):
    rta = False

    if len(horario) == 5:
        if horario[2] == ":":
            
            hora = horario[0:2]
            minutos = horario[3:5]
            
            if len(hora) == 2 and len(minutos) == 2 and hora.isnumeric() and minutos.isnumeric() and int(hora) <= 24 and int(minutos) <= 60:
                rta = True

    return rta

def abrir_archivo(type, archivo):

    if archivo == ARCHIVO_ORIGINAL:
        return open(NOMBRE_ARCHIVO_ORIGINAL, type)
    elif archivo == ARCHIVO_AUXILIAR:
        return open(NOMBRE_ARCHIVO_AUXILIAR, type) 
    
def parametro_modificar_validos(parametro):
    return parametro == NOMBRE or parametro == CANTIDAD_DE_PERSONAS or parametro == HORARIO or parametro == UBICACION

def mostrar_por_pantalla(reserva):
    print(f"ID: {reserva[0]}")
    print(f"Reserva a nombre de: {reserva[1]}")
    print(f"Cantidad de comensales: {reserva[2]}")
    print(f"Horario de la reserva: {reserva[3]}")
    print(f"Ubicacion de la mesa: {reserva[4]}")
    print("\n")
    print("<----------------------------------->")
    print("\n")

if __name__ == "__main__":
    print("###############################################")
    print("###### Bibloteca: funciones_auxiliares.py ######")
    print("###############################################")
    print("  -->Funciones:")
    print("       -->ubicacion_valida:")
    print("              * Pre condicion: -")
    print("              * Post condicion: Añade la reserva al archivo datos.csv si es valida")
    print("       -->hora_valida:")
    print("              * Pre condicion: -")
    print("              * Post condicion: Devulve True si la hora es valida")
    print("       -->abrir_archivo:")
    print("              * Pre condicion: Necesita recibir la forma de abrir el archivo y el archibo a abrir")
    print("              * Post condicion: Abre el archivo indicado")
    print("       -->parametro_modificar_validos:")
    print("              * Pre condicion: -")
    print("              * Post condicion: Devulve true si es un parametro valido")
    print("       -->mostrar_por_pantalla:")
    print("              * Pre condicion: Necesita recibir una reserva")
    print("              * Post condicion: Muestra por pantalla una reserva con formato agradable")
    print("###############################################")
    print("###############################################")