from modules.profile import student
from modules.profile.course import Course
from modules.profile.student import Student
from modules.profile.storage import get_all_courses, save_course, save_student
from utils.grading import get_grade_point, get_letter_grade
from utils.validation import ( validate_course_count, validate_name, validate_student_id, validate_university, validate_department, validate_semester, validate_email )
from modules.profile.storage import get_student
from modules.profile.storage import update_student_record
from modules.profile.storage import delete_student_record
from utils.config import ADMIN_PASSKEY
from modules.profile.storage import get_all_students
from modules.profile.storage import get_semester_courses

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
            
def add_semester_courses():
    print("\n===== Add Semester Courses =====")

    # Student ID
    student_id = input("Enter Student ID: ").strip()

    while not validate_student_id(student_id):
        print("Invalid Student ID. Please enter a 5-digit number.")
        student_id = input("Enter Student ID: ").strip()

    student = get_student(student_id)

    if student is None:
        print("\nStudent not found.")
        return

    print(f"\nStudent: {student['full_name']}")

    # Total completed semesters
    completed_semesters = input("How many semesters have you completed? ").strip()

    while not validate_semester(completed_semesters):
        print("Invalid number of semesters.")
        completed_semesters = input("How many semesters have you completed? ").strip()

    semester_count = int(completed_semesters)

    # Loop through each semester
    for semester in range(1, semester_count + 1):

        print(f"\n========== Semester {semester} ==========")

        # Number of courses
        course_count = input("Number of Courses: ").strip()

        while not validate_course_count(course_count):
            print("Invalid number of courses.")
            course_count = input("Number of Courses: ").strip()

        course_count = int(course_count)

        # Loop through each course
        for i in range(course_count):

            print(f"\n----- Course {i+1} -----")

            # Course Code
            course_code = input("Course Code: ").strip()

            # Course Name
            course_name = input("Course Name: ").strip()

            while not validate_name(course_name):
                print("Invalid Course Name.")
                course_name = input("Course Name: ").strip()

            # Credit
            credit = input("Credit: ").strip()

            while not credit.isdigit() or int(credit) not in [1, 2, 3, 4]:
                print("Credit must be 1, 2, 3 or 4.")
                credit = input("Credit: ").strip()

            credit = int(credit)

            # Marks
            marks = input("Marks (0-100): ").strip()

            while True:
                try:
                    marks = float(marks)

                    if 0 <= marks <= 100:
                        break

                    print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

                marks = input("Marks (0-100): ").strip()

            # Calculate grade
            letter_grade = get_letter_grade(marks)
            grade_point = get_grade_point(marks)

            # Create Course object
            course = Course(
                student_id,
                semester,
                course_code,
                course_name,
                credit,
                marks,
                letter_grade,
                grade_point
            )

            # Save course
            save_course(course)

            # Display summary
            print("\n===== Course Summary =====")
            print(f"Semester     : {semester}")
            print(f"Course Code  : {course.course_code}")
            print(f"Course Name  : {course.course_name}")
            print(f"Credit       : {course.credit}")
            print(f"Marks        : {course.marks}")
            print(f"Letter Grade : {course.letter_grade}")
            print(f"Grade Point  : {course.grade_point}")

    print("\nAll semester records saved successfully!")

def view_semester_courses():
    print("\n===== View Semester Courses =====")

    student_id = input("Enter Student ID: ").strip()

    while not validate_student_id(student_id):
        print("Invalid Student ID. Please enter a 5-digit number.")
        student_id = input("Enter Student ID: ").strip()

    student = get_student(student_id)

    if student is None:
        print("\nStudent not found.")
        return

    print(f"\nStudent: {student['full_name']}")

    semester = input("Enter Semester to view: ").strip()

    while not validate_semester(semester):
        print("Invalid Semester. Please enter a valid semester.")
        semester = input("Enter Semester to view: ").strip()

    courses = get_semester_courses(student_id, semester)

    if not courses:
        print(f"\nNo courses found for Semester {semester}.")
        return

    print(f"\n===== Courses for Semester {semester} =====")
    for course in courses:
        print(f"\nCourse Code  : {course['course_code']}")
        print(f"Course Name  : {course['course_name']}")
        print(f"Credit       : {course['credit']}")
        print(f"Marks        : {course['marks']}")
        print(f"Letter Grade : {course['letter_grade']}")
        print(f"Grade Point  : {course['grade_point']}")

def calculate_semester_gpa():
    print("\n===== Calculate Semester GPA =====")

    student_id = input("Enter Student ID: ").strip()

    while not validate_student_id(student_id):
        print("Invalid Student ID. Please enter a 5-digit number.")
        student_id = input("Enter Student ID: ").strip()

    selected_semester = input("Enter Semester: ").strip()

    while not validate_semester(selected_semester):
        print("Invalid Semester. Please enter a valid semester.")
        selected_semester = input("Enter Semester: ").strip()   

    courses = get_semester_courses(student_id, selected_semester)
    if not courses:
        print(f"\nNo courses found for Semester {selected_semester}.")
        return 
    total_credits = 0
    total_grade_points = 0 
    
    for course in courses:
        credit = float(course["credit"])
        grade_point = float(course["grade_point"])

        total_credits += credit
        total_grade_points += credit * grade_point

    semester_gpa = total_grade_points / total_credits if total_credits > 0 else 0
    print(f"\n===== Semester GPA for Semester {selected_semester} =====")
    print(f"\nStudent ID: {student_id}")
    print(f"\nStudent Name: {get_student(student_id)['full_name']}")
    print(f"\nSemester: {selected_semester}")
    print(f"\nTotal Credits for Semester {selected_semester}: {total_credits}")
    print(f"\nSemester GPA for {selected_semester}: {semester_gpa:.2f}")

def calculate_overall_cgpa():
    print("\n===== Calculate Overall CGPA =====")

    student_id = input("Enter Student ID: ").strip()

    semesters = set()
    for course in courses:
        semesters.add(course["semester"])
    
    semester_count = len(semesters)

    while not validate_student_id(student_id):
        print("Invalid Student ID. Please enter a 5-digit number.")
        student_id = input("Enter Student ID: ").strip()

    courses = get_all_courses(student_id)
    total_courses = len(courses)
    if not courses:
        print(f"\nNo courses found for Student ID {student_id}.")
        return 

    total_credits = 0
    total_grade_points = 0 

    for course in courses:
        credit = float(course["credit"])
        grade_point = float(course["grade_point"])

        total_credits += credit
        total_grade_points += credit * grade_point

    overall_cgpa = total_grade_points / total_credits if total_credits > 0 else 0
    print(f"\n===== Overall CGPA =====")
    print(f"\nStudent ID: {student_id}")
    print(f"\nStudent Name: {student['full_name']}")
    print(f"\nTotal Semesters Taken: {semester_count}")
    print(f"\nTotal Courses: {total_courses}")
    print(f"\nTotal Credits: {total_credits}")
    print(f"\nOverall CGPA: {overall_cgpa:.2f}")