from utils.helpers import clear_screen
from modules import student, teacher, course, grade

def main_menu():
    """
    Displays the main menu and handles user input.
    """
    clear_screen()
    print("===================================================")
    print("   University & Student Management System (CLI)   ")
    print("===================================================")
    print("\n1. Manage Students")
    print("2. Manage Teachers")
    print("3. Manage Courses")
    print("4. Manage Grades")
    print("5. Exit Program")
    print("---------------------------------------------------")
    
    choice = input("Select an option: ")
    return choice

def student_menu():
    """Student management menu."""
    while True:
        clear_screen()
        print("\n--- Student Management ---")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            student.add_student()
        elif choice == '2':
            student.view_students()
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")
        input("\nPress Enter to continue...")

def teacher_menu():
    """Teacher management menu."""
    while True:
        clear_screen()
        print("\n--- Teacher Management ---")
        print("1. Add New Teacher")
        print("2. View All Teachers")
        print("3. Back to Main Menu")
        choice = input("Choose: ")
        
        if choice == '1':
            teacher.add_teacher()
        elif choice == '2':
            teacher.view_teachers()
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")
        input("\nPress Enter to continue...")

def course_menu():
    """Course management menu."""
    while True:
        clear_screen()
        print("\n--- Course Management ---")
        print("1. Add New Course")
        print("2. View All Courses")
        print("3. Back to Main Menu")
        choice = input("Choose: ")
        
        if choice == '1':
            course.add_course()
        elif choice == '2':
            course.view_courses()
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")
        input("\nPress Enter to continue...")

def grade_menu():
    """Grade management menu."""
    while True:
        clear_screen()
        print("\n--- Grade Management ---")
        print("1. Record a Grade for a Student")
        print("2. View a Student's Grades")
        print("3. Back to Main Menu")
        choice = input("Choose: ")
        
        if choice == '1':
            grade.record_grade()
        elif choice == '2':
            grade.view_student_grades()
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    while True:
        user_choice = main_menu()
        if user_choice == '1':
            student_menu()
        elif user_choice == '2':
            teacher_menu()
        elif user_choice == '3':
            course_menu()
        elif user_choice == '4':
            grade_menu()
        elif user_choice == '5':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice, please select a number from the menu.")
            input("\nPress Enter to continue...")
