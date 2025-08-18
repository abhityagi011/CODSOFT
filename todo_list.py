todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as completed")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "✔️" if task["done"] else "❌"
            print(f"{index}. [{status}] {task['task']}")

def add_task():
    task_text = input("Enter the task: ")
    todo_list.append({"task": task_text, "done": False})
    print("Task added!")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        removed = todo_list.pop(index)
        print(f"Removed: {removed['task']}")
    except (IndexError, ValueError):
        print("Invalid task number.")

def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        todo_list[index]["done"] = True
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_completed()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
