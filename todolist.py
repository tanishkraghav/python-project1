# Define an empty list to store the tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Added '{task}' to your to-do list.")

# Function to remove a task from the list
def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        print(f"Removed '{task}' from your to-do list.")
    else:
        print("Invalid task number. Please try again.")

# Main loop to interact with the to-do list
while True:
    print("\nWhat would you like to do?")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        new_task = input("Enter the task you want to add: ")
        add_task(new_task)
    elif choice == '3':
        display_tasks()
        task_to_remove = int(input("Enter the number of the task to remove: "))
        remove_task(task_to_remove)
    elif choice == '4':
        print("Thank you. Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
