from modules.profile.student import Student
from modules.profile.storage import save_student
from utils.validation import ( validate_name, validate_student_id, validate_university, validate_department, validate_semester, validate_email )
from modules.profile.storage import get_student
from modules.profile.storage import update_student_record
from modules.profile.storage import delete_student_record
from utils.config import ADMIN_PASSKEY
from modules.profile.storage import get_all_students

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

def update_student():
    print("\n===== Update Student Profile =====")

    student_id = input("Enter Student ID: ").strip()

    student = get_student(student_id)

    if not student:
        print("\nStudent not found.")
        return

    print("\nCurrent Information")
    print(f"Name       : {student['full_name']}")
    print(f"University : {student['university']}")
    print(f"Department : {student['department']}")
    print(f"Semester   : {student['semester']}")
    print(f"Email      : {student['email']}")

    print("\nLeave a field empty to keep the current value.\n")

    full_name = input("New Full Name: ").strip()
    university = input("New University: ").strip()
    department = input("New Department: ").strip()
    semester = input("New Semester: ").strip()
    email = input("New Email: ").strip()

    if full_name:
        student["full_name"] = full_name

    if university:
        student["university"] = university

    if department:
        student["department"] = department

    if semester:
        student["semester"] = semester

    if email:
        student["email"] = email

    update_student_record(student)

    print("\nStudent updated successfully!")

def delete_student():
    
    print("\n===== Delete Student Profile =====")

    student_id = input("Enter Student ID: ").strip()

    student = get_student(student_id)

    if not student:
        print("\nStudent not found.")
        return

    print("\nStudent Found")
    print(f"Student ID : {student['student_id']}")
    print(f"Full Name  : {student['full_name']}")
    print(f"University : {student['university']}")
    print(f"Department : {student['department']}")
    print(f"Semester   : {student['semester']}")
    print(f"Email      : {student['email']}")

    confirm = input("\nAre you sure you want to delete this student? (Y/N): ").strip().upper()

    if confirm == "Y":
        if delete_student_record(student_id):
            print("\nStudent deleted successfully!")
        else:
            print("\nFailed to delete student.")

    elif confirm == "N":
        print("\nDeletion cancelled.")

    else:
        print("\nInvalid choice. Deletion cancelled.")

def view_all_students(passkey):
    if passkey != ADMIN_PASSKEY:
        print("\nAccess Denied. Invalid passkey.")
        return

    print("\n===== All Students =====")

    students = get_all_students()

    if not students:
        print("\nNo students found.")
        return

    for student in students:
            print(f"\nStudent ID : {student['student_id']}")
            print(f"Full Name  : {student['full_name']}")
            print(f"University : {student['university']}")
            print(f"Department : {student['department']}")
            print(f"Semester   : {student['semester']}")
            print(f"Email      : {student['email']}")
            