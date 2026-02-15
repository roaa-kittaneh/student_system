import json
import csv
from pathlib import Path
from typing import List

from .models import Student
from .exceptions import (
    DuplicateStudentError,
    StudentNotFoundError,
    InvalidGradeError,
    InvalidEmailError,
)

FILE_PATH = Path("students.json")


def load_students() -> List[Student]:
    if not FILE_PATH.exists():
        return []

    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            return [Student(**student) for student in data]
    except json.JSONDecodeError:
        return []


def save_students(students: List[Student]):
    with open(FILE_PATH, "w") as f:
        json.dump([student.__dict__ for student in students], f, indent=2)


def validate_email(email: str):
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format")


def add_student(student_id: str, name: str, email: str):
    students = load_students()

    if any(s.student_id == student_id for s in students):
        raise DuplicateStudentError("Student ID already exists")

    validate_email(email)

    student = Student(student_id, name, email)
    students.append(student)
    save_students(students)
    return student


def add_grade(student_id: str, grade: float):
    if grade < 0 or grade > 100:
        raise InvalidGradeError("Grade must be between 0 and 100")

    students = load_students()

    for student in students:
        if student.student_id == student_id:
            student.grades.append(grade)
            save_students(students)
            return student

    raise StudentNotFoundError("Student not found")


def get_top_students(n=3):
    students = load_students()
    return sorted(students, key=lambda s: s.average(), reverse=True)[:n]


def export_to_json(file_name="export_students.json"):
    students = load_students()
    with open(file_name, "w") as f:
        json.dump([s.__dict__ for s in students], f, indent=2)


def export_to_csv(file_name="export_students.csv"):
    students = load_students()
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Email", "Average"])
        for s in students:
            writer.writerow([s.student_id, s.name, s.email, s.average()])
