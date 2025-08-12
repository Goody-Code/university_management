import time
import sys
from utils.helpers import clear_screen
from modules import student, teacher, course, grade

# التحقق من وجود المكتبات اللازمة للشاشة الاحترافية
try:
    import pyfiglet
    from colorama import init, Fore, Style
    LIBS_INSTALLED = True
except ImportError:
    LIBS_INSTALLED = False

def display_splash_screen():
    """
    يعرض شاشة ترحيبية احترافية بأسلوب "الهاكر" عند بدء تشغيل البرنامج.
    """
    if not LIBS_INSTALLED:
        # شاشة بديلة في حال لم يتم تثبيت المكتبات
        print("===================================================")
        print("   University & Student Management System (CLI)   ")
        print("     Developed by: Abu Al-Jamal & Eng. Aman Al-Quwa    ")
        print("===================================================")
        print("\nHint: For the best experience, run: pip install pyfiglet colorama")
        time.sleep(4)
        return

    # تهيئة Colorama
    init(autoreset=True)
    clear_screen()
    
    # 1. الشعار الرئيسي باستخدام ASCII Art وتأثير الكتابة
    font = pyfiglet.Figlet(font='standard') # خط كلاسيكي وواضح
    title_text = "University\nManagement"
    title_art = font.renderText(title_text)
    
    colors = [Fore.GREEN, Fore.CYAN]
    for i, char in enumerate(title_art):
        color = colors[i % len(colors)]
        sys.stdout.write(color + Style.BRIGHT + char)
        sys.stdout.flush()
        time.sleep(0.002)
        
    # 2. الإطار وأسماء المطورين
    border = "═" * 70
    dev_info = "Developed By: Abu Al-Jamal & Eng. Aman Al-Quwa".center(70)

    print(f"\n{Fore.GREEN + Style.BRIGHT}{border}")
    print(f"{Fore.YELLOW + Style.BRIGHT}{dev_info}")
    print(f"{Fore.GREEN + Style.BRIGHT}{border}\n")

    # 3. تسلسل التحميل ليعطي شعورًا بالاحترافية
    loading_messages = [
        ("Initializing System...", 0.7),
        ("Connecting to data files...", 0.6),
        ("Loading core modules...", 0.8),
        ("All systems operational. Launching...", 1.5)
    ]
    
    for i, (msg, delay) in enumerate(loading_messages):
        progress = f"[{'#' * (i + 1):<4}]" # شريط تقدم بسيط
        print(f"  {Fore.WHITE}{progress} {msg}")
        time.sleep(delay)

    time.sleep(1) # تأخير أخير قبل مسح الشاشة


def main_menu():
    """
    يعرض القائمة الرئيسية للتطبيق.
    """
    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "===================================================")
    print(Fore.WHITE + Style.BRIGHT + "      University & Student Management System")
    print(Fore.CYAN + Style.BRIGHT + "===================================================")
    print(f"\n{Fore.GREEN}1. {Fore.WHITE}Manage Students")
    print(f"{Fore.GREEN}2. {Fore.WHITE}Manage Teachers")
    print(f"{Fore.GREEN}3. {Fore.WHITE}Manage Courses")
    print(f"{Fore.GREEN}4. {Fore.WHITE}Manage Grades")
    print(f"\n{Fore.RED}5. {Fore.WHITE}Exit Program")
    print(Fore.CYAN + "---------------------------------------------------")
    
    choice = input(f"{Fore.YELLOW}Select an option: ")
    return choice

# --- باقي الدوال (student_menu, teacher_menu, etc.) تبقى كما هي بدون تغيير ---
def student_menu():
    """قائمة إدارة الطلاب."""
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
            print(Fore.RED + "Invalid option, please try again.")
        input(f"\n{Fore.YELLOW}Press Enter to continue...")

def teacher_menu():
    """قائمة إدارة المعلمين."""
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
            print(Fore.RED + "Invalid option, please try again.")
        input(f"\n{Fore.YELLOW}Press Enter to continue...")

def course_menu():
    """قائمة إدارة المواد الدراسية."""
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
            print(Fore.RED + "Invalid option, please try again.")
        input(f"\n{Fore.YELLOW}Press Enter to continue...")

def grade_menu():
    """قائمة إدارة الدرجات."""
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
            print(Fore.RED + "Invalid option, please try again.")
        input(f"\n{Fore.YELLOW}Press Enter to continue...")


if __name__ == "__main__":
    # عرض الشاشة الترحيبية الاحترافية أولاً
    display_splash_screen()

    # اللوب الرئيسي للبرنامج
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
            print(Fore.GREEN + "\nThank you for using the system. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice, please select a number from the menu.")
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
