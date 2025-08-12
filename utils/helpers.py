import json
import os

DATA_DIR = 'data'
STUDENTS_FILE = os.path.join(DATA_DIR, 'students.json')
TEACHERS_FILE = os.path.join(DATA_DIR, 'teachers.json')
COURSES_FILE = os.path.join(DATA_DIR, 'courses.json')
GRADES_FILE = os.path.join(DATA_DIR, 'grades.json')

def load_data(file_path):
    """
    Loads data from a JSON file.
    If the file doesn't exist or is empty, returns an empty list.
    """
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_data(file_path, data):
    """
    Saves data to a JSON file.
    Ensures the directory exists first.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def clear_screen():
    """Clears the terminal screen for a better UI experience."""
    os.system('cls' if os.name == 'nt' else 'clear')
