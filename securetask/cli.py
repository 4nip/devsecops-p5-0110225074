"""Simple interactive command-line interface."""
from securetask.service import TaskService


def run() -> None:
    """Run the SecureTask interactive menu."""
    service = TaskService()
    while True:
        print("\n=== SecureTask ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ")
            try:
                task = service.add_task(title)
                print(f"Added: {task.title}")
            except ValueError as error:
                print(f"Invalid input: {error}")
        elif choice == "2":
            tasks = service.list_tasks()
            if not tasks:
                print("No tasks yet.")
            for number, task in enumerate(tasks, start=1):
                status = "Done" if task.completed else "Pending"
                print(f"{number}. [{status}] {task.title}")
        elif choice == "3":
            tasks = service.list_tasks()
            if not tasks:
                print("There are no tasks to complete.")
                continue
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task.title}")
            try:
                number = int(input("Task number to complete: ").strip())
                task = service.complete_task(number - 1)
                print(f"Completed: {task.title}")
            except (ValueError, IndexError) as error:
                print(f"Could not complete task: {error}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Choose 1, 2, 3, or 4.")
