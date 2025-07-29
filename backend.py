import mysql.connector
from datetime import datetime, timedelta

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="281273",
    database="library_management"
)
cursor = conn.cursor(buffered=True)

# -- STUDENT --

def register_student(name, email, password):
    cursor.execute("SELECT * FROM students WHERE email=%s", (email,))
    if cursor.fetchone():
        return False, "Email already registered."
    cursor.execute("INSERT INTO students (name, email, password) VALUES (%s,%s,%s)", (name, email, password))
    conn.commit()
    return True, "Student registered successfully."

def login_student(email, password):
    cursor.execute("SELECT student_id FROM students WHERE email=%s AND password=%s", (email, password))
    row = cursor.fetchone()
    if row:
        return True, row[0]  # return student_id
    return False, None

def get_all_books():
    cursor.execute("SELECT book_id, title, author, quantity FROM books")
    return cursor.fetchall()

def get_available_books():
    cursor.execute("SELECT book_id, title, author, quantity FROM books WHERE quantity > 0")
    return cursor.fetchall()

def get_student_issued_books(student_id):
    query = """
        SELECT ib.issue_id, b.title, b.author, ib.issue_date, ib.due_date, ib.return_date, ib.fine
        FROM issued_books ib
        JOIN books b ON ib.book_id = b.book_id
        WHERE ib.student_id=%s
    """
    cursor.execute(query, (student_id,))
    return cursor.fetchall()

def issue_book(student_id, book_id):
    # Check if book available
    cursor.execute("SELECT quantity FROM books WHERE book_id=%s", (book_id,))
    row = cursor.fetchone()
    if not row or row[0] <= 0:
        return False, "Book not available."

    # Issue book for 7 days
    issue_date = datetime.now().date()
    due_date = issue_date + timedelta(days=7)

    cursor.execute(
        "INSERT INTO issued_books (student_id, book_id, issue_date, due_date) VALUES (%s, %s, %s, %s)",
        (student_id, book_id, issue_date, due_date)
    )
    cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE book_id=%s", (book_id,))
    conn.commit()
    return True, "Book issued successfully."

def return_book(issue_id):
    return_date = datetime.now().date()
    cursor.execute("SELECT due_date, book_id FROM issued_books WHERE issue_id=%s AND return_date IS NULL", (issue_id,))
    row = cursor.fetchone()
    if not row:
        return False, "Invalid issue ID or book already returned."

    due_date, book_id = row
    days_late = (return_date - due_date).days
    fine = 0
    if days_late > 0:
        fine = days_late * 10

    cursor.execute(
        "UPDATE issued_books SET return_date=%s, fine=%s WHERE issue_id=%s",
        (return_date, fine, issue_id)
    )
    cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE book_id=%s", (book_id,))
    conn.commit()
    return True, f"Book returned successfully. Fine: ₹{fine}"

# -- LIBRARIAN --

def register_librarian(name, email, password):
    cursor.execute("SELECT * FROM librarians WHERE email=%s", (email,))
    if cursor.fetchone():
        return False, "Email already registered."
    cursor.execute("INSERT INTO librarians (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    conn.commit()
    return True, "Librarian registered successfully."

def login_librarian(email, password):
    cursor.execute("SELECT librarian_id FROM librarians WHERE email=%s AND password=%s", (email, password))
    row = cursor.fetchone()
    if row:
        return True
    return False

def add_book(title, author, quantity):
    cursor.execute("SELECT * FROM books WHERE title=%s AND author=%s", (title, author))
    if cursor.fetchone():
        return False, "Book already exists."
    cursor.execute("INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)", (title, author, quantity))
    conn.commit()
    return True, "Book added successfully."

def get_all_students():
    cursor.execute("SELECT student_id, name, email FROM students")
    return cursor.fetchall()

def get_all_issued_books():
    query = """
        SELECT ib.issue_id, s.name, b.title, ib.issue_date, ib.due_date, ib.return_date, ib.fine
        FROM issued_books ib
        JOIN students s ON ib.student_id = s.student_id
        JOIN books b ON ib.book_id = b.book_id
    """
    cursor.execute(query)
    return cursor.fetchall()
