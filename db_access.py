import json
import uuid
import utils

students = {}
db_file = "./database.json"


# DATABASE OPERATIONS
def load_db():
    """Loads the database""" 
    with open(db_file, "r") as f:
        return json.load(f)

students = load_db()

def save_db(data):
    """Overwrites the database"""
    with open(db_file, "w") as f:
        json.dump(data, f, indent=4)


# STUDENT SYSTEM OPERATIONS
def list_all_students() -> str:
    """Lists all students in order of highest GPA to lowest"""
    student_list = []
    
     
    
    
    return

def create_student_id() -> int:
    return


def student_to_database(student_information: dict, student_uuid: str) -> None:
    """Pushes the recently added student to the database"""
    student_id = create_student_id()
    students[student_uuid] = student_information
    save_db(students) 

