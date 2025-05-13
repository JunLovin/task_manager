const tareas_json = require('./tareas.json')
const { listarTareas, agregarTarea, eliminarTareaPorId } = require('./utils.js')

if (process.argv[2] === "tareas") {
    listarTareas()
} else if (process.argv[2] === "crear") {
    agregarTarea(process.argv[3], process.argv[4])
} else if (process.argv[2] === "eliminar") {
    eliminarTareaPorId(process.argv[3])
} else {
    console.log("Comando no reconocido, por favor, ingresa un argumento valido: tareas, crear \"(nombre)\" \"(descripcion)\", eliminar (id)")
}