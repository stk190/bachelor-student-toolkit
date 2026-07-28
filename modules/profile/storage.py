import csv
import os

STUDENTS_FILE = 'data/students.csv'
COURSES_FILE = 'data/courses.csv'

STUDENT_FIELDS = ["student_id", "full_name", "university", "department", "email"]
COURSE_FIELDS = ["student_id", "semester", "course_code", "course_name",
                  "credit", "marks", "letter_grade", "grade_point"]


def ensure_file(filepath, fieldnames):
    """Create the folder/file with a header row if it doesn't exist yet."""
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(filepath):
        with open(filepath, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(fieldnames)
        print(f"\n'{filepath}' not found. A new file has been created.")



def save_student(student):
    ensure_file(STUDENTS_FILE, STUDENT_FIELDS)
    print(f"Saving student: {student.full_name}")

    try:
        with open(STUDENTS_FILE, mode='a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([student.student_id, student.full_name, student.university,
                              student.department, student.email])
    except Exception as e:
        print("Error saving student:", e)


def get_student(student_id):
    ensure_file(STUDENTS_FILE, STUDENT_FIELDS)

    try:
        with open(STUDENTS_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("student_id") == student_id:
                    return row
    except Exception as e:
        print("Error reading students:", e)

    return None


def update_student_record(updated_student):
    ensure_file(STUDENTS_FILE, STUDENT_FIELDS)
    students = []

    try:
        with open(STUDENTS_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("student_id") == updated_student["student_id"]:
                    students.append(updated_student)
                else:
                    students.append(row)
    except Exception as e:
        print("Error reading students:", e)
        return False

    try:
        with open(STUDENTS_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
            writer.writeheader()
            writer.writerows(students)
    except Exception as e:
        print("Error saving students:", e)
        return False

    return True


def delete_student_record(student_id):
    ensure_file(STUDENTS_FILE, STUDENT_FIELDS)
    students = []
    deleted = False

    try:
        with open(STUDENTS_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("student_id") == student_id:
                    deleted = True
                    continue
                students.append(row)
    except Exception as e:
        print("Error reading students:", e)
        return False

    if deleted:
        try:
            with open(STUDENTS_FILE, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
                writer.writeheader()
                writer.writerows(students)
        except Exception as e:
            print("Error saving students:", e)
            return False

    return deleted


def get_all_students():
    ensure_file(STUDENTS_FILE, STUDENT_FIELDS)
    students = []

    try:
        with open(STUDENTS_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except Exception as e:
        print("Error reading students:", e)
        return []

    return students



def save_course(course):
    ensure_file(COURSES_FILE, COURSE_FIELDS)
    print(f"Saving course: {course.course_name}")

    try:
        with open(COURSES_FILE, mode='a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([course.student_id, course.semester, course.course_code,
                              course.course_name, course.credit, course.marks,
                              course.letter_grade, course.grade_point])
    except Exception as e:
        print("Error saving course:", e)


def get_semester_courses(student_id, semester):
    ensure_file(COURSES_FILE, COURSE_FIELDS)
    courses = []

    try:
        with open(COURSES_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("student_id") == student_id and row.get("semester") == str(semester):
                    courses.append(row)
    except Exception as e:
        print("Error reading courses:", e)

    return courses


def get_all_courses(student_id):
    ensure_file(COURSES_FILE, COURSE_FIELDS)
    courses = []

    try:
        with open(COURSES_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("student_id") == student_id:
                    courses.append(row)
    except Exception as e:
        print("Error reading courses:", e)

    return courses


def get_all_courses_records():
    ensure_file(COURSES_FILE, COURSE_FIELDS)
    courses = []

    try:
        with open(COURSES_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                courses.append(row)
    except Exception as e:
        print("Error reading courses:", e)

    return courses