from modules.profile.student import Student
from modules.profile.storage import save_student
def register_student():
    "Register a new student"
    student_id = input("Enter Student ID: ")
    full_name = input("Enter Full Name: ")
    university = input("Enter University: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")
    email = input("Enter Email: ")

    student = Student(student_id, full_name, university, department, semester, email)
    save_student(student)
    print("\nStudent registered successfully!")
    return student