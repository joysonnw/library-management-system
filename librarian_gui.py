import tkinter as tk
from tkinter import messagebox, ttk
import backend

class LibrarianGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Librarian - Library Management")
        self.root.geometry("700x500")
        self.show_login()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear()
        tk.Label(self.root, text="Librarian Login", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.root, text="Email").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()
        tk.Label(self.root, text="Password").pack()
        self.pass_entry = tk.Entry(self.root, show="*")
        self.pass_entry.pack()
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.pass_entry.get()
        success = backend.login_librarian(email, password)
        if success:
            messagebox.showinfo("Success", "Logged in successfully!")
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def show_dashboard(self):
        self.clear()
        tk.Label(self.root, text="Librarian Dashboard", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="Add New Book", command=self.show_add_book).pack(pady=5)
        tk.Button(self.root, text="View All Books", command=self.view_books).pack(pady=5)
        tk.Button(self.root, text="View All Students", command=self.view_students).pack(pady=5)
        tk.Button(self.root, text="View Issued Books", command=self.view_issued_books).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.show_login).pack(pady=10)

    def show_add_book(self):
        self.clear()
        tk.Label(self.root, text="Add New Book", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Title").pack()
        self.title_entry = tk.Entry(self.root)
        self.title_entry.pack()
        tk.Label(self.root, text="Author").pack()
        self.author_entry = tk.Entry(self.root)
        self.author_entry.pack()
        tk.Label(self.root, text="Quantity").pack()
        self.qty_entry = tk.Entry(self.root)
        self.qty_entry.pack()

        tk.Button(self.root, text="Add Book", command=self.add_book).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_dashboard).pack()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        try:
            qty = int(self.qty_entry.get())
        except:
            messagebox.showerror("Error", "Quantity must be a number.")
            return
        if not title or not author:
            messagebox.showerror("Error", "Please fill all fields.")
            return
        success, msg = backend.add_book(title, author, qty)
        if success:
            messagebox.showinfo("Success", msg)
            self.show_dashboard()
        else:
            messagebox.showerror("Error", msg)

    def view_books(self):
        self.clear()
        tk.Label(self.root, text="All Books", font=("Arial", 16)).pack(pady=10)
        cols = ("ID", "Title", "Author", "Quantity")
        self.tree = ttk.Treeview(self.root, columns=cols, show="headings")
        for col in cols:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True)

        books = backend.get_all_books()
        for book in books:
            self.tree.insert("", "end", values=book)

        tk.Button(self.root, text="Back", command=self.show_dashboard).pack(pady=10)

    def view_students(self):
        self.clear()
        tk.Label(self.root, text="All Students", font=("Arial", 16)).pack(pady=10)
        cols = ("Student ID", "Name", "Email")
        self.tree = ttk.Treeview(self.root, columns=cols, show="headings")
        for col in cols:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True)

        students = backend.get_all_students()
        for student in students:
            self.tree.insert("", "end", values=student)

        tk.Button(self.root, text="Back", command=self.show_dashboard).pack(pady=10)

    def view_issued_books(self):
        self.clear()
        tk.Label(self.root, text="Issued Books", font=("Arial", 16)).pack(pady=10)
        cols = ("Issue ID", "Student Name", "Book Title", "Issue Date", "Due Date", "Return Date", "Fine")
        self.tree = ttk.Treeview(self.root, columns=cols, show="headings")
        for col in cols:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True)

        issued_books = backend.get_all_issued_books()
        for ib in issued_books:
            display_row = list(ib)
            display_row[5] = display_row[5] if display_row[5] else "Not returned"
            display_row[6] = f"₹{display_row[6]}" if display_row[6] else "₹0"
            self.tree.insert("", "end", values=display_row)

        tk.Button(self.root, text="Back", command=self.show_dashboard).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = LibrarianGUI(root)
    root.mainloop()
