import re


def validate_name(name):
    """Name must contain only letters and spaces, max 100 characters."""
    name = name.strip()

    if len(name) == 0:
        return False

    if len(name) > 100:
        return False

    return bool(re.fullmatch(r"[A-Za-z ]+", name))


def validate_student_id(student_id):
    """Student ID must be exactly 5 digits."""
    return bool(re.fullmatch(r"\d{5}", student_id))


def validate_university(university):
    """University name must contain only letters and spaces."""
    university = university.strip()

    if len(university) == 0:
        return False

    return bool(re.fullmatch(r"[A-Za-z ]+", university))


def validate_department(department):
    """Department name must contain only letters and spaces."""
    department = department.strip()

    if len(department) == 0:
        return False

    return bool(re.fullmatch(r"[A-Za-z ]+", department))


def validate_semester(semester):
    """Semester must be between 1 and 16."""
    if not semester.isdigit():
        return False

    semester = int(semester)
    return 1 <= semester <= 16


def validate_email(email):
    """Basic email validation."""
    return bool(re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email))

def validate_semester(semester):
    if not semester.isdigit():
        return False

    semester = int(semester)
    return 1 <= semester <= 16
def validate_course_count(count):
    if not count.isdigit():
        return False

    count = int(count)
    return 1 <= count <= 8
import re

def validate_course_code(code):
    pattern = r"^[A-Za-z]{2,4}\d{3}$"
    return bool(re.fullmatch(pattern, code))

def validate_course_name(name):
    if len(name) == 0 or len(name) > 100:
        return False

    return all(char.isalpha() or char.isspace() for char in name)

def validate_credit(credit):
    if not credit.isdigit():
        return False

    return int(credit) in [1, 2, 3]

def validate_course_count(count):
    if not count.isdigit():
        return False

    count = int(count)
    return 1 <= count <= 8