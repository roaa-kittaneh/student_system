from students.manager import (
    add_student,
    add_grade,
    get_top_students,
    export_to_json,
    export_to_csv,
)
from students.exceptions import (
    DuplicateStudentError,
    StudentNotFoundError,
    InvalidGradeError,
    InvalidEmailError,
)


def main():
    while True:
        print("\n1. Add Student")
        print("2. Add Grade")
        print("3. Top Students")
        print("4. Export JSON")
        print("5. Export CSV")
        print("6. Exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                sid = input("ID: ")
                name = input("Name: ")
                email = input("Email: ")
                add_student(sid, name, email)
                print("Student added")

            elif choice == "2":
                sid = input("Student ID: ")
                grade = float(input("Grade: "))
                add_grade(sid, grade)
                print("Grade added")

            elif choice == "3":
                top = get_top_students()
                for s in top:
                    print(s.name, "-", s.average())

            elif choice == "4":
                export_to_json()
                print("Exported to JSON")

            elif choice == "5":
                export_to_csv()
                print("Exported to CSV")

            elif choice == "6":
                break

            else:
                print("Invalid choice")

        except (
            DuplicateStudentError,
            StudentNotFoundError,
            InvalidGradeError,
            InvalidEmailError,
        ) as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
