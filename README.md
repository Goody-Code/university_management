---

# University Management System (CLI) ☕

A simple, command-line based (CLI) system for managing students, teachers, courses, and grades in a university. Built with Python and uses JSON files for data storage. It's designed to be lightweight, easy to use, and run in any standard terminal, including Termux on Android.

## ✨ Features

*   **Manage Students**: Add new students and view a list of all registered students.
*   **Manage Teachers**: Add new teachers and view a list of all staff.
*   **Manage Courses**: Add new courses and assign teachers to them.
*   **Manage Grades**: Record student grades for different courses and view a student's complete academic record.
*   **Interactive CLI**: An easy-to-use menu-driven interface for smooth navigation.
*   **Persistent Storage**: All data is saved locally in organized `JSON` files.

## 📂 Project File Structure

The project is organized with a clean structure to separate concerns, making it easier to understand and maintain.

```
university_management/
│
├── data/
│   ├── students.json
│   ├── teachers.json
│   ├── courses.json
│   └── grades.json
│
├── modules/
│   ├── __init__.py
│   ├── student.py
│   ├── teacher.py
│   ├── course.py
│   └── grade.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
└── main.py
```

*   **`university_management/`**: The main project directory.
*   **`data/`**: Contains `JSON` files for data storage. This acts as a simple, file-based database.
    *   `students.json`: Stores student records.
    *   `teachers.json`: Stores teacher records.
    *   `courses.json`: Stores course details.
    *   `grades.json`: Stores student grades.
*   **`modules/`**: Contains the core logic for each entity in the system.
    *   `student.py`: Manages all student-related operations.
    *   `teacher.py`: Manages all teacher-related operations.
    *   `course.py`: Manages all course-related operations.
    *   `grade.py`: Manages all grade-related operations.
*   **`utils/`**: Contains helper functions used across different modules.
    *   `helpers.py`: Includes functions for loading/saving `JSON` data and clearing the screen.
*   **`main.py`**: The entry point of the application. It contains the main menu and handles user interaction.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have **Python** installed on your system. If not, you can install it on a Debian-based system (like Ubuntu or Termux) with the following command:

```bash
# Update and upgrade packages
sudo apt update && sudo apt upgrade -y

# Install Python
sudo apt install python -y
```
For Termux users:
```bash
pkg update && pkg upgrade
pkg install python
```

### Installation & Setup

1.  **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/Goody-Code/university_management.git
    cd university_management


2.  The repository already contains the complete file structure and code. The `data` directory with its `.json` files is included.

## ▶️ How to Run the Project

Once you are inside the project's root directory (`university_management`), run the following command in your terminal:

```bash
python main.py
```

This command will start the application, and you will be greeted with the main interactive menu. From there, you can navigate through the different management options. All data you enter will be automatically saved in the `data/` folder.
