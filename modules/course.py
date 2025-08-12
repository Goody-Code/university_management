from utils.helpers import load_data, save_data, COURSES_FILE
from modules.teacher import view_teachers

def add_course():
    """Adds a new course."""
    courses = load_data(COURSES_FILE)
    
    course_code = input("Enter course code (e.g., CS101): ")
    # Check if course code is already in use
    for c in courses:
        if c['code'] == course_code:
            print("Error: This course code already exists.")
            return
            
    name = input("Enter course name: ")
    
    print("Select a teacher for the course from the following list:")
    view_teachers()
    teacher_id = input("Enter teacher's employee ID: ")
    
    # Validation to ensure the teacher exists could be added here
    
    courses.append({
        'code': course_code,
        'name': name,
        'teacher_id': teacher_id
    })
    
    save_data(COURSES_FILE, courses)
    print(f"Course '{name}' added successfully!")

def view_courses():
    """Displays a list of all courses."""
    courses = load_data(COURSES_FILE)
    if not courses:
        print("No courses registered yet.")
        return
        
    print("\n--- Course List ---")
    for c in courses:
        print(f"Code: {c['code']}, Name: {c['name']}, Teacher ID: {c['teacher_id']}")
    print("-------------------\n")

def find_course_by_code(course_code):
    """Finds a course by its code."""
    courses = load_data(COURSES_FILE)
    for c in courses:
        if c['code'] == course_code:
            return c
    return None
