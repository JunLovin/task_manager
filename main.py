import json

# - Función para listar las tareas
def listar_tareas():
    # ? Creo una conexión con el archivo tareas.json
    with open('tareas.json') as tareas_json:
        # ? Guardo la información del archivo en una variable
        tareas = json.load(tareas_json)
        #? Imprimo las tareas con su ID, nombre y descripción
        for tarea in tareas['tareas']:
            print(f"ID: {tarea['id']}")
            print(f"Nombre: {tarea['nombre']}")
            print(f"Descripción: {tarea['descripcion']}")

# - Función para agregar una tarea
def crear_tarea():
    # ? Pido el nombre al usuario mediante un input
    nombre = input("Ingresa el nombre de la tarea:\n")
    # ? Si el nombre dado no existe o es vacío, retorno un mensaje de error
    if not nombre:
        return "Por favor, ingresa el nombre de la tarea."
    # ? Pido la descripción al usuario mediante un input
    descripcion = input("Ingresa la descripción de la tarea:\n")
    # ? Creo una conexión con el archivo tareas.json
    with open('tareas.json') as tareas_json:
        # ? Guardo la información del archivo en una variable
        tareas = json.load(tareas_json)
        # ? Creo un objeto con la nueva tarea
        tarea = {
            "id": len(tareas['tareas']) + 1,
            "nombre": nombre,
            "descripcion": descripcion,
            "completada": False
            }
        # ? Agrego la tarea al array de tareas
        tareas['tareas'].append(tarea)
        # print(tareas)
        # ? Creo una conexión con el archivo tareas.json
        with open('tareas.json', 'w') as tareas_json:
            # ? Sobreescribo el archivo el array de tareas con la nueva tarea agregada
            json.dump(tareas, tareas_json, indent=4)
        return "Tarea agregada exitosamente."

# - Función para eliminar una tarea por su ID
def eliminar_tarea():
    # ? Pido el ID al usuario mediante un input
    id = int(input("Ingresa el ID de la tarea a eliminar:\n"))
    # ? Si el ID dado no existe o es 0, retorno un mensaje de error
    if not id:
        return "Por favor, ingresa el ID de la tarea a eliminar."
    # ? Creo una conexión con el archivo tareas.json
    with open('tareas.json') as tareas_json:
        # ? Guardo la información del archivo en una variable
        tareas = json.load(tareas_json)
        # ? Recorro el array de tareas
        for tarea in tareas['tareas']:
            # ? Si el ID de la tarea es igual al ID dado, elimino la tarea y salgo del bucle for
            if tarea['id'] == id:
                tareas['tareas'].remove(tarea)
                break
        # ? Creo una conexión con el archivo tareas.json
        with open('tareas.json', 'w') as tareas_json:
            # ? Sobreescribo el archivo el array de tareas con la tarea eliminada
            json.dump(tareas, tareas_json, indent=4)
        return "Tarea eliminada exitosamente."