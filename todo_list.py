# todo_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "✅ Completed" if task["completed"] else "❌ Not Completed"
                print(f"{i}. {task['task']} - {status}")

    def mark_completed(self, task_no):
        if 0 < task_no <= len(self.tasks):
            self.tasks[task_no - 1]["completed"] = True
            print(f"Task {task_no} marked as completed!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_no):
        if 0 < task_no <= len(self.tasks):
            removed = self.tasks.pop(task_no - 1)
            print(f"Task '{removed['task']}' deleted successfully!")
        else:
            print("Invalid task number!")

    def update_task(self, task_no, new_task):
        if 0 < task_no <= len(self.tasks):
            self.tasks[task_no - 1]["task"] = new_task
            print(f"Task {task_no} updated successfully!")
        else:
            print("Invalid task number!")


def main():
    todo = ToDoList()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_no = int(input("Enter task number to mark as completed: "))
            todo.mark_completed(task_no)
        elif choice == "4":
            task_no = int(input("Enter task number to update: "))
            new_task = input("Enter new task: ")
            todo.update_task(task_no, new_task)
        elif choice == "5":
            task_no = int(input("Enter task number to delete: "))
            todo.delete_task(task_no)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
