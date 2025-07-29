# Library Management System 🏫📚

A simple DBMS-based mini project built using Python for managing a library's data.

## 💡 Overview

This system helps librarians and students manage:

- Book inventory
- Issuing/returning books
- Librarian and student records

## 🧩 Features

- GUI for Librarian and Student using `tkinter`
- Backend logic using Python
- Database connectivity with MySQL (via mysql-connector)
- Screenshots and ER diagrams included

## 🗃️ File Structure

```
library-management-system/
├── backend/
│   ├── backend.py                # DB and core logic
│   ├── librarian_gui.py         # GUI for librarian
│   ├── student_gui.py           # GUI for student
│   ├── main.py                  # Entry point
│   └── *.png                    # ER diagrams, screenshots
├── frontend/
│   └── mysql connector.png      # Connection setup screenshot
```

## 🛠️ Technologies Used

- Python
- MySQL
- `tkinter` for GUI
- `mysql-connector-python` for DB connection

## 📷 ER Diagrams & Screenshots

Check the `/backend` and `/frontend` folders for:

- Books table
- Students table
- Librarians table
- Issued books
- Table creation schema

## 🚫 .gitignore

See `.gitignore` for excluded files like `__pycache__`.

---

## ✍️ Author

Joyson (2nd Year AIML Student)
