# Declaracion de constantes
AFUERA = "F"
ADENTRO = "A"

ESCRITURA = "a"
LECTURA = "r"
ARCHIVO_ORIGINAL = "original"
ARCHIVO_AUXILIAR = "aux"

def ubicacion_valida(ubicacion):
    rta = False
    
    if ubicacion == ADENTRO or ubicacion == AFUERA:
        rta = True

    return rta

def hora_valida(hora):
    return True

def abrir_archivo(type, archivo):

    if archivo == ARCHIVO_ORIGINAL:
        return open("datos.csv", type)
    elif archivo == ARCHIVO_AUXILIAR:
        return open("aux.csv", type) 
    

if __name__ == "__main__":
    print("###############################################")
    print("###### Bibloteca: funciones_auxiliares.py ######")
    print("###############################################")
    print("  -->Funciones:")
    print("       -->ubicacion_valida:")
    print("              * Pre condicion: Necesita recibir un array con 5 elementos")
    print("              * Post condicion: Añade la reserva al archivo datos.csv si es valida")
    print("       -->hora_valida:")
    print("              * Pre condicion:")
    print("              * Post condicion:")
    print("       -->abrir_archivo:")
    print("              * Pre condicion:")
    print("              * Post condicion:")
    print("       -->Modificar:")
    print("              * Pre condicion:")
    print("              * Post condicion:")
    print("###############################################")
    print("###############################################")