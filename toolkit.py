
# ==========================================
# MY PYTHON WEEK 8 TOOLKIT
# ==========================================


# TOOL 1: SIMPLE CALCULATOR
# This tool performs basic mathematical operations.

def calculator():

    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter the first number: "))

        operator = input("Choose an operation (+, -, *, /): ")

        num2 = float(input("Enter the second number: "))

        if operator == "+":
            answer = num1 + num2

        elif operator == "-":
            answer = num1 - num2

        elif operator == "*":
            answer = num1 * num2

        elif operator == "/":

            if num2 == 0:
                print("Sorry, you cannot divide by zero!")
                return

            answer = num1 / num2

        else:
            print("Invalid operation!")
            return

        print(f"The answer is: {answer}")

    except ValueError:
        print("Please enter valid numbers.")


# TOOL 2: TO-DO LIST
# This tool allows users to add, view and remove tasks.

def todo_list(tasks):

    while True:

        print("\n--- TO-DO LIST ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":

            if len(tasks) == 0:
                print("Your task list is empty.")

            else:
                print("\nYour tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "2":

            new_task = input("Enter a new task: ").strip()

            if new_task:
                tasks.append(new_task)
                print(f"Task '{new_task}' added successfully!")

            else:
                print("Task cannot be empty.")

        elif choice == "3":

            if len(tasks) == 0:
                print("There are no tasks to remove.")

            else:

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter task number to remove: "))

                    if 1 <= task_number <= len(tasks):

                        removed_task = tasks.pop(task_number - 1)

                        print(f"Task '{removed_task}' removed successfully!")

                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":

            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please try again.")


# TOOL 3: NUMBER GUESSING GAME
# This tool asks the user to guess a secret number.

def guessing_game():

    secret_number = 7

    print("\n--- NUMBER GUESSING GAME ---")
    print("I am thinking of a number between 1 and 10.")

    while True:

        try:
            guess = int(input("Enter your guess: "))

            if guess < secret_number:

                print("Too low! Try again.")

            elif guess > secret_number:

                print("Too high! Try again.")

            else:

                print(f"Congratulations! You guessed {secret_number}!")
                break

        except ValueError:
            print("Please enter a whole number.")


# MAIN PROGRAM
# This displays the menu and runs the selected tool.

def main():

    # This list stores the user's tasks.
    tasks = []

    print("\n================================")
    print("   WELCOME TO MY PYTHON TOOLKIT")
    print("================================")

    while True:

        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":

            calculator()

        elif choice == "2":

            todo_list(tasks)

        elif choice == "3":

            guessing_game()

        elif choice == "4":

            print("\nThank you for using my toolkit!")
            print("Goodbye. Have a great day!")
            break

        else:

            print(f"Sorry, '{choice}' is not a valid choice.")
            print("Please choose a number between 1 and 4.")


# Start the program.
if __name__ == "__main__":
    main()
