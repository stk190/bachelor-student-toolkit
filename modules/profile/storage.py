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