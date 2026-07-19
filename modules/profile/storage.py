import csv
import os
DATA_FILE = 'data/students.csv'

def save_student(student):
    file_exists = os.path.isfile(DATA_FILE)
    print(f"Saving student: {student.full_name}")

    with open(DATA_FILE, mode='a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(DATA_FILE) == 0:
            writer.writerow(['student_id', 'full_name', 'university', 'department', 'semester', 'email'])

        writer.writerow([student.student_id, student.full_name, student.university, student.department, student.semester, student.email])   

def get_student(student_id):
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["student_id"] == student_id:
                return row

    return None

def update_student_record(updated_student):
    students = []

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["student_id"] == updated_student["student_id"]:
                students.append(updated_student)
            else:
                students.append(row)

    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = [ "student_id", "full_name", "university", "department", "semester", "email"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)

def delete_student_record(student_id):
    students = []
    deleted = False

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["student_id"] == student_id:
                deleted = True
                continue
            students.append(row)    
            
    if deleted:
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["student_id", "full_name", "university", "department", "semester", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
            return deleted
        
def get_all_students():
    students = []

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students

def save_course(course):
    course_file = 'data/courses.csv'
    file_exists = os.path.isfile(course_file)
    print(f"Saving course: {course.course_name}")

    with open(course_file, mode='a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(course_file) == 0:
            writer.writerow(['student_id', 'semester', 'course_code', 'course_name', 'credit', 'marks', 'letter_grade', 'grade_point'])

        writer.writerow([course.student_id, course.semester, course.course_code, course.course_name, course.credit, course.marks, course.letter_grade, course.grade_point])