# Declaracion de constantes
AFUERA = "F"
ADENTRO = "A"

def ubicacion_valida(ubicacion):
    rta = False
    
    if ubicacion == ADENTRO or ubicacion == AFUERA:
        rta = True

    return rta

def hora_valida(hora):
    return True

def abrir_archivo(type):
    if type == "a":
        return open("datos.csv", "a")
    elif type == "r":
        return open("datos.csv", "r")
   