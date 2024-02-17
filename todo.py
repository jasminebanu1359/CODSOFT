import tkinter as tk
from tkinter import messagebox

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=2, column=0, padx=10, pady=10)

        self.mark_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.mark_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_listbox.insert(tk.END, f"{task} - Not Completed")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks available.")
        else:
            task_list = "\n".join([f"{index + 1}. {task['task']} - {'Completed' if task['completed'] else 'Not Completed'}" for index, task in enumerate(self.tasks)])
            messagebox.showinfo("Tasks", task_list)

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index]["completed"] = True
            self.task_listbox.delete(task_index)
            messagebox.showinfo("Info", "Task marked as completed.")
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()
