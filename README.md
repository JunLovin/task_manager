# Task Manager 📝

¡Bienvenido a Task Manager!  
Una sencilla aplicación de consola en Python para gestionar tus tareas de manera eficiente usando un archivo JSON.

## ¿Cómo funciona?

Este programa te permite:
- Listar todas tus tareas
- Crear nuevas tareas
- Eliminar tareas existentes

Las tareas se almacenan en el archivo `tareas.json`.

---

## Comandos disponibles

Ejecuta el programa desde la terminal usando:

```bash
python main.py <comando>
```

Donde `<comando>` puede ser:

- **tareas**
Muestra el listado de todas las tareas guardadas.
```bash
python main.py tareas
```
- **crear**
Permite crear una nueva tarea. El programa te pedirá el nombre y la descripción por consola.
```bash
python main.py crear
```
- **eliminar**
Eliminar una tarea existente. El programa te pedirá el ID de la tarea a eliminar.
```bash
python main.py eliminar
```

---

## Estructura de las tareas

Cada tarea tiene la siguiente estructura en el archivo `tareas.json`:

```json
{
    "id": 1,
    "titulo": "Tarea de ejemplo",
    "descripcion": "Descripción de la tarea",
    "completada": false
}
```

---

## Requisitos

- Python 3.x

---

## Notas:

- Si ejecutas el programa sin argumentos, te mostrará un mensaje de ayuda.
- Si introduces un comando no válido, te avisará por consola.


---
Creado con ❤️ por [Said Ruiz](https://said-beta.vercel.app)