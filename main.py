# Student Assistant System
# Study Planner & To-Do List


import json
import os


STATUS = ("Pending", "Completed")


# Task Class
# Encapsulation

class Task:

    def __init__(self, subject, title, deadline):

        self.subject = subject
        self.title = title
        self.deadline = deadline
        self.status = "Pending"


    def complete(self):

        self.status = "Completed"


    def to_dictionary(self):

        return {
            "subject": self.subject,
            "title": self.title,
            "deadline": self.deadline,
            "status": self.status
        }



# Student Assistant Class

class StudentAssistant:


    def __init__(self, username):

        self.username = username
        self.filename = "tasks.json"
        self.tasks = []

        self.load_tasks()



    def system_role(self):

        print("Student Assistant System")



    # Load Tasks

    def load_tasks(self):

        try:

            if os.path.exists(self.filename):

                with open(self.filename, "r") as file:

                    data = json.load(file)


                    for item in data:

                        task = Task(
                            item["subject"],
                            item["title"],
                            item["deadline"]
                        )

                        task.status = item["status"]

                        self.tasks.append(task)


        except json.JSONDecodeError:

            self.tasks = []

            print("Invalid File Format")


        except Exception as e:

            print("Error:", e)



    # Save Tasks

    def save_tasks(self):

        try:

            data = []

            for task in self.tasks:

                data.append(task.to_dictionary())


            with open(self.filename, "w") as file:

                json.dump(data, file, indent=4)


        except Exception as e:

            print("Error:", e)




    # Add Task

    def add_task(self):

        print("\n----- Add Task -----")


        subject = input("Subject: ")

        title = input("Task: ")

        deadline = input("Deadline (DD-MM-YYYY): ")


        task = Task(
            subject,
            title,
            deadline
        )


        self.tasks.append(task)

        self.save_tasks()


        print("Task Added Successfully!")




    # View Tasks

    def view_tasks(self):

        print("\n========== TASK LIST ==========")


        if len(self.tasks) == 0:

            print("No Tasks Available")

            return


        subjects = set()


        for i, task in enumerate(self.tasks, start=1):

            subjects.add(task.subject)


            print(
f"""
Task Number : {i}
---------------------
Subject     : {task.subject}
Task        : {task.title}
Deadline    : {task.deadline}
Status      : {task.status}
"""
            )


        print("Unique Subjects:")

        print(subjects)




    # Complete Task

    def complete_task(self):

        self.view_tasks()


        try:

            number = int(input("\nEnter Task Number: "))


            if 1 <= number <= len(self.tasks):

                task = self.tasks[number - 1]


                if task.status == "Completed":

                    print("Task already completed!")


                else:

                    task.complete()

                    self.save_tasks()

                    print("Task Completed Successfully!")


            else:

                print("Invalid Task Number")


        except ValueError:

            print("Enter numbers only")





    # Delete Task

    def delete_task(self):

        self.view_tasks()


        try:

            number = int(input("\nEnter Task Number: "))


            if 1 <= number <= len(self.tasks):

                removed = self.tasks.pop(number - 1)

                self.save_tasks()


                print(
                    removed.title,
                    "Deleted Successfully"
                )


            else:

                print("Invalid Task Number")


        except ValueError:

            print("Enter numbers only")





    # Search Task

    def search_task(self):

        keyword = input("Search Subject: ").lower()


        found = False


        for task in self.tasks:


            if keyword in task.subject.lower():

                found = True


                print(
f"""
Subject : {task.subject}
Task    : {task.title}
Deadline: {task.deadline}
Status  : {task.status}
"""
                )


        if not found:

            print("No Task Found")





    # Progress Report

    def progress_report(self):

        total = len(self.tasks)

        completed = 0


        for task in self.tasks:

            if task.status == "Completed":

                completed += 1


        pending = total - completed


        rate = 0


        if total > 0:

            rate = (completed / total) * 100


        print(
f"""
========== PROGRESS ==========

Total Tasks : {total}

Completed   : {completed}

Pending     : {pending}

Completion Rate: {rate:.2f}%

"""
        )






# Main Program


student = StudentAssistant("Student")


while True:


    print("""
================================
 STUDENT ASSISTANT SYSTEM
 STUDY PLANNER & TO-DO LIST
================================

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Search Task
6. Progress Report
7. Exit

""")


    try:

        choice = int(input("Enter Choice: "))


        if choice == 1:

            student.add_task()


        elif choice == 2:

            student.view_tasks()


        elif choice == 3:

            student.complete_task()


        elif choice == 4:

            student.delete_task()


        elif choice == 5:

            student.search_task()


        elif choice == 6:

            student.progress_report()


        elif choice == 7:

            print("\nThank You For Using Student Assistant System")

            break


        else:

            print("Invalid Choice")



    except ValueError:

        print("Please enter numbers only")


    except Exception as e:

        print("Error:", e)