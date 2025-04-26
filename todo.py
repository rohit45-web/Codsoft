from tkinter import *
from tkinter import messagebox


class TodoApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("To-Do List Application")
        self.root.geometry("400x500+100+100")
        self.root.config(bg="moccasin")

        self.title_label = Label(self.root, text="To-Do List", font=("Algerian", 20, "bold"), bg="moccasin", fg="navy")
        self.title_label.place(x=100, y=10, width=200, height=40)

        self.task_input = Entry(self.root, font=("Arial", 14), bg="lightgrey")
        self.task_input.place(x=20, y=60, width=260, height=30)

        self.add_task_button = Button(self.root, text="Add Task", font=("Centaur", 16, 'bold'), bg="darkgreen", fg="white",
                                      command=self.add_task)
        self.add_task_button.place(x=290, y=60, width=90, height=30)

        self.task_listbox = Listbox(self.root, font=("Arial", 12), bg="lightgrey", fg="black")
        self.task_listbox.place(x=20, y=110, width=360, height=280)

        self.delete_task_button = Button(self.root, text="Delete Task", font=("Centaur", 16, 'bold'), bg="olive", fg="white",
                                         command=self.delete_task)
        self.delete_task_button.place(x=40, y=410, width=120, height=40)

        self.clear_all_button = Button(self.root, text="Clear All", font=("Centaur", 16, 'bold'), bg="olive", fg="white",
                                       command=self.clear_all_tasks)
        self.clear_all_button.place(x=240, y=410, width=120, height=40)

    def add_task(self):
        task = self.task_input.get().strip()
        if task:
            self.task_listbox.insert(END, task)
            self.task_input.delete(0, END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def clear_all_tasks(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.task_listbox.delete(0, END)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = TodoApp()
    app.run()