import json
import uuid
import utils
from datetime import datetime
import time
import re

db_file = "./database.json"
current_year = 2026


# DATABASE OPERATIONS
def load_db():
    """Loads the database""" 
    with open(db_file, "r") as f:
        return json.load(f)

def save_db(data):
    """Overwrites the database"""
    with open(db_file, "w") as f:
        json.dump(data, f, indent=4)


## UPDATE STUDENT COUNTER
def update_student_counter() -> None:
    global current_year 
    
    if datetime.now().year > current_year:
        current_year = datetime.now().year
        student_counter = 0

students = load_db()
student_counter = len(students)
update_student_counter()


# STUDENT SYSTEM OPERATIONS
## GENERAL VALIDATORS
def validate_student_id(message: str) -> str:
    """Validates if the student ID is in a valid format and if it exists in the database."""
    student_id_format = rf"^{datetime.now().year}S[1-9]\d*$"
    
    while True:
        given_id = input(message)

        if not re.fullmatch(student_id_format, given_id):
            print("This student ID is not in a valid format.\n")
        elif students.get(given_id) == None:
            print("This student ID does not exist in the database.\n")
        else:
            return given_id



## PRINT STUDENTS
def list_all_students() -> str | None:
    # add proper formatting for listing all of the students
    # Student List
    # ------------
    # something like that
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


## DELETE STUDENT
def delete_student(student_id):
    """Delete a student in the database using a student id"""
    return


## UPDATE STUDENT
def validate_update_student_choice(message: str) -> int | False:
    """Validates the update student choice, ensuring it's within 1 and 4."""
    while True:
        student_choice = utils.validate_int_input(message)

        if not (1 <= student_choice <= 5):
            print("Given student choice is not within 1 and 4.\n")
            return False
        else:
            return student_choice

def acquire_updated_name() -> dict[str, str]:
    """Acquires the student's updated name"""
    print("Please input the updated name.\n") 
    
    updated_name = {
        "first_name": utils.title_case("Updated First Name: "),
        "middle_name": utils.title_case("Updated Middle Name: "),
        "last_name": utils.title_case("Updated Last Name: ")
    } 

    return updated_name

def acquire_updated_age() -> dict[str, int]:
    """Acquires the student's updated age"""
    print("Please input the updated age.\n")

    updated_age = {
        "age": utils.validate_age_input("Updated Age: ")
    }

    return updated_age


def acquire_updated_course() -> dict[str, str]:
    """Acquires the student's updated course"""
    updated_course = {
        "course": utils.validate_course_input("Updated Course: ")
    } 
    
    return updated_course


def acquire_updated_gpa() -> dict[str, float]:
    """Acquires the student's updated GPA"""
    print("Please input the updated GPA.\n")
    
    updated_gpa = {
        "gpa": utils.validate_gpa_input("Updated GPA: ")
    } 
    
    return updated_gpa
    
    
def acquire_updated_all() -> dict[str, int | float | str]:
    """Acquires the updated information on all aspects for the student"""
    print("Please input the updated information:\n")
    
    updated_information = {
        "first_name": utils.title_case("Updated First Name: "),
        "middle_name": utils.title_case("Updated Middle Name: "),
        "last_name": utils.title_case("Updated Last Name: "),
        "age": utils.validate_age_input("Updated Age: "),
        "course": utils.validate_course_input("Updated Course: "),
        "gpa": utils.validate_gpa_input("Updated GPA: ")
    }
    
    return updated_information

def update_student_choice() -> dict:
    """Serves as the control center on what will be picked to update"""
    
    print("What information of student would you like to update?")
    student_choice = validate_update_student_choice("Options:\n (1) Name\n (2) Age\n (3) Course\n (4) GPA\n (5) ALL\n\nChoose: ")

    update_student = {
        1: acquire_updated_name,
        2: acquire_updated_age,
        3: acquire_updated_course,
        4: acquire_updated_gpa,
        5: acquire_updated_all
    }

    return update_student[student_choice]()
    

def update_student_in_database() -> None:
    """Using the student ID, the system updates the student's information"""
    student_id = validate_student_id("Input the student ID you wish to update: ") 
    updated_student_information = update_student_choice()

    for identification, updated_info in updated_student_information.items():
        students[student_id][identification] = updated_info

    save_db(students)

## ADD STUDENT
def create_student_id() -> int:
    """Creates the student's unique identifier"""
    global student_counter

    student_counter += 1
    student_id = f"{current_year}S{student_counter}"    
    
    print(f"Student ID: {student_id}")
    print("Please make sure to store the student_id in a safe location.\nThis will be used as the student's form of identification.\n")
    
    return student_id


def student_to_database(student_information: dict) -> None:
    """Pushes the recently added student to the database"""
    student_id = create_student_id()
    students[student_id] = student_information
    save_db(students)
