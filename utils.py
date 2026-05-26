import db_access

# --- GROUP 1: VALIDATORS ---
# All validators starts with validate_
def validated_string_input(message: str) -> str:
    """Takes in a message input and checks if it's a valid string"""
    valid_string = False
    
    while not valid_string:
        try: 
            string = input(message)
            valid_string = True
            return string

        except ValueError or TypeError:
            print("The given input is not a valid string.")
            valid_string = True
            return


def validated_int_input(message: str) -> int:
    """Takes in a message input and checks if it's a valid integer"""
    
    valid_int = False
    
    while not valid_int:
        try:
            integer = int(input(message)) 
            valid_int = True    
            return integer
    
    try:
        valid_int = int(input(message))
        return valid_int

    except ValueError or TypeError:
        print("The given input is not a valid integer.")
        return

def validated_float_input(message: str) -> float:
    """Takes in a message input and checks if it's a valid float"""
    try:
        valid_float = float(input(message))
        return valid_float

    except ValueError or TypeError:
        print("Given input is not a valid ")
        return
        


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

### TO FIX
def validate_course_input(course: str) -> bool:
    """Validates the inputted course in student information"""    

    validated_string = validated_strin

    
    try:
        # need a better way to structure this valid_courses, so that it wont be too repetitive
        valid_courses = {'BSCS',
                        'Bachelor of Science in Computer Science',
                        'BSIT',
                        'Bachelor of Science in Information Technology',
                        'BSN',
                        'Bachelor of Science in Nursing',
                        'BSA',
                        'Bachelor of Science in Accountancy',
                        'BSME',
                        'Bachelor of Science in Mechanical Engineering',
                        'BSEE',
                        'Bachelor of Science in Electrical Engineering'
                        }
        
        if valid_courses[course]:
            return True
        
    except KeyError: 
        print("Inputted course is not within the existing courses.")
        return False


# --- GROUP 2: MAIN MENU ---
# functions related to the main menu

def acquire_student_information() -> dict:
    student_information = {
        "first_name": None,
        "middle_initial": None,
        "last_name": None,
        "age": None,
        "course": None,
        "gpa": None
    }
    
    valid_input = None 
     
    while valid_input == None:

    
    first_name = validated_string_input("Input the student's first name: ")
    middle_name = validated_string_input("Input the student's middle name: ")
    last_name = validated_string_input("Input the student's last name: ")
    age = validated_int_input("How old is the student? ")
    course = validated_string_input("From what course does this student belong to: ")
    gpa = validated_float_input("Lastly, input the student's GPA: ")
    
    print("Name:", first_name, middle_name, last_name)
    print("Age:", age)
    print("Course:", course)
    print("GPA:", gpa)
    

def add_student() -> None:
    """Calls up db_access to add information to the database""" 
    student_information = acquire_student_information()
    student_uuid = 

    # db_access.student_to_database()
    
    return "Add Student"

def update_student():
    return "Update Student"

def delete_student():
    return "Delete Student"

def search_student():
    return "Search Student"

def list_all_students():
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
        return "The choice picked is not within 1 and 7"


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
