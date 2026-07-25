"""
Module 2: Class Routine & Exam Planner
Student Assistant System - Mid-term Group Project

This module is self-contained and can be "plugged in" to the central
menu system. Just import this file and call run_module() from the
main interface.

Data storage: CSV files (no database used, per project rules)
    - routine.csv : Day, Time, Subject, Room
    - exams.csv   : Subject, Date, Time, Room

Author: (your name here)
Branch: feature/routine-planner
"""

import csv
import os
from datetime import datetime

# ---------------------------------------------------------------------
# File paths (kept in the same folder as this script)
# ---------------------------------------------------------------------
ROUTINE_FILE = "data/routine.csv"
EXAM_FILE = "data/exams.csv"

ROUTINE_FIELDS = ["Day", "Time", "Subject", "Room"]
EXAM_FIELDS = ["Subject", "Date", "Time", "Room"]

VALID_DAYS = ["Saturday", "Sunday", "Monday", "Tuesday",
              "Wednesday", "Thursday", "Friday"]


# ---------------------------------------------------------------------
# Helper functions for CSV handling
# ---------------------------------------------------------------------
def init_file(filename, fields):
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(fields)

def read_csv(filename):
    """Return all rows of a CSV file as a list of dicts."""
    init_file(filename, ROUTINE_FIELDS if filename == ROUTINE_FILE else EXAM_FIELDS)
    with open(filename, "r", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(filename, fields, rows):
    """Overwrite the CSV file with the given rows (used for edit/delete)."""
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def append_row(filename, fields, row):
    """Add a single new row to the CSV file."""
    init_file(filename, fields)
    with open(filename, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writerow(row)


# ---------------------------------------------------------------------
# Input validation helpers
# ---------------------------------------------------------------------
def get_valid_day():
    while True:
        day = input(f"Day ({'/'.join(VALID_DAYS)}): ").strip().title()
        if day in VALID_DAYS:
            return day
        print("Invalid day. Please try again.")


def get_valid_time():
    while True:
        time_str = input("Time (e.g. 09:00 AM): ").strip()
        try:
            datetime.strptime(time_str, "%I:%M %p")
            return time_str
        except ValueError:
            print("Invalid format. Use HH:MM AM/PM, e.g. 02:30 PM")


def get_valid_date():
    while True:
        date_str = input("Date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD, e.g. 2026-08-15")


# ---------------------------------------------------------------------
# CLASS ROUTINE FEATURES
# ---------------------------------------------------------------------
def add_routine_entry():
    print("\n--- Add Class Routine Entry ---")
    day = get_valid_day()
    time_str = get_valid_time()
    subject = input("Subject name: ").strip()
    room = input("Room number: ").strip()

    row = {"Day": day, "Time": time_str, "Subject": subject, "Room": room}
    append_row(ROUTINE_FILE, ROUTINE_FIELDS, row)
    print("Class added to routine successfully!\n")


def view_routine():
    print("\n--- Class Routine ---")
    rows = read_csv(ROUTINE_FILE)
    if not rows:
        print("No classes added yet.\n")
        return

    choice = input("View (A)ll or a specific (D)ay? [A/D]: ").strip().upper()
    if choice == "D":
        day = get_valid_day()
        rows = [r for r in rows if r["Day"] == day]
        if not rows:
            print(f"No classes scheduled on {day}.\n")
            return

    # Sort by day order, then time
    day_order = {d: i for i, d in enumerate(VALID_DAYS)}
    rows.sort(key=lambda r: (day_order.get(r["Day"], 99), r["Time"]))

    print(f"\n{'Day':<10}{'Time':<12}{'Subject':<20}{'Room':<10}")
    print("-" * 52)
    for r in rows:
        print(f"{r['Day']:<10}{r['Time']:<12}{r['Subject']:<20}{r['Room']:<10}")
    print()


def delete_routine_entry():
    print("\n--- Delete a Routine Entry ---")
    rows = read_csv(ROUTINE_FILE)
    if not rows:
        print("No classes to delete.\n")
        return

    for i, r in enumerate(rows, 1):
        print(f"{i}. {r['Day']} | {r['Time']} | {r['Subject']} | Room {r['Room']}")

    try:
        num = int(input("Enter number to delete (0 to cancel): "))
        if num == 0:
            return
        if 1 <= num <= len(rows):
            removed = rows.pop(num - 1)
            write_csv(ROUTINE_FILE, ROUTINE_FIELDS, rows)
            print(f"Removed: {removed['Subject']} on {removed['Day']}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


# ---------------------------------------------------------------------
# EXAM PLANNER FEATURES
# ---------------------------------------------------------------------
def add_exam():
    print("\n--- Add Exam ---")
    subject = input("Subject name: ").strip()
    date_str = get_valid_date()
    time_str = get_valid_time()
    room = input("Room number: ").strip()

    row = {"Subject": subject, "Date": date_str, "Time": time_str, "Room": room}
    append_row(EXAM_FILE, EXAM_FIELDS, row)
    print("Exam added successfully!\n")


def view_exams():
    print("\n--- Upcoming Exams ---")
    rows = read_csv(EXAM_FILE)
    if not rows:
        print("No exams scheduled yet.\n")
        return

    today = datetime.now().date()
    # Sort by date
    rows.sort(key=lambda r: r["Date"])

    print(f"\n{'Subject':<20}{'Date':<12}{'Time':<12}{'Room':<8}{'Days Left':<10}")
    print("-" * 62)
    for r in rows:
        exam_date = datetime.strptime(r["Date"], "%Y-%m-%d").date()
        days_left = (exam_date - today).days
        status = f"{days_left}" if days_left >= 0 else "Passed"
        print(f"{r['Subject']:<20}{r['Date']:<12}{r['Time']:<12}{r['Room']:<8}{status:<10}")
    print()


def delete_exam():
    print("\n--- Delete an Exam ---")
    rows = read_csv(EXAM_FILE)
    if not rows:
        print("No exams to delete.\n")
        return

    for i, r in enumerate(rows, 1):
        print(f"{i}. {r['Subject']} | {r['Date']} | {r['Time']} | Room {r['Room']}")

    try:
        num = int(input("Enter number to delete (0 to cancel): "))
        if num == 0:
            return
        if 1 <= num <= len(rows):
            removed = rows.pop(num - 1)
            write_csv(EXAM_FILE, EXAM_FIELDS, rows)
            print(f"Removed exam: {removed['Subject']}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


# ---------------------------------------------------------------------
# MODULE MENU (this is the "plug-in point" for the central menu)
# ---------------------------------------------------------------------
def run_module():
    """
    Entry point called by the main application's central menu.
    Example from main.py:
        import routine_planner
        routine_planner.run_module()
    """
    init_file(ROUTINE_FILE, ROUTINE_FIELDS)
    init_file(EXAM_FILE, EXAM_FIELDS)

    while True:
        print("=" * 40)
        print(" CLASS ROUTINE & EXAM PLANNER")
        print("=" * 40)
        print("1. Add Class to Routine")
        print("2. View Class Routine")
        print("3. Delete a Class")
        print("4. Add Exam")
        print("5. View Upcoming Exams")
        print("6. Delete an Exam")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_routine_entry()
        elif choice == "2":
            view_routine()
        elif choice == "3":
            delete_routine_entry()
        elif choice == "4":
            add_exam()
        elif choice == "5":
            view_exams()
        elif choice == "6":
            delete_exam()
        elif choice == "0":
            print("Returning to main menu...\n")
            break
        else:
            print("Invalid choice. Try again.\n")


# ---------------------------------------------------------------------
# Allows standalone testing: run this file directly to test the module
# without needing the rest of the group's project.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    run_module()