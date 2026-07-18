import csv
import os
DATA_FILE = 'data/students.csv'

def save_student(student):
    file_exists = os.path.isfile(DATA_FILE)

    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(DATA_FILE) == 0:
            writer.writerow(['Student ID', 'Full Name', 'University', 'Department', 'Semester', 'Email'])

            writer.writerow([student.student_id, student.full_name, student.university, student.department, student.semester, student.email])   
