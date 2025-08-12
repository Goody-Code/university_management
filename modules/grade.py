from utils.helpers import load_data, save_data, GRADES_FILE
from modules.student import view_students, find_student_by_id
from modules.course import view_courses, find_course_by_code

def record_grade():
    """Records a grade for a student in a specific course."""
    grades = load_data(GRADES_FILE)
    
    view_students()
    student_id = input("Enter the ID of the student to record a grade for: ")
    if not find_student_by_id(student_id):
        print("Error: Student not found.")
        return
        
    view_courses()
    course_code = input("Enter the course code: ")
    if not find_course_by_code(course_code):
        print("Error: Course not found.")
        return
        
    grade = input("Enter the grade (e.g., 95, A+): ")
    
    grades.append({
        'student_id': student_id,
        'course_code': course_code,
        'grade': grade
    })
    
    save_data(GRADES_FILE, grades)
    print("Grade recorded successfully!")

def view_student_grades():
    """Displays the grades of a specific student."""
    grades = load_data(GRADES_FILE)
    
    view_students()
    student_id = input("Enter the student ID to view grades: ")
    
    student = find_student_by_id(student_id)
    if not student:
        print("Error: Student not found.")
        return

    student_grades = [g for g in grades if g['student_id'] == student_id]
    
    if not student_grades:
        print(f"No grades recorded for student {student['name']}.")
        return

    print(f"\n--- Grades for Student: {student['name']} ({student['id']}) ---")
    for g in student_grades:
        course = find_course_by_code(g['course_code'])
        course_name = course['name'] if course else "Unknown Course"
        print(f"Course: {course_name} ({g['course_code']}), Grade: {g['grade']}")
    print("----------------------------------------------------\n")
