from task_manager.tasks import add_task, list_tasks, delete_task

def main():
    tasks = []
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            task = input("Describe la tarea: ")
            add_task(tasks, task)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            task_number = int(input("Número de tarea a eliminar: "))
            delete_task(tasks, task_number)
        elif choice == "4":
            print("Saliendo del gestor...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
