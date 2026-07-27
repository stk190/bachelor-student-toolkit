# Bachelor Student Toolkit

Bachelor Student Toolkit is a Python command-line application developed as a midterm group project for the **Programming in Python** course, Summer 25-26 semester, American International University-Bangladesh (AIUB). The project is divided into four modules, with each team member responsible for one module.

**Current Module Status:**

| Module | Status |
|---|---|
| Student Profile & Academic Records | ✅ Completed |
| Class Routine & Exam Schedule | 🚧 In Progress |
| Expense Tracker | ✅ Completed |
| Study Planner | 🚧 In Progress |

---

## Student Profile & Academic Records

This module manages student information and academic records. All data is persisted using CSV files, and the program automatically creates those files (with the correct headers) if they don't already exist — no manual setup required.

### Features

#### Student Management

- Register Student — validates all fields and rejects duplicate Student IDs
- View Student Profile
- Update Student Profile — re-validates any field you change; leaves a field untouched if left blank
- Delete Student Profile (with confirmation prompt)
- View All Students (Admin Protected)

#### Academic Records

- Add Semester Courses — **chained entry**: if a student already has courses saved from a previous session, the previous semesters and courses are shown first, and new entries continue from the next semester onward instead of overwriting existing data
- View Semester Courses
- Calculate Semester GPA
- Calculate Overall CGPA
- View Student Transcript

#### Dashboard (Admin Protected)

- Total Students
- Total Registered Courses
- Average / Highest / Lowest / Median CGPA
- CGPA Standard Deviation

*(Dashboard statistics are computed using NumPy.)*

---

## AIUB Grading System

The application follows the AIUB grading policy.

| Marks | Grade | Grade Point |
|-------|-------|-------------|
| 90 - 100 | A+ | 4.00 |
| 85 - 89.99 | A | 3.75 |
| 80 - 84.99 | B+ | 3.50 |
| 75 - 79.99 | B | 3.25 |
| 70 - 74.99 | C+ | 3.00 |
| 65 - 69.99 | C | 2.75 |
| 60 - 64.99 | D+ | 2.50 |
| 50 - 59.99 | D | 2.25 |
| Below 50 | F | 0.00 |

The system automatically converts marks into letter grades and grade points.

---

## Input Validation

The module validates:

- Student ID (exactly 5 digits, must not already be registered)
- Full Name / University / Department (letters and spaces only)
- Email Address (standard email format)
- Semester (1–16)
- Number of Courses per semester (1–8)
- Course Code (2–4 letters followed by 3 digits, e.g. `CSE101`; duplicate course codes within the same semester entry are rejected)
- Course Credit (1, 2, 3, or 4)
- Marks (numeric, 0–100)

---

## Error Handling

- Missing `students.csv` / `courses.csv` files are created automatically on first use instead of crashing the program.
- Corrupted or incomplete rows in either CSV are skipped (with a message) during GPA/CGPA/transcript calculations instead of stopping the whole operation.
- Non-numeric input for marks is caught and re-prompted using `try`/`except`.
- GPA/CGPA calculations guard against division by zero when no valid credit-bearing courses exist.

---

## Data Storage

Student information is stored in:

```
data/students.csv
```

Course information is stored in:

```
data/courses.csv
```

No database is used in this project.

---

## Project Structure

```text
bachelor-student-toolkit/
│
├── data/
│   ├── students.csv
│   └── courses.csv
│
├── modules/
│   ├── profile/
│   │   ├── manager.py
│   │   ├── profile.py
│   │   ├── storage.py
│   │   ├── student.py
│   │   └── course.py
│   ├── routine/        (pending)
│   ├── expenses/        (pending)
│   └── planner/        (pending)
│
├── utils/
│   ├── grading.py
│   ├── validation.py
│   ├── input_utils.py
│   └── config.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

Type `exit` or `0` at any prompt to quit the program immediately.

---

## Technologies Used

- Python 3
- NumPy
- CSV Files
- Object-Oriented Programming (OOP)
- Git & GitHub

---

## Future Work

The remaining modules will be integrated into the application:

- Class Routine & Exam Schedule
- Expense Tracker
- Study Planner

---

## Developed For

Python Programming Midterm Project
American International University-Bangladesh (AIUB)

## Student Profile & Academic Records — Developed By

Alim Al Razi Shatak (23-51897-2)
