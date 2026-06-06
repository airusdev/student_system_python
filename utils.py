import db_access
from datetime import datetime
import uuid
import re

# --- GROUP 1: VALIDATORS ---
# All validators starts with validate_
def validate_string_input(message: str) -> str:
    """Takes in a message input and checks if it's a valid string"""
    
    while True:
        string = input(message)
        string_to_compare = string.replace(" ", "")
        
        if not string_to_compare.isalpha():
            print("The given string must not contain other characters except letters.\n")
        else:
            return string
            

def validate_int_input(message: str) -> int:
    """Takes in a message input and checks if it's a valid integer"""

    while True:
        try:
            integer = int(input(message))
            return integer

        except (TypeError, ValueError):
            print("The given input is not a valid integer.\n")


def validate_float_input(message: str) -> float:
    """Takes in a message input and checks if it's a valid float"""
    
    while True:
        try:
            valid_float = float(input(message)) 
            return valid_float
        
        except (ValueError, TypeError):
            print("Given input is not a valid float.\n")
       

def validate_menu_input(string_input: str) -> int:
    """Validates the user's choice in the main menu and returns it"""
    
    try:
        string_input = int(string_input)  
        if not (1 <= string_input <= 7):
            print("The inputted integer must be within 1 and 7")
            return 
        else:
            return string_input

    except ValueError:
        print("The given choice is not an integer.")
        return


def validate_gpa_input(message: str) -> float:
    """Takes in a message for the input() and checks if the input is a valid GPA""" 
    
    valid_gpa = False
    
    while not valid_gpa:
        gpa = validate_float_input(message) 
        
        if (1 <= gpa <= 4):
            valid_gpa = True
            return gpa
        else:
            print("The given GPA is not within 1 and 4.\n")


def validate_course_input(message: str) -> str:
    """Validates the inputted course in student information"""
    
    # print valid courses and guide user
    valid_courses = {'BSCS - Bachelor of Science in Computer Science',
                     'DMD - Doctor of Dental Medicine',
                    'BSIT - Bachelor of Science in Information Technology',
                    'BSN - Bachelor of Science in Nursing',
                    'BSA - Bachelor of Science in Accountancy',
                    'BSME - Bachelor of Science in Mechanical Engineering',
                    'BSEE - Bachelor of Sciencee in Electrical Engineering',
                    }
    
    print("\nPlease input the abbreviation.\nFor example, put in 'BSCS' if you want to pursue Computer Science.\n")
    for course in valid_courses:
        print(course)
    
    found = False 
    while not found:
        input_course = validate_string_input("\n" + message)
        
        for course in valid_courses:
            if input_course.upper() in course:
                found = True
                return course                

        if not found:
            print("Please input the correct abbreviation for your course.")

def validate_age_input(message: str) -> int:
    """Validates if the student's age is within 15 and 60."""
    while True:
        integer = validate_int_input(message)
        
        if (15 <= integer <= 60):
            valid_age = True
            return integer
        else:
            print("The inputted age must be within 15 and 60.\n") 
    
    
    valid_age = False
    
    while not valid_age:
        integer = validate_int_input(message)
        
        if 15 <= integer <= 60:
            valid_age = True
            return integer
        else:
            print("The inputted age must be within 15 and 60.\n")    




# --- GROUP 2: STRING FORMATTING ---
def title_case(message: str) -> str:
    """Formats the inputted string to Title Case""" 
    
    string = validate_string_input(message).split(" ")
    new_string = ""
    
    for i in range(0, len(string)):
        new_string = string[i][0].upper() + string[i][1:].lower()
        string[i] = new_string
        
    return " ".join(string)


# --- GROUP 3: MAIN MENU ---
# functions related to the main menu

def acquire_student_information() -> dict:
    """Acquire the student's information that's about to be added."""
    
    student_information = {
        "first_name": title_case("Input the student's first name: "),
        "middle_name": title_case("Input the student's middle name: "),
        "last_name": title_case("Input the student's last name: "),
        "age": validate_age_input("How old is the student? "),
        "course": validate_course_input("In what course does the student belong to? "),
        "gpa": validate_gpa_input("Lastly, input the student's GPA: ")
    }
    
    print("\nInformation:")
    for access, info in student_information.items():
        print(f"{access}: {info}")
    
    return student_information


def add_student() -> None:
    """Calls up db_access to add information to the database""" 
    student_information = acquire_student_information()
    db_access.student_to_database(student_information)
    
    return "Added Student"


def update_student():
    db_access.update_student_in_database()
    return "Updated Student"

def delete_student():
    db_access.delete_student()
    return "Delete Student"

def search_student():
    return "Search Student"

def list_all_students():
    db_access.list_all_students()
    return "List All Students"

def sort_students():
    return "Sort Students"

def exit_():
    print("System Exit.")
    return None

def pick_option(option: int):
    """Returns the corresponding valid function according to the choice the user picked"""

    try:
        main_menu_options = {
            1: add_student,
            2: update_student,
            3: delete_student,
            4: search_student,
            5: list_all_students,
            6: sort_students,
            7: exit_
        }

        return main_menu_options[option]()

    except KeyError:
        return "The choice picked is not within 1 and 7."


def main_menu() -> str:
    """Prints the main menu and takes in the user's choice"""

    print("\nStudent Record System")
    print("─────────────────────", end="\n")
    print("[1] Add Student")
    print("[2] Update Student")
    print("[3] Delete Student")
    print("[4] Search Student")
    print("[5] List All Students")
    print("[6] Sort Students")
    print("[7] Exit", end="\n")

    user_choice = input("\nChoice: ")
    validated_choice = validate_menu_input(user_choice) 
    
    return validated_choice

