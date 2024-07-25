import os

FILE_NAME = 'todo.txt'

def main():
  tasks = load_tasks()
  while True:
    show_menu()
    choice = input("Choose an option: ").strip()
    if choice == '1':
      add_task(tasks)
    elif choice == '2':
      view_task(tasks)
    elif choice == '3':
      remove_task(tasks)
    elif choice == '4':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please select a valid option")

def load_tasks():
  if not os.path.exists(FILE_NAME):
    return []
  with open(FILE_NAME, 'r') as file:
    tasks = file.readlines()
  return [task.strip() for task in tasks if task.strip()]

def show_menu():
  print("\nTo-Do List")
  print("1. Add task")
  print("2. View tasks")
  print("3. Remove tasks")
  print("4. Exit")

def add_task(tasks):
  task = input("Enter the task: ").strip()
  if task:
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")
  else:
    print("Task cannot be empty")

def save_tasks(tasks):
  with open(FILE_NAME, 'w') as file:
    for task in tasks:
      file.write(task + '\n')

def view_task(tasks):
  if not tasks:
    print("No tasks to show")
  else: 
    print("\nTasks:")
    for idx, task in enumerate(tasks, start=1):
      print(f"{idx}. {task}")

def remove_task(tasks):
  view_tasks(tasks)
  try:
    task_index = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= task_index < len(tasks):
      removed_task = tasks.pop(task_index)
      save_tasks(tasks)
      print(f"Removed task: {remove_task}")
    else:
      print("Invalid task number")
  except ValueError:
    print("Invalid input. Please enter a number")

if __name__ == "__main__":
  main()