import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    task = simpledialog.askstring("Enter Task", "Enter your task:")
    if task:
        listbox.insert(tk.END, task)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all_tasks():
    response = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
    if response:
        listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Colorful To-Do List")

# Set colorful background
root.configure(bg="#FFD700")  # You can replace "#FFD700" with any other color code

# Create a frame to hold the to-do list
frame = tk.Frame(root, bg="#FFD700", padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Create a listbox to display tasks
listbox = tk.Listbox(frame, selectbackground="#a6a6a6", selectmode=tk.SINGLE, font=("Helvetica", 12))
listbox.pack(fill=tk.BOTH, expand=True)

# Create buttons to add, delete, and clear tasks
add_button = tk.Button(frame, text="Add Task", command=add_task, bg="#4caf50", fg="#ffffff", font=("Helvetica", 12))
add_button.pack(side=tk.LEFT, padx=5, pady=5)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task, bg="#f44336", fg="#ffffff", font=("Helvetica", 12))
delete_button.pack(side=tk.LEFT, padx=5, pady=5)

clear_button = tk.Button(frame, text="Clear All", command=clear_all_tasks, bg="#2196f3", fg="#ffffff", font=("Helvetica", 12))
clear_button.pack(side=tk.LEFT, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
