# Student Management System

A simple command-line Student Management System built with Python.  
The project demonstrates object-oriented programming, clean project structure, exception handling, file exporting, and basic testing practices.

---

##  Features

- Register students (name, ID, email, grades)
- Update student grades
- List all students
- Show top students based on average grade
- Export student list to JSON
- Export student list to CSV
- Handle invalid input using custom exceptions
- Linted using flake8
- Tested with pytest

---
و
##  Project Structure
```
student_system/
│
├── main.py                # CLI entry point
├── students/
│   ├── __init__.py
│   ├── models.py          # Student class
│   ├── manager.py         # Business logic
│   ├── exceptions.py      # Custom exceptions
│   └── utils.py           # Export helpers
│
├── tests/
│   └── test_manager.py    # Unit tests
│
└── README.md
```
---

##  Installation

1. Clone the repository:

git clone <your-repo-link>  
cd student_system



2. Install dependencies:

pip install pytest flake8

---

##  Run the Application

python main.py

---

##  Run Tests

pytest

---

##  Check Code Style

python -m flake8 .

---

