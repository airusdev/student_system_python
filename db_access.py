import json
import uuid
import utils
from datetime import datetime
import time

db_file = "./database.json"
current_year = 2026


# UPDATE STUDENT COUNTER
def update_student_counter() -> None:
    global current_year 
    
    if datetime.now().year > current_year:
        current_year = datetime.now().year
        student_counter = 0

update_student_counter()



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


def list_all_students() -> str:
    """Lists all students in order of how they were added"""

    if student_counter == 0:
        print("There are no added students yet!")
        return


    for identification, information in students.items():
        first_name = information["first_name"]
        middle_name = information["middle_name"]
        last_name = information["last_name"]
        age = information["age"]
        course = information["course"]
        gpa = information["gpa"]

        student = f"Full Name: {first_name} {middle_name[0]}. {last_name}\nAge: {age}\nCourse: {course}\nGPA: {gpa}"
        print(student)


# UPDATE STUDENT
def update_name() -> str:
    return

def update_age() -> int:
    return

def update_course() -> str:
    return

def update_gpa() -> float:
    return

def update_student_choice(choice)

def update_student_in_database(student_id: int) -> None: # we can use utils.validate_student_id
    """Using the student ID, the system updates the student's information"""
    print("What information of student would you like to update?")
    print(" (1) Name\n (2) Age\n (3) Course\n (4) GPA")



## ADD STUDENT
def create_student_id() -> int:
    """Creates the student's unique identifier"""
    global student_counter

    student_id = f"{current_year}S{student_counter}"    
    student_counter += 1
    
    print(f"Student ID: {student_id}")
    print("Please make sure to store the student_id in a safe location.\nThis will be used as the student's form of identification.\n")
    
    return student_id


def student_to_database(student_information: dict) -> None:
    """Pushes the recently added student to the database"""
    student_id = create_student_id()
    students[student_id] = student_information
    save_db(students)
