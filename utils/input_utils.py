import sys

def user_input(prompt):
    value = input(prompt).strip()

    if value.lower() in ("exit", "0"):
        print("\nThank you for using Bachelor Student Toolkit.\n")
        sys.exit()

    return value