import json

tasks = []

def add_task(name, priority, due_date):
    task = {
        'name': name,
        'priority': priority,
        'due_date': due_date,
        'status': 'Pending'
    }
    tasks.append(task)
    print("Task added successfully!")
    save_tasks()

def remove_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task removed successfully!")
        save_tasks()
    else:
        print("Invalid index!")

def mark_task_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]['status'] = 'Completed'
        print("Task marked as completed!")
        save_tasks()
    else:
        print("Invalid index!")

def display_tasks():
    if not tasks:
        print("Task list is empty.")
    else:
        print("\nTask List:")
        for index, task in enumerate(tasks):
            print(f"{index}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {task['status']}")

def save_tasks():
    with open("tasks.txt", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    try:
        with open("tasks.txt", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def main():
    load_tasks()
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            priority = input("Enter priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(name, priority, due_date)
        elif choice == '2':
            index = int(input("Enter the index of the task to remove: "))
            remove_task(index)
        elif choice == '3':
            index = int(input("Enter the index of the task to mark as completed: "))
            mark_task_completed(index)
        elif choice == '4':
            display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
