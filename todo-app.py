import tkinter as tk
import json
from tkinter import messagebox

# Load tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task():
    task = entry_task.get()
    category = entry_category.get()
    if task and category:
        tasks.append({"task": task, "category": category})
        listbox_tasks.insert(tk.END, f"{task} ({category})")
        save_tasks()
        entry_task.delete(0, tk.END)
        entry_category.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Both fields are required!")

# Delete a task
def delete_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        listbox_tasks.delete(selected_task)
        del tasks[selected_task[0]]
        save_tasks()

# Initialize the main window
root = tk.Tk()
root.title("Advanced To-Do List")

# Entry widgets for task and category
entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=5)

entry_category = tk.Entry(root, width=30)
entry_category.pack(pady=5)

# Buttons to add and delete tasks
btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete.pack(pady=5)

# Listbox to display tasks
listbox_tasks = tk.Listbox(root, width=40, height=10)
listbox_tasks.pack(pady=10)

# Load existing tasks
tasks = load_tasks()
for task in tasks:
    listbox_tasks.insert(tk.END, f"{task['task']} ({task['category']})")

root.mainloop()
