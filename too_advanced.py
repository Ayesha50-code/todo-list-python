import json

FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Show menu
def show_menu():
    print("\n--- Advanced To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == "1":  # Add Task
        name = input("Enter task name: ")
        due = input("Enter due date (YYYY-MM-DD): ")
        task = {"name": name, "due": due, "done": False}
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!")

    elif choice == "2":  # View Tasks
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                status = "✅ Done" if t["done"] else "⏳ Pending"
                print(f"{i}. {t['name']} (Due: {t['due']}) - {status}")

    elif choice == "3":  # Mark Complete
        num = int(input("Enter task number to mark complete: "))
        if 0 < num <= len(tasks):
            tasks[num-1]["done"] = True
            save_tasks(tasks)
            print("🎉 Task marked as completed!")
        else:
            print("⚠️ Invalid task number!")

    elif choice == "4":  # Delete Task
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num-1)
            save_tasks(tasks)
            print(f"❌ Task '{removed['name']}' deleted!")
        else:
            print("⚠️ Invalid task number!")

    elif choice == "5":  # Exit
        print("Goodbye 👋")
        break

    else:
        print("⚠️ Invalid choice! Please enter 1-5.")
