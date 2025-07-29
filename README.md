# Library Management System 
A simple DBMS-based mini project built using Python for managing a library's data.

## Overview
This system helps librarians and students manage:
- Book inventory
- Issuing/returning books
- Librarian and student records

## Features
- GUI for Librarian and Student using `tkinter`
- Backend logic using Python
- Database connectivity with MySQL (via mysql-connector)

## Technologies Used
- Python
- MySQL
- `tkinter` for GUI
- `mysql-connector-python` for DB connection

## How to Run 

Follow these steps to set up and run the project on your local machine:
### 1. Install Dependencies
Make sure you have Python and MySQL installed. Then, install the MySQL connector:
```bash
pip install mysql-connector-python
```
### 2. Set Up the Database
- Open MySQL and create a new database (e.g., `library_db`)
- Create the necessary tables based on the structure
- Update the database connection details (host, username, password, database name) in `backend.py`
### 3. Run the Application
To launch the main GUI interface:
```bash
python main.py
```
You can also run the GUIs individually:
```bash
python librarian_gui.py
python student_gui.py
```
### 4. Use the Interface
- The **Librarian GUI** allows managing books and issuing/returning them
- The **Student GUI** enables students to view book availability and their issue history

## .gitignore
See `.gitignore` for excluded files like `__pycache__`.
