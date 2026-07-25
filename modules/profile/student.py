class Student:
    "Represents a student in the system"
    def __init__(self, student_id, full_name, university, department, email):
        self.student_id = student_id
        self.full_name = full_name
        self.university = university
        self.department = department
        self.email = email

    def display_info(self):
        "Student Information:"
        print(f"Student ID: {self.student_id}")
        print(f"Full Name: {self.full_name}")
        print(f"University: {self.university}")
        print(f"Department: {self.department}")
        print(f"Email: {self.email}")