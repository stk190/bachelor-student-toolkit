from modules.profile.student import Student

def register_student():
    "Register a new student"
    student_id = input("Enter Student ID: ")
    full_name = input("Enter Full Name: ")
    university = input("Enter University: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")
    email = input("Enter Email: ")

    student = Student(student_id, full_name, university, department, semester, email)
    print("\nStudent registered successfully!")
    return student