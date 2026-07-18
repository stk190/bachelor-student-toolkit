from modules.profile.student import Student
from modules.profile.storage import save_student
from utils.validation import ( validate_name, validate_student_id, validate_university, validate_department, validate_semester, validate_email )
from modules.profile.storage import get_student

def register_student():
    "Register a new student"
    ##ID
    student_id = input("Enter Student ID: ").strip()
    while student_id=="" or not validate_student_id(student_id):
        print("Invalid Student ID. Please enter a 5-digit number.")
        student_id = input("Enter Student ID: ").strip()

    ##full name
    full_name = input("Enter Full Name: ").strip()
    while full_name=="" or not validate_name(full_name):
        print("Invalid Full Name. Please enter a valid name.")
        full_name = input("Enter Full Name: ").strip()

    ##university
    university = input("Enter University: ").strip()
    while university=="" or not validate_university(university):
        print("Invalid University. Please enter a valid university name.")
        university = input("Enter University: ").strip()

    ##department
    department = input("Enter Department: ").strip()
    while department=="" or not validate_department(department):
        print("Invalid Department. Please enter a valid department name.")
        department = input("Enter Department: ").strip()
    ##semester
    semester = input("Enter Semester: ").strip()
    while semester=="" or not validate_semester(semester):
        print("Invalid Semester. Please enter a valid semester.")
        semester = input("Enter Semester: ").strip()
    ##email
    email = input("Enter Email: ").strip()
    while email=="" or not validate_email(email):
        print("Invalid Email. Please enter a valid email address.")
        email = input("Enter Email: ").strip()

    student = Student(student_id, full_name, university, department, semester, email)
    save_student(student)
    print("\nStudent registered successfully!")
    return student

def view_student():
    print("\n View Student Profile ")

    student_id = input("Enter Student ID: ")

    student = get_student(student_id)

    if student:
        print("\n Student Information")
        print(f"Student ID : {student['student_id']}")
        print(f"Full Name  : {student['full_name']}")
        print(f"University : {student['university']}")
        print(f"Department : {student['department']}")
        print(f"Semester   : {student['semester']}")
        print(f"Email      : {student['email']}")
    else:
        print("\nStudent not found.")