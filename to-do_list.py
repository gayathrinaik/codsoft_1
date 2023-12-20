import tkinter as tk
from tkinter import ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Task Entry
        self.task_entry = ttk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task Button
        add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # Task List
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Mark as Completed Button
        complete_button = ttk.Button(root, text="Mark as Completed", command=self.mark_as_completed)
        complete_button.grid(row=2, column=0, padx=10, pady=10)

        # Delete Task Button
        delete_button = ttk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=2, column=1, padx=10, pady=10)

        # Run the main loop
        self.root.mainloop()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.task_listbox.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)  # Clear the entry field

    def mark_as_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.task_listbox.itemconfig(task_index, {'bg': 'light green'})
            # You can add further logic if needed when a task is marked as completed

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
