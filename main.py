import sys
# - Importo todas las funciones del archivo utils.py
import utils

# - Función principal
if __name__ == "__main__":
    # ? Verifico si se proporcionó un comando como argumento
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        # ? Si el comando es 'tareas', llamo a la función listar_tareas()
        if comando == "tareas":
            utils.listar_tareas()
        # ? Si el comando es 'crear', llamo a la función crear_tarea()
        elif comando == "crear":
            print(utils.crear_tarea())
        # ? Si el comando es 'eliminar', llamo a la función eliminar_tarea()
        elif comando == "eliminar":
            print(utils.eliminar_tarea())
        # ? Si el comando no es válido, imprimo un mensaje de error
        else:
            print("Comando no válido.")
    # ? Si no se proporcionó un comando, imprimo un mensaje de ayuda
    else:
        print("Por favor, proporciona un comando: 'tareas', 'crear' o 'eliminar'")