#A python project of "To Do List Application" by using object,function and module are given below.

class TodoList:
    def __init__(self):
        #Fristly we have to initialize an empty to-do list.
        self.tasks = []

    def display_tasks(self):
          # Display the current list of tasks.
        print("\nYOUR TO-DO LIST:")
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}: {task}")

    def add_task(self):
          #Add new tasks to the to-do list.
        input_str = input("Enter tasks to add in To-Do List : ")
        input_list = input_str.split()
        added = False

        for task in input_list:
            if task.strip():  # Check for non-empty strings
                self.tasks.append(task.strip())
                added = True

        if added:
            print("Tasks added successfully.")
        else:
            print("No valid tasks provided. To-Do List remains unchanged.")

    def delete_task(self):
          #Delete a task from the to-do list.
        self.display_tasks()
        if not self.tasks:  # If the todo list is empty
            return

        try:
            index = int(input("Enter the task number to delete: "))
            if 1 <= index <= len(self.tasks):
                deleted_task = self.tasks.pop(index - 1)
                print(f"Task '{deleted_task}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def mark_completed(self):
          #Mark a task as completed.
        self.display_tasks()
        if not self.tasks:
            return

        try:
            index = int(input("Enter the task number to mark as completed: "))
            if 1 <= index <= len(self.tasks):
                self.tasks[index - 1] += " (completed)"
                print(f"Task '{self.tasks[index - 1]}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def load_tasks(self):
         #Load previously saved tasks from a file.
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    self.tasks.append(line.strip())
        except FileNotFoundError:
            print("No existing to-do list found. Starting with an empty list.")

    def save_tasks(self):
          #Save current tasks to a file.
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        print("Your recent tasks successfully saved.")

def main():
      #Main function to run the to-do list application.
    todo_list = TodoList()
    todo_list.load_tasks()

    while True:
        print("\nTO-DO LIST MENU:")
        print("1. Display Tasks")
        print("2. Add A Task")
        print("3. Delete A Task")
        print("4. Mark A Task As Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            todo_list.add_task()
        elif choice == '3':
            todo_list.delete_task()
        elif choice == '4':
            todo_list.mark_completed()
        elif choice == '5':
            todo_list.save_tasks()
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

