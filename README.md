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
<img width="267" height="145" alt="Screenshot 2026-02-15 131911" src="https://github.com/user-attachments/assets/b9e3a5a5-47b6-4c23-8120-513afb315e2c" />
<img width="272" height="172" alt="Screenshot 2026-02-15 131938" src="https://github.com/user-attachments/assets/8db757d1-d20c-40f2-870d-5b9043cfcce2" />
<img width="236" height="164" alt="Screenshot 2026-02-15 132233" src="https://github.com/user-attachments/assets/c7f8374f-2ee9-4a1c-b388-288570a160b1" />
<img width="738" height="625" alt="Screenshot 2026-02-15 132307" src="https://github.com/user-attachments/assets/e54dd197-6610-4cad-bfc5-a3307b75eb9a" />
<img width="728" height="673" alt="Screenshot 2026-02-15 132337" src="https://github.com/user-attachments/assets/4c2119e2-7e96-4e92-8f9e-27320fca415e" />
<img width="694" height="85" alt="Screenshot 2026-02-15 132420" src="https://github.com/user-attachments/assets/dfec616f-e078-4ce1-a9cc-7ff7b1d10d2a" />

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

