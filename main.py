import tkinter as tk
from tkinter import messagebox
import student_gui
import librarian_gui

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x200")
        self.show_main_menu()

    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Library Management System", font=("Arial", 20)).pack(pady=20)

        tk.Button(self.root, text="Student", width=20, command=self.open_student).pack(pady=10)
        tk.Button(self.root, text="Librarian", width=20, command=self.open_librarian).pack(pady=10)

    def open_student(self):
        self.root.destroy()
        root = tk.Tk()
        student_gui.StudentGUI(root)
        root.mainloop()

    def open_librarian(self):
        self.root.destroy()
        root = tk.Tk()
        librarian_gui.LibrarianGUI(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
