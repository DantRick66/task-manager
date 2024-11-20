def add_task(tasks, task):
    tasks.append(task)
    print(f"Tarea '{task}' añadida con éxito.")

def list_tasks(tasks):
    if not tasks:
        print("No hay tareas.")
    else:
        print("\nLista de Tareas:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")