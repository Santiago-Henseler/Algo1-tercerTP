# Importo librerias
import sys
import comandos

# Declaracion de constantes (aunque en pytho no existan, las siguientes variables que declare las considerare constantes) #

ADD = "agregar"
MODIFY = "modificar"
DELET = "eliminar"
LIST = "listar"

def main():
    entrada = sys.argv[1:]

    if entrada[0] == ADD:
        if len(entrada) == 5:
            comandos.agregar(entrada)
        else:
            print("Cantidad de parametros invalidos")
            return

    if entrada[0] == MODIFY:
        comandos.modificar(entrada)

    if entrada[0] == DELET:
        comandos.eliminar(entrada)

    if entrada[0] == LIST:
        if len(entrada) == 1 or len(entrada) == 3:
            comandos.listar(entrada)
        else:
            print("Cantidad de parametros invalidos")
            return
        

main()