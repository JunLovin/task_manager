const path = require('path')
const fs = require('fs')
const tareas_json = require('./tareas.json')

const listarTareas = () => {
    console.log("Listado de tareas:")
    console.log("-------------------------------\n")
    for (let i = 0; i < tareas_json.tareas.length; i++) {
        console.log(`ID: ${tareas_json.tareas[i].id}\nTarea: ${tareas_json.tareas[i].titulo}\nDescripcion: ${tareas_json.tareas[i].descripcion}\nCompletada: ${tareas_json.tareas[i].completada ? "Si" : "No"}\n\n`)
    }
    console.log("\n-------------------------------")
}

// listarTareas()

const agregarTarea = (nombre, descripcion) => {
    if (!nombre) {
        return "Debe ingresar un nombre para la tarea"
    }
    const nueva_tarea = {
        "id": tareas_json.tareas.length + 1,
        "titulo": nombre,
        "descripcion": descripcion,
        "completado": false
    }
    tareas_json.tareas.push(nueva_tarea)
    console.log(tareas_json)
    fs.writeFileSync(path.join(__dirname, './tareas.json'), JSON.stringify(tareas_json), 'utf-8')
    return "Tarea agregada correctamente"
}

// console.log(agregarTarea("Tarea dos", "Esta es la descripcion de la tarea dos"))

const eliminarTareaPorId = id => {
    if (!id) {
        return "Debe ingresar un id para eliminar la tarea"
    }
    for (let i = 0; i < tareas_json.tareas.length; i++) {
        if (tareas_json.tareas[i].id === Number(id)) {
            tareas_json.tareas = tareas_json.tareas.filter(tarea => tarea.id !== Number(id))
            break
        }
    }
    fs.writeFileSync(path.join(__dirname, './tareas.json'), JSON.stringify(tareas_json), 'utf-8')
    console.log(tareas_json.tareas)
}

// eliminarTareaPorId(2)

module.exports = { listarTareas, agregarTarea, eliminarTareaPorId }