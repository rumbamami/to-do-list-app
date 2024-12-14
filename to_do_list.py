# To-Do List Application
todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter the task you want to add: ")
    todo_list.append(task)
    print(f'"{task}" has been added to your to-do list.')

def remove_task():
    if not todo_list:
        print("\nYour to-do list is empty. Nothing to remove.")
    else:
        view_tasks()
        try:
            task_number = int(input("\nEnter the number of the task to remove: "))
            removed_task = todo_list.pop(task_number - 1)
            print(f'"{removed_task}" has been removed from your to-do list.')
        except (ValueError, IndexError):
            print("Invalid task number. Please try again.")

# Main program loop
while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
