from utils.helpers import load_data, save_data, STUDENTS_FILE

def add_student():
    """Adds a new student."""
    students = load_data(STUDENTS_FILE)
    
    student_id = input("Enter student ID: ")
    # Check if student ID is already in use
    for s in students:
        if s['id'] == student_id:
            print("Error: This student ID already exists.")
            return

    name = input("Enter student's full name: ")
    major = input("Enter student's major: ")
    
    students.append({
        'id': student_id,
        'name': name,
        'major': major
    })
    
    save_data(STUDENTS_FILE, students)
    print(f"Student '{name}' added successfully!")

def view_students():
    """Displays a list of all students."""
    students = load_data(STUDENTS_FILE)
    if not students:
        print("No students registered yet.")
        return
        
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Major: {s['major']}")
    print("--------------------\n")

def find_student_by_id(student_id):
    """Finds a student by their ID."""
    students = load_data(STUDENTS_FILE)
    for s in students:
        if s['id'] == student_id:
            return s
    return None
