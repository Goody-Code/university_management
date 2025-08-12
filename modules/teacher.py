from utils.helpers import load_data, save_data, TEACHERS_FILE

def add_teacher():
    """Adds a new teacher."""
    teachers = load_data(TEACHERS_FILE)
    
    teacher_id = input("Enter teacher's employee ID: ")
    # Check if employee ID is already in use
    for t in teachers:
        if t['id'] == teacher_id:
            print("Error: This employee ID already exists.")
            return

    name = input("Enter teacher's full name: ")
    department = input("Enter teacher's department: ")
    
    teachers.append({
        'id': teacher_id,
        'name': name,
        'department': department
    })
    
    save_data(TEACHERS_FILE, teachers)
    print(f"Teacher '{name}' added successfully!")

def view_teachers():
    """Displays a list of all teachers."""
    teachers = load_data(TEACHERS_FILE)
    if not teachers:
        print("No teachers registered yet.")
        return
        
    print("\n--- Teacher List ---")
    for t in teachers:
        print(f"Employee ID: {t['id']}, Name: {t['name']}, Department: {t['department']}")
    print("--------------------\n")
