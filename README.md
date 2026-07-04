# Student Management System

A web-based Student Management System built with **Flask** and **MS SQL Server**. It lets you add student records through a web form, view them all in an admin panel, and update or delete individual records.

This project was built to practice core web development concepts: object-oriented programming, Flask routing, database integration with SQLAlchemy, and CRUD operations (Create, Read, Update, Delete).

## Features

- **Add students** through a web form (name, age, class, and marks for Maths, Science, English)
- **View all students** in an admin panel table
- **Update** a student's details directly from the admin table
- **Delete** a student record
- **Automatic average** calculation of marks for each student
- Object-oriented design using abstraction, inheritance, and encapsulation

## Tech Stack

- **Python** – core language
- **Flask** – web framework
- **Flask-SQLAlchemy** – database ORM
- **MS SQL Server** – database (via pyodbc)
- **HTML + Jinja2** – frontend templates

## Project Structure

```
student_management_project/
├── route.py            # Main Flask app: routes and database model
├── student.py          # OOP classes: Person (abstract) and Student
├── templates/
│   ├── index.html      # Form to add a student
│   ├── admin.html      # Admin panel: view, update, delete
│   └── display.html    # Success page after adding a student
└── README.md
```

## How It Works

The app follows a clear flow from the user's input to the database:

1. The user fills in the form on `index.html` and submits it.
2. Flask receives the data in the `/submit` route.
3. A `Student` object is created (handles the OOP logic, like calculating the average).
4. A `Record` object is created and saved to the MS SQL Server database.
5. The admin panel (`/admin`) reads all records and displays them in a table, where they can be updated or deleted.

## Object-Oriented Design

The `student.py` file demonstrates three core OOP concepts:

- **Abstraction** – `Person` is an abstract base class that cannot be instantiated on its own.
- **Inheritance** – `Student` inherits common attributes (name, age) from `Person`.
- **Encapsulation** – attributes like name and age are private and accessed through getter methods.

## Routes

| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Home page (the add-student form) |
| `/add` | GET | Show the add-student form |
| `/submit` | POST | Save a new student to the database |
| `/admin` | GET | View all students in a table |
| `/update/<id>` | POST | Update one student's details |
| `/delete/<id>` | POST | Delete one student |

## Setup and Run

### Prerequisites

- Python 3.x installed
- MS SQL Server with a database named `StudentRecord`
- ODBC Driver 17 for SQL Server installed

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SehajKaur03/student-management-system.git
   cd student-management-system
   ```

2. Install the required packages:
   ```bash
   pip install flask flask-sqlalchemy pyodbc
   ```

3. Make sure your MS SQL Server is running and has a `StudentRecord` database with a `RECORD` table that matches the columns in `route.py`.

4. Run the app:
   ```bash
   python route.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Pages

- `http://127.0.0.1:5000/` — add a new student
- `http://127.0.0.1:5000/admin` — view, update, and delete students

## Future Improvements

- Add an admin login with sessions to protect the admin panel
- Add form validation and friendlier error messages
- Store the calculated average in the database
- Improve the UI with CSS styling

## Author

Built by **Sehaj Kaur** as a learning project to practice Flask, SQLAlchemy, and object-oriented programming.
