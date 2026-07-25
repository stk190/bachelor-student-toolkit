import csv
import os
from datetime import datetime

CSV_FILE = "data/expenses.csv"


def init_csv():
    """Ensures expenses.csv exists with headers."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    """Adds a new expense row to the CSV."""
    init_csv()
    print("\n--- Add Expense ---")

    # Date defaults to today if left blank
    date_input = input("Date (YYYY-MM-DD) [Press Enter for Today]: ").strip()
    if not date_input:
        date_input = datetime.now().strftime("%Y-%m-%d")

    category = input("Category (e.g., Food, Transport, Books): ").strip()

    # Simple input validation for amount
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("❌ Invalid amount. Expense not saved.")
        return

    description = input("Description: ").strip()

    # Append to CSV
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date_input, category, f"{amount:.2f}", description])

    print("✅ Expense saved successfully!")


def view_expenses():
    """Displays all expenses in a clean table format."""
    init_csv()
    print("\n--- All Expenses ---")

    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses recorded yet.")
        return

    # Header and divider
    print(f"{'Date':<12} | {'Category':<12} | {'Amount':<10} | {'Description'}")
    print("-" * 55)

    # Data rows
    for row in rows[1:]:
        print(f"{row[0]:<12} | {row[1]:<12} | ${row[2]:<9} | {row[3]}")


def view_total():
    """Calculates total money spent."""
    init_csv()
    total = 0.0

    with open(CSV_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])

    print(f"\n💵 Total Spent: ${total:.2f}")


def expense_tracker_menu():
    """Main function for this module (called by main application)."""
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Back to Main Menu")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")


# Allows you to test this module individually by running: python expense_tracker.py
if __name__ == "__main__":
    expense_tracker_menu()
