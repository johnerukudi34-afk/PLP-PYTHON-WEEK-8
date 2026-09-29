print("Welcome to My Python Toolkit!")

while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
    # Simple Calculator: performs basic calculations with two numbers.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"Sum: {num1 + num2}")
    print(f"Difference: {num1 - num2}")
    print(f"Product: {num1 * num2}")

    if num2 != 0:
        print(f"Division: {num1 / num2}")
    else:
        print("Division: Cannot divide by zero.")

elif choice == "2":
    # To-Do List: lets the user add, view, and remove tasks.
    tasks = []

    while True:
        print("\nTo-Do List")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        task_choice = input("Enter your choice: ")

        if task_choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' was added.")

        elif task_choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif task_choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                task_number = int(input("Enter the task number to remove: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' was removed.")
                else:
                    print("That task number is not valid.")

        elif task_choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print(f"Sorry, '{task_choice}' is not a valid option.")
elif choice == "3":
    # Number Checker: checks whether a number is positive, negative, zero, even, or odd.
    number = int(input("Enter a number: "))

    if number > 0:
        print(f"{number} is positive.")
    elif number < 0:
        print(f"{number} is negative.")
    else:
        print(f"{number} is zero.")

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

    elif choice == "4":
        print("Thank you for using My Python Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")