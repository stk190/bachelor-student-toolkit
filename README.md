# Bachelor Student Toolkit

Bachelor Student Toolkit is a Python command-line application developed as a midterm group project. The project is divided into four modules, where each team member is responsible for developing one module.

Current Module Status:
- Student Profile & Academic Records (Completed)
- Class Routine & Exam Schedule (In Progress)
- Expense Tracker (In Progress)
- Study Planner (In Progress)

---

## Student Profile & Academic Records

This module manages student information and academic records. All data is stored using CSV files.

### Features

#### Student Management

- Register Student
- View Student Profile
- Update Student Profile
- Delete Student Profile
- View All Students (Admin Protected)

#### Academic Records

- Add Semester Courses
- View Semester Courses
- Calculate Semester GPA
- Calculate Overall CGPA
- View Student Transcript

#### Dashboard

- Total Students
- Total Registered Courses

---

## AIUB Grading System

The application follows the AIUB grading policy.

| Marks | Grade | Grade Point |
|-------|-------|-------------|
| 90 - 100 | A+ | 4.00 |
| 85 - 89 | A | 3.75 |
| 80 - 84 | B+ | 3.50 |
| 75 - 79 | B | 3.25 |
| 70 - 74 | C+ | 3.00 |
| 65 - 69 | C | 2.75 |
| 60 - 64 | D+ | 2.50 |
| 50 - 59 | D | 2.25 |
| Below 50 | F | 0.00 |

The system automatically converts marks into letter grades and grade points.

---

## Input Validation

The module validates:

- Student ID
- Full Name
- University
- Department
- Semester
- Email Address
- Number of Courses
- Course Credit
- Marks

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
│   └── profile/
│       ├── manager.py
│       ├── profile.py
│       ├── storage.py
│       ├── student.py
│       └── course.py
│
├── utils/
│   ├── grading.py
│   ├── validation.py
│   └── config.py
│
├── main.py
└── README.md
```

---

## Technologies Used

- Python 3
- CSV Files
- Object-Oriented Programming (OOP)
- Git
- GitHub

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