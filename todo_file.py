# Step 3: To-Do List with File Saving

tasks = []

# File ka naam
FILENAME = "tasks.txt"

# File se tasks load karna
def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # agar file nahi hai to ignore

# Tasks ko file me save karna
def save_tasks():
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

# Start me load kar lo
load_tasks()

while True:
    show_menu()
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks()
        print("✅ Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num-1)
            save_tasks()
            print(f"❌ Task '{removed}' deleted!")
        else:
            print("⚠️ Invalid task number!")

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("⚠️ Invalid choice! Please enter 1-4.")
