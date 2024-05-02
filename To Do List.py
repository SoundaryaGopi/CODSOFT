tasks = []

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == '2':
        if tasks:
            print("Your To-Do List:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Your To-Do List is empty.")
    elif choice == '3':
        print("Thank you for using the To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
