import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

tasks = []

# --- Functions ---
def update_task_list():
    listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        listbox.insert(tk.END, f"{'[✔]' if task['done'] else '[ ]'} {task['name']}")

def add_task():
    task_text = entry.get()
    if task_text.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    tasks.append({'name': task_text, 'done': False})
    entry.delete(0, tk.END)
    update_task_list()

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def mark_done():
    try:
        selected_index = listbox.curselection()[0]
        tasks[selected_index]['done'] = not tasks[selected_index]['done']
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark done!")

# --- GUI Layout ---
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(pady=5)

listbox = tk.Listbox(root, width=45, height=10)
listbox.pack(pady=10)

btn_done = tk.Button(root, text="Mark as Done", command=mark_done)
btn_done.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete.pack(pady=5)

# Start with empty list
update_task_list()

# Run the app
root.mainloop()
