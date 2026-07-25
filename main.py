from modules.profile.profile import profile_menu
from utils.input_utils import user_input

def main():
    while True:
        
        print ("\n===== Bachelor Student Toolkit =====")
        print ("    1. Profile")
        print ("    2. Class  & Exam Schedule")
        print ("    3. Expense Tracker")
        print ("    4. Study Planner")
        print ("    5. Exit")
        print ("====================================\n")

        choice = user_input("\n Enter your choice (1-5): ")
    
        if choice == '1':
            profile_menu()
        elif choice == '2':
            print("under development!!!")
        elif choice == '3':
            print("under development!!!")
        elif choice == '4':
            print("under development!!!")
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("\n Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  