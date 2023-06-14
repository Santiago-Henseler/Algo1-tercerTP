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
    if len(entrada) > 0:
        if entrada[0] == ADD:
            if len(entrada) == 5:
                comandos.agregar(entrada)
            else:
                print("Cantidad de valores invalida, los valores a agregar son:")
                print("       -->nombre")
                print("       -->acompañantes")
                print("       -->hora")
                print("       -->ubicacion")
                return
        elif entrada[0] == MODIFY:
            if len(entrada) == 2:
               comandos.modificar(entrada)
            else:
                print("Cantidad de parametros invalidos")
        elif entrada[0] == DELET:
            if len(entrada) == 2:
                comandos.eliminar(entrada)
            else:
                print("Cantidad de parametros invalidos")
                return
        elif entrada[0] == LIST:
            if len(entrada) == 1 or len(entrada) == 3:
                comandos.listar(entrada)
            else:
                print("Cantidad de parametros invalidos")
                return
        else:
            print("Comando inexistente, los comando a usar son:")
            print("       -->Agregar")
            print("       -->Listar")
            print("       -->Eliminar")
            print("       -->Modificar")
    else:
        print("Comando no especificado, los comando a usar son:")
        print("       -->Agregar")
        print("       -->Listar")
        print("       -->Eliminar")
        print("       -->Modificar")
        return  

main()