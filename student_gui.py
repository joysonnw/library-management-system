import tkinter as tk
from tkinter import messagebox, ttk
import backend

class StudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student - Library Management")
        self.root.geometry("600x400")
        self.student_id = None
        self.show_login()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear()
        tk.Label(self.root, text="Student Login", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.root, text="Email").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()
        tk.Label(self.root, text="Password").pack()
        self.pass_entry = tk.Entry(self.root, show="*")
        self.pass_entry.pack()
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Register", command=self.show_register).pack()

    def show_register(self):
        self.clear()
        tk.Label(self.root, text="Student Registration", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.root, text="Name").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        tk.Label(self.root, text="Email").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()
        tk.Label(self.root, text="Password").pack()
        self.pass_entry = tk.Entry(self.root, show="*")
        self.pass_entry.pack()
        tk.Button(self.root, text="Register", command=self.register).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.show_login).pack()

    def login(self):
        email = self.email_entry.get()
        password = self.pass_entry.get()
        success, student_id = backend.login_student(email, password)
        if success:
            self.student_id = student_id
            messagebox.showinfo("Success", "Logged in successfully!")
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.pass_entry.get()
        success, msg = backend.register_student(name, email, password)
        if success:
            messagebox.showinfo("Success", msg)
            self.show_login()
        else:
            messagebox.showerror("Error", msg)

    def show_dashboard(self):
        self.clear()
        tk.Label(self.root, text="Student Dashboard", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="View All Books", command=self.view_books).pack(pady=5)
        tk.Button(self.root, text="View My Issued Books", command=self.view_issued_books).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=10)

    def view_books(self):
        self.clear()
        tk.Label(self.root, text="Available Books", font=("Arial", 16)).pack(pady=10)

        cols = ("ID", "Title", "Author", "Quantity")
        self.tree = ttk.Treeview(self.root, columns=cols, show="headings")
        for col in cols:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True)

        books = backend.get_all_books()
        for book in books:
            self.tree.insert("", "end", values=book)

        tk.Button(self.root, text="Issue Selected Book", command=self.issue_selected_book).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_dashboard).pack()

    def issue_selected_book(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a book.")
            return
        book_id = self.tree.item(selected[0])["values"][0]
        success, msg = backend.issue_book(self.student_id, book_id)
        if success:
            messagebox.showinfo("Success", msg)
            self.view_books()
        else:
            messagebox.showerror("Error", msg)

    def view_issued_books(self):
        self.clear()
        tk.Label(self.root, text="My Issued Books", font=("Arial", 16)).pack(pady=10)

        cols = ("Issue ID", "Title", "Author", "Issue Date", "Due Date", "Return Date", "Fine")
        self.tree = ttk.Treeview(self.root, columns=cols, show="headings")
        for col in cols:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True)

        issued_books = backend.get_student_issued_books(self.student_id)
        for book in issued_books:
            # Return date and fine might be None, convert to string for display
            display_row = list(book)
            display_row[5] = display_row[5] if display_row[5] else "Not returned"
            display_row[6] = f"₹{display_row[6]}" if display_row[6] else "₹0"
            self.tree.insert("", "end", values=display_row)

        tk.Button(self.root, text="Return Selected Book", command=self.return_selected_book).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_dashboard).pack()

    def return_selected_book(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a book to return.")
            return
        issue_id = self.tree.item(selected[0])["values"][0]
        success, msg = backend.return_book(issue_id)
        if success:
            messagebox.showinfo("Success", msg)
            self.view_issued_books()
        else:
            messagebox.showerror("Error", msg)

    def logout(self):
        self.student_id = None
        self.show_login()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentGUI(root)
    root.mainloop()
