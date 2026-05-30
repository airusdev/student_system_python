import json
import uuid
import utils
from datetime import datetime

db_file = "./database.json"

# DATABASE OPERATIONS
def load_db():
    """Loads the database""" 
    with open(db_file, "r") as f:
        return json.load(f)

students = load_db()
student_counter = len(students) - 1

def save_db(data):
    """Overwrites the database"""
    with open(db_file, "w") as f:
        json.dump(data, f, indent=4)



# STUDENT SYSTEM OPERATIONS
def delete_student(student_id):
    """Delete a student in the database using a student id"""
    return


def create_student_id() -> int: ## NUMBER ONE PRIORITY
    """Creates the student's unique identifier"""
    global student_counter
    current_year = datetime.now().year

    student_id = f"{current_year}A{student_counter}"    
    student_counter += 1
    
    return student_id


def validate_student_existence(given_info: dict) -> str: ## NUMBER TWO PRIORITY
    """Identifies if the student already exists in the system"""
    student_exists = False
    
    for student_id, information in students.items():
        if students[student_id] == given_info:
            student_exists = True
    
s
    if student_exists:
        print("This student exists already!") 
    

def list_all_students() -> str:
    """Lists all students in order of highest GPA to lowest"""
    student_list = []
    
    return


# create a validation if a student already exists
def student_to_database(student_information: dict) -> None:
    """Pushes the recently added student to the database"""
    student_in_database = validate_student_existence(student_information)

    student_id = create_student_id()
    students[student_id] = student_information

    
    
    save_db(students) 
    
    print(f"Student ID: {student_id}")

