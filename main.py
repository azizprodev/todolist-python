def display_menu():
    print("\nTodo List Menu:")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. Update a task")
    print("4. View tasks")
    print("5. Exit")

def add_task(todolist):
    task = input("Enter a new task: ")
    todolist.append(task)
    print(f"Task '{task}' added.")

def delete_task(todolist):
    view_tasks(todolist)
    try:
        task_index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_index < len(todolist):
            removed_task = todolist.pop(task_index)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def update_task(todolist):
    view_tasks(todolist)
    try:
        task_index = int(input("Enter the number of the task to update: ")) - 1
        if 0 <= task_index < len(todolist):
            new_task = input("Enter the new task: ")
            old_task = todolist[task_index]
            todolist[task_index] = new_task
            print(f"Task '{old_task}' updated to '{new_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(todolist):
    if not todolist:
        print("No tasks in the list.")
    else:
        print("\nTodo List:")
        for index, task in enumerate(todolist, start=1):
            print(f"{index}. {task}")

def main():
    todolist = []
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_task(todolist)
            elif choice == 2:
                delete_task(todolist)
            elif choice == 3:
                update_task(todolist)
            elif choice == 4:
                view_tasks(todolist)
            elif choice == 5:
                print("Exiting Todo List. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
