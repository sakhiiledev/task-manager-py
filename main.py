from db import TaskDatabase
from dotenv import load_dotenv 
import os

load_dotenv('.env')

# menu options

def menu():
    db_params = {
    'dbname': os.getenv('DB_NAME'),
    'dbuser': os.getenv('DB_USER'),
    'dbpassword': os.getenv('DB_PASSWORD'),
    }


    db = TaskDatabase(**db_params)
    print("Task Manager")
    print("1. Create Task")
    print("2. Read Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    while True:
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            db.create_task(title, description)
            print("Task created")

        elif choice == '2':
            tasks = db.read_tasks()
            print("\nTasks:")
            for task in tasks:
                print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}")

        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_title = input("Enter new task title: ")
            new_description = input("Enter new task description: ")
            db.update_task(task_id, new_title, new_description)
            print("Task updated successfully!")

        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            db.delete_task(task_id)
            print("Task deleted successfully!")

        elif choice == '5':
            db.close()
            print("Goodbye!")
            break

if __name__ == "__main__":
    menu()
