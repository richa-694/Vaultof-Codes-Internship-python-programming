import csv


class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

def save_tasks(tasks):
    with open('tasks.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Description", "Category", "Completed"])
        for task in tasks:
            writer.writerow([task.title, task.description, task.category, task.completed])

def load_tasks():
    try:
        with open('tasks.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row
            tasks = []
            for row in reader:
                task = Task(row[0], row[1], row[2])
                task.completed = row[3] == 'True'
                tasks.append(task)
            return tasks
    except FileNotFoundError:
        return []

def main():
    tasks = load_tasks()
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category: ")
            task = Task(title, description, category)
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!")
        elif choice == '2':
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{i}. {task.title} - {task.description} - {task.category} - {status}")
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: ")) - 1
            if task_id >= 0 and task_id < len(tasks):
                tasks[task_id].mark_completed()
                save_tasks(tasks)
                print("Task marked as completed successfully!")
            else:
                print("Invalid task ID.")
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: ")) - 1
            if task_id >= 0 and task_id < len(tasks):
                del tasks[task_id]
                save_tasks(tasks)
                print("Task deleted successfully!")
            else:
                print("Invalid task ID.")
        elif choice == '5':
            save_tasks(tasks)
            break

if __name__ == "__main__":
    main()