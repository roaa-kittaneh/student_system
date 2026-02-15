import pytest
from students.manager import (
    add_student,
    add_grade,
    get_top_students,
)
from students.exceptions import (
    DuplicateStudentError,
    InvalidGradeError,
)


def test_add_student():
    student = add_student("S001", "Ali", "ali@email.com")
    assert student.name == "Ali"


def test_duplicate_student():
    add_student("S002", "Sara", "sara@email.com")
    with pytest.raises(DuplicateStudentError):
        add_student("S002", "Sara2", "sara2@email.com")


def test_invalid_grade():
    add_student("S003", "Omar", "omar@email.com")
    with pytest.raises(InvalidGradeError):
        add_grade("S003", 150)


def test_add_grade():
    add_student("S004", "Lina", "lina@email.com")
    student = add_grade("S004", 90)
    assert 90 in student.grades


def test_top_students():
    add_student("S005", "Top", "top@email.com")
    add_grade("S005", 100)
    top = get_top_students(1)
    assert top[0].student_id == "S005"
