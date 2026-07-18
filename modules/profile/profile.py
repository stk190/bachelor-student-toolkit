from modules.profile.manager import delete_student, register_student, view_all_students
from modules.profile.manager import view_student
from modules.profile.manager import update_student
from modules.profile.manager import delete_student

def profile_menu():
    while True:

        print("1. Register Student")
        print("2. View Student Profile")
        print("3. Update Student Profile")
        print("4. Delete Student Profile")
        print("5. View All Students (restricted)")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            register_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            passkey = input("Enter admin passkey: ")
            view_all_students(passkey)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

       