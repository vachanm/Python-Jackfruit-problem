import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tasks = []

def refresh_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "[✔]" if task["done"] else "[ ]"
        due_str = task["due_date"].strftime("%d/%m/%Y")
        display_text = f"{status} {task['title']} — Due: {due_str}"
        task_listbox.insert(tk.END, display_text)

def add_task():
    title = title_entry.get().strip()
    due_str = due_entry.get().strip()

    if title == "" or due_str == "":
        messagebox.showwarning("Error", "Enter both task and due date.")
        return

    try:
        due_date = datetime.strptime(due_str, "%d/%m/%Y").date()
    except ValueError:
        messagebox.showerror("Invalid Date", "Use DD/MM/YYYY format.")
        return

    tasks.append({"title": title, "due_date": due_date, "done": False})
    refresh_listbox()

    title_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)

def mark_done():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Error", "Select a task first.")
        return
    tasks[selected[0]]["done"] = True
    refresh_listbox()

def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Error", "Select a task first.")
        return
    tasks.pop(selected[0])
    refresh_listbox()


# ---------------- UI SETUP ---------------- #

root = tk.Tk()
root.title("To-Do List App")
root.attributes("-fullscreen", True)

BIG_FONT = ("Arial", 22)
MED_FONT = ("Arial", 18)
BUTTON_FONT = ("Arial", 20)

# Title
heading = tk.Label(root, text="My To-Do List", font=("Arial", 36, "bold"))
heading.pack(pady=20)

# Task label + input
title_label = tk.Label(root, text="Task Name:", font=BIG_FONT)
title_label.pack(pady=5)

title_entry = tk.Entry(root, font=MED_FONT, width=40)
title_entry.pack(pady=5)

# Due date label + input
due_label = tk.Label(root, text="Due Date (DD/MM/YYYY):", font=BIG_FONT)
due_label.pack(pady=5)

due_entry = tk.Entry(root, font=MED_FONT, width=40)
due_entry.pack(pady=5)

# Buttons Frame (to keep them neatly aligned)
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

add_button = tk.Button(button_frame, text="Add Task", font=BUTTON_FONT, width=12, command=add_task)
add_button.grid(row=0, column=0, padx=10)

done_button = tk.Button(button_frame, text="Mark Done", font=BUTTON_FONT, width=12, command=mark_done)
done_button.grid(row=0, column=1, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", font=BUTTON_FONT, width=12, command=delete_task)
delete_button.grid(row=0, column=2, padx=10)

# Task Listbox
task_listbox = tk.Listbox(root, font=MED_FONT, width=60, height=12)
task_listbox.pack(pady=20)

# Exit button (bottom of screen)
exit_button = tk.Button(root, text="Exit App", font=BUTTON_FONT, command=root.destroy, width=10)
exit_button.pack(pady=20)
root.mainloop()
