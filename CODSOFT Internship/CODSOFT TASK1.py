#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json

# Function to load tasks from a JSON file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to a JSON file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to display the list of tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. Name: {task['name']}")
            print(f"   Description: {task['description']}")
            print(f"   Due Date: {task['due_date']}")
            print(f"   Status: {'Completed' if task['completed'] else 'Not Completed'}")
            print()

# Function to create a new task
def create_task(tasks):
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    task = {
        'name': name,
        'description': description,
        'due_date': due_date,
        'completed': False
    }

    tasks.append(task)
    print("Task created successfully.")

# Function to mark a task as completed
def mark_task_completed(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main function
def main():
    tasks = load_tasks('tasks.json')

    while True:
        print("\nTo-Do List Application")
        print("1. Create a new task")
        print("2. Mark a task as completed")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            create_task(tasks)
        elif choice == '2':
            mark_task_completed(tasks)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            save_tasks('tasks.json', tasks)
            print("Exiting the application. Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




