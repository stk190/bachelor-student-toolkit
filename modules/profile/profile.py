from modules.profile.manager import register_student
from modules.profile.manager import view_student

def profile_menu():
    while True:

        print("1. Register Student")
        print("2. View Student Profile")
        print("3. Back")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            register_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

        print ("Feature coming soon...")