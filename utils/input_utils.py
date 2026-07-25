import sys

def user_input(prompt):
    try:
        value = input(prompt).strip()
    except KeyboardInterrupt:
        print("\nProgram stopped.")
        sys.exit()

    if value.lower() in ("exit", "0"):
        print("\nThank you for using Bachelor Student Toolkit.\n")
        sys.exit()

    return value