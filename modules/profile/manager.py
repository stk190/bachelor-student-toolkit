import numpy as np

from modules.profile import student
from modules.profile.course import Course
from modules.profile.student import Student
from modules.profile.storage import get_all_students, get_semester_courses, get_student, update_student_record, delete_student_record, get_all_courses, get_all_courses_records, save_course, save_student, get_all_students, get_all_courses


from utils.grading import get_grade_point, get_letter_grade
from utils.config import ADMIN_PASSKEY
from utils.input_utils import user_input
from utils.validation import validate_course_count, validate_name, validate_student_id, validate_university, validate_department, validate_semester, validate_email, validate_course_code, validate_credit

def register_student():
    print("\n==== Register a new student ====\n")

    while True:
        student_id = user_input("Enter Student ID: ").strip()

        while student_id == "" or not validate_student_id(student_id):
            print("Invalid Student ID. Please enter a 5-digit number.")
            student_id = user_input("Enter Student ID: ").strip()

        if get_student(student_id):
            print("This Student ID is already registered. Please enter a different one.")
            continue

        break

    ##full name
    full_name = user_input("Enter Full Name: ").strip()
    while full_name == "" or not validate_name(full_name):
        print("\nInvalid Full Name. Please enter a valid name.")
        full_name = user_input("Enter Full Name: ").strip()

    ##university
    university = user_input("Enter University: ").strip()
    while university == "" or not validate_university(university):
        print("\nInvalid University. Please enter a valid university name.")
        university = user_input("Enter University: ").strip()

    ##department
    department = user_input("Enter Department: ").strip()
    while department == "" or not validate_department(department):
        print("\nInvalid Department. Please enter a valid department name.")
        department = user_input("Enter Department: ").strip()

    ##email
    email = user_input("Enter Email: ").strip()
    while email == "" or not validate_email(email):
        print("\nInvalid Email. Please enter a valid email address.")
        email = user_input("Enter Email: ").strip()

    student = Student(student_id, full_name, university, department, email)
    save_student(student)
    print("\n==== Student registered successfully!====\n")
    return student


def view_student():
    print("\n ==== View Student Profile ==== \n")

    student_id = user_input("Enter Student ID: ")

    student = get_student(student_id)

    if student:
        print("\n==== Student Information ====")
        print(f"Student ID : {student['student_id']}")
        print(f"Full Name  : {student['full_name']}")
        print(f"University : {student['university']}")
        print(f"Department : {student['department']}")
        print(f"Email      : {student['email']}")
        print("\n===============================\n")
    else:
        print("\n Student not found!!! ")


def update_student():
    print("\n===== Update Student Profile =====")

    student_id = user_input("Enter Student ID: ").strip()

    student = get_student(student_id)

    if not student:
        print("\n==== Student not found. ====  ")
        return

    print("\n==== Current Information ====")
    print(f"Name       : {student['full_name']}")
    print(f"University : {student['university']}")
    print(f"Department : {student['department']}")
    print(f"Email      : {student['email']}")
    print("==============================\n")

    print("\n==== Leave a field empty to keep the current value.==== \n")

    full_name = user_input("New Full Name: ").strip()
    university = user_input("New University: ").strip()
    department = user_input("New Department: ").strip()
    email = user_input("New Email: ").strip()

    if full_name:
        if not validate_name(full_name):
            print("\nInvalid Full Name. Keeping previous value.")
        else:
            student["full_name"] = full_name

    if university:
        if not validate_university(university):
            print("\nInvalid University. Keeping previous value.")
        else:
            student["university"] = university

    if department:
        if not validate_department(department):
            print("\nInvalid Department. Keeping previous value.")
        else:
            student["department"] = department

    if email:
        if not validate_email(email):
            print("\nInvalid Email. Keeping previous value.")
        else:
            student["email"] = email

    if update_student_record(student):
        print("\n==== Student updated successfully! ====")
    else:
        print("\n==== Failed to update student. ====")


def delete_student():

    print("\n===== Delete Student Profile =====")

    student_id = user_input("Enter Student ID: ").strip()

    student = get_student(student_id)

    if not student:
        print("\n==== Student not found. ====")
        return

    print("\n==== Student Found ====\n")
    print(f"Student ID : {student['student_id']}")
    print(f"Full Name  : {student['full_name']}")
    print(f"University : {student['university']}")
    print(f"Department : {student['department']}")
    print(f"Email      : {student['email']}")
    print("==============================")

    confirm = user_input("\nAre you sure you want to delete this student? (Y/N): ").strip().upper()

    if confirm == "Y":
        if delete_student_record(student_id):
            print("\n==== Student deleted successfully! ====")
        else:
            print("\n==== Failed to delete student. ====")

    elif confirm == "N":
        print("\n==== Deletion cancelled. ====")

    else:
        print("\n==== Invalid choice. Deletion cancelled. ====")


def view_all_students(passkey):
    if passkey != ADMIN_PASSKEY:
        print("\nAccess Denied. Invalid passkey.")
        return

    print("\n===== All Students =====")

    students = get_all_students()

    if not students:
        print("\nNo students found.")
        return
    print("\n====================================")
    for student in students:

            print(f"\nStudent ID : {student['student_id']}")
            print(f"Full Name  : {student['full_name']}")
            print(f"University : {student['university']}")
            print(f"Department : {student['department']}")
            print(f"Email      : {student['email']}")
            print("====================================")


def add_semester_courses():
    print("\n===== Add Semester Courses =====")

    # Student ID
    student_id = user_input("Enter Student ID: ").strip()

    while not validate_student_id(student_id):
        print("Invalid Student ID. Please enter a 5-digit number.")
        student_id = user_input("Enter Student ID: ").strip()

    student = get_student(student_id)

    if student is None:
        print("\nStudent not found.")
        return

    print(f"\nStudent: {student['full_name']}")

    # ---- Check for previously stored semester/course data ----
    existing_courses = get_all_courses(student_id)

    if existing_courses:
        existing_semesters = sorted(set(int(course["semester"]) for course in existing_courses))
        last_semester = max(existing_semesters)

        print("\n===== Previous Records Found =====")
        print(f"Semesters already recorded : {', '.join(str(s) for s in existing_semesters)}")
        print(f"Total courses recorded     : {len(existing_courses)}")

        for sem in existing_semesters:
            sem_courses = [c for c in existing_courses if int(c["semester"]) == sem]
            print(f"\n-- Semester {sem} ({len(sem_courses)} course(s)) --")
            for c in sem_courses:
                print(f"  {c['course_code']} - {c['course_name']} "
                      f"(Credit: {c['credit']}, Grade: {c['letter_grade']})")
        print("===================================")

        print(f"\nNew semesters will continue from Semester {last_semester + 1}.")
        start_semester = last_semester + 1
    else:
        print("\nNo previous records found. Starting from Semester 1.")
        start_semester = 1

    # Number of NEW semesters to add
    new_semester_input = user_input("How many new semesters do you want to add? ").strip()

    while (not validate_semester(new_semester_input)
           or start_semester + int(new_semester_input) - 1 > 16):
        print("Invalid number of semesters, or it would exceed the 16-semester limit.")
        new_semester_input = user_input("How many new semesters do you want to add? ").strip()

    new_semester_count = int(new_semester_input)

    # Loop through each NEW semester, continuing the chain
    for semester in range(start_semester, start_semester + new_semester_count):

        print(f"\n========== Semester {semester} ==========")

        # Number of courses
        course_count = user_input("Number of Courses: ").strip()

        while not validate_course_count(course_count):
            print("Invalid number of courses.")
            course_count = user_input("Number of Courses: ").strip()

        course_count = int(course_count)

        used_course_codes = set()

        for i in range(course_count):

            print(f"\n----- Course {i+1} -----")

            course_code = user_input("Course Code (e.g. CSE101): ").strip().upper()

            while not validate_course_code(course_code) or course_code in used_course_codes:
                if course_code in used_course_codes:
                    print("You already entered this course code for this semester.")
                else:
                    print("Invalid Course Code. Format must be 2-4 letters followed by 3 digits (e.g. CSE101).")
                course_code = user_input("Course Code (e.g. CSE101): ").strip().upper()

            used_course_codes.add(course_code)

            course_name = user_input("Course Name: ").strip()

            while not validate_name(course_name):
                print("Invalid Course Name.")
                course_name = user_input("Course Name: ").strip()

            credit = user_input("Credit: ").strip()

            while not validate_credit(credit):
                print("Credit must be 1, 2, 3 or 4.")
                credit = user_input("Credit: ").strip()

            credit = int(credit)

            marks = user_input("Marks (0-100): ").strip()

            while True:
                try:
                    marks = float(marks)

                    if 0 <= marks <= 100:
                        break

                    print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

                marks = user_input("Marks (0-100): ").strip()

            letter_grade = get_letter_grade(marks)
            grade_point = get_grade_point(marks)

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

            save_course(course)

            print("\n===== Course Summary =====")
            print(f"Semester     : {semester}")
            print(f"Course Code  : {course.course_code}")
            print(f"Course Name  : {course.course_name}")
            print(f"Credit       : {course.credit}")
            print(f"Marks        : {course.marks}")
            print(f"Letter Grade : {course.letter_grade}")
            print(f"Grade Point  : {course.grade_point}")

    print("\nAll new semester records saved successfully!")

def view_semester_courses():
    print("\n===== View Semester Courses =====")

    student_id = user_input("Enter Student ID: ").strip()

    while not validate_student_id(student_id):
        print("Invalid Student ID. Please enter a 5-digit number.")
        student_id = user_input("Enter Student ID: ").strip()

    student = get_student(student_id)

    if student is None:
        print("\nStudent not found.")
        return

    print(f"\nStudent: {student['full_name']}")

    semester = user_input("Enter Semester to view: ").strip()

    while not validate_semester(semester):
        print("Invalid Semester. Please enter a valid semester.")
        semester = user_input("Enter Semester to view: ").strip()

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

    student_id = user_input("Enter Student ID: ").strip()

    while not validate_student_id(student_id):
        print("Invalid Student ID. Please enter a 5-digit number.")
        student_id = user_input("Enter Student ID: ").strip()

    student = get_student(student_id)

    if student is None:
        print("\nStudent not found.")
        return

    selected_semester = user_input("Enter Semester: ").strip()

    while not validate_semester(selected_semester):
        print("Invalid Semester. Please enter a valid semester.")
        selected_semester = user_input("Enter Semester: ").strip()

    courses = get_semester_courses(student_id, selected_semester)
    if not courses:
        print(f"\nNo courses found for Semester {selected_semester}.")
        return

    total_credits = 0
    total_grade_points = 0

    for course in courses:
        try:
            credit = float(course["credit"])
            grade_point = float(course["grade_point"])
        except (KeyError, ValueError, TypeError):
            print(f"Skipping a corrupted course record for course code '{course.get('course_code', '?')}'.")
            continue

        total_credits += credit
        total_grade_points += credit * grade_point

    semester_gpa = total_grade_points / total_credits if total_credits > 0 else 0
    print(f"\n===== Semester GPA for Semester {selected_semester} =====")
    print(f"\nStudent ID: {student_id}")
    print(f"\nStudent Name: {student['full_name']}")
    print(f"\nSemester: {selected_semester}")
    print(f"\nTotal Credits for Semester {selected_semester}: {total_credits}")
    print(f"\nSemester GPA for {selected_semester}: {semester_gpa:.2f}")


def calculate_overall_cgpa():
    print("\n===== Calculate Overall CGPA =====")

    student_id = user_input("Enter Student ID: ").strip()

    while not validate_student_id(student_id):
        print("Invalid Student ID. Please enter a 5-digit number.")
        student_id = user_input("Enter Student ID: ").strip()

    student = get_student(student_id)

    if student is None:
        print("\nStudent not found.")
        return

    courses = get_all_courses(student_id)

    if not courses:
        print(f"\nNo courses found for Student ID {student_id}.")
        return

    semesters = set()
    total_credits = 0
    total_grade_points = 0
    valid_course_count = 0

    for course in courses:
        semesters.add(course.get("semester"))

        try:
            credit = float(course["credit"])
            grade_point = float(course["grade_point"])
        except (KeyError, ValueError, TypeError):
            print(f"Skipping a corrupted course record for course code '{course.get('course_code', '?')}'.")
            continue

        total_credits += credit
        total_grade_points += credit * grade_point
        valid_course_count += 1

    semester_count = len(semesters)

    if total_credits == 0:
        print("\nNo valid course records to calculate CGPA.")
        return

    overall_cgpa = total_grade_points / total_credits

    print("\n===== Overall CGPA =====")
    print(f"Student ID                : {student_id}")
    print(f"Student Name              : {student['full_name']}")
    print(f"Completed Semesters       : {semester_count}")
    print(f"Total Courses             : {valid_course_count}")
    print(f"Total Credits             : {total_credits}")
    print(f"Overall CGPA              : {overall_cgpa:.2f}")


def view_transcript():
    print("\n========== VIEW TRANSCRIPT ==========")

    # Student ID
    student_id = user_input("Enter Student ID: ").strip()

    while not validate_student_id(student_id):
        print("Invalid Student ID. Please enter a 5-digit number.")
        student_id = user_input("Enter Student ID: ").strip()

    # Check student
    student = get_student(student_id)

    if student is None:
        print("\nStudent not found.")
        return

    # Get all courses
    courses = get_all_courses(student_id)

    if not courses:
        print("\nNo academic records found.")
        return

    print("\n============= TRANSCRIPT =============")
    print(f"Student ID   : {student['student_id']}")
    print(f"Student Name : {student['full_name']}")
    print(f"University   : {student['university']}")
    print(f"Department   : {student['department']}")

    current_semester = None

    semester_credits = 0
    semester_points = 0

    overall_credits = 0
    overall_points = 0
    valid_course_count = 0
    all_semesters = set()

    for course in courses:

        semester_value = course.get("semester")

        # Print previous semester GPA before moving to next semester
        if current_semester is not None and current_semester != semester_value:

            semester_gpa = semester_points / semester_credits if semester_credits > 0 else 0

            print("---------------------------------------")
            print(f"Semester GPA : {semester_gpa:.2f}")

            semester_credits = 0
            semester_points = 0

        # New semester heading
        if current_semester != semester_value:
            current_semester = semester_value

            print(f"\n========== Semester {current_semester} ==========")

        # Print course
        print(f"\nCourse Code  : {course.get('course_code', '?')}")
        print(f"Course Name  : {course.get('course_name', '?')}")
        print(f"Credit       : {course.get('credit', '?')}")
        print(f"Marks        : {course.get('marks', '?')}")
        print(f"Letter Grade : {course.get('letter_grade', '?')}")
        print(f"Grade Point  : {course.get('grade_point', '?')}")

        try:
            credit = float(course["credit"])
            point = float(course["grade_point"])
        except (KeyError, ValueError, TypeError):
            print("(Skipped from GPA calculation — corrupted record.)")
            continue

        all_semesters.add(semester_value)
        valid_course_count += 1

        semester_credits += credit
        semester_points += credit * point

        overall_credits += credit
        overall_points += credit * point

    # Last semester GPA
    if semester_credits > 0:
        semester_gpa = semester_points / semester_credits

        print("---------------------------------------")
        print(f"Semester GPA : {semester_gpa:.2f}")

    # Overall CGPA
    overall_cgpa = 0

    if overall_credits > 0:
        overall_cgpa = overall_points / overall_credits

    print("\n=======================================")
    print(f"Completed Semesters : {len(all_semesters)}")
    print(f"Total Courses       : {valid_course_count}")
    print(f"Total Credits       : {overall_credits}")
    print(f"Overall CGPA        : {overall_cgpa:.2f}")
    print("=======================================")


def dashboard_statistics(passkey):
    passkey = user_input("Enter admin passkey: ")
    if passkey != ADMIN_PASSKEY:
        print("Access denied. Invalid passkey.")
        return

    print("\n========== Dashboard ==========")

    students = get_all_students()
    courses = get_all_courses_records()

    total_students = len(students)
    total_courses = len(courses)

    cgpa_list = []

    for student in students:
        student_courses = get_all_courses(student["student_id"])

        if not student_courses:
            continue

        total_credit = 0
        total_point = 0

        for course in student_courses:
            try:
                credit = float(course["credit"])
                point = float(course["grade_point"])
            except (KeyError, ValueError, TypeError):
                continue

            total_credit += credit
            total_point += credit * point

        if total_credit > 0:
            cgpa = total_point / total_credit
            cgpa_list.append(cgpa)

    print(f"\nTotal Students           : {total_students}")
    print(f"Total Registered Courses : {total_courses}")

    if cgpa_list:
        cgpa_array = np.array(cgpa_list)

        print(f"Average CGPA            : {np.mean(cgpa_array):.2f}")
        print(f"Highest CGPA            : {np.max(cgpa_array):.2f}")
        print(f"Lowest CGPA             : {np.min(cgpa_array):.2f}")
        print(f"Median CGPA             : {np.median(cgpa_array):.2f}")
        print(f"Standard Deviation      : {np.std(cgpa_array):.2f}")
    else:
        print("No CGPA data available yet.")

    print("===============================")