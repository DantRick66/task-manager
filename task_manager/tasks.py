"""
Módulo para gestionar tareas del proyecto.
"""


def add_task(tasks, task):
    """Añade una tarea a la lista."""
    tasks.append(task)
    print(f"Tarea '{task}' añadida con éxito.")

def list_tasks(tasks):
    """Lista todas las tareas."""
    if not tasks:
        print("No hay tareas.")
    else:
        print("\nLista de Tareas:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(tasks, task_number):
    """Elimina una tarea de la lista por su número."""
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Tarea '{removed}' eliminada.")
    else:
        print("Número de tarea inválido.")
