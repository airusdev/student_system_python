# Student System in Python
## TODAY'S GOALS (June 7, 2026)
    1. fix validation of validate_course_input()
    2. finish search_student()


error in validate_course_input() -> put in "BS" and it gets accepted. it assumed the first matching 'BS' abbreviation





## STUDENT SYSTEM
1. input validation
    <!-- 1.1 input validation of string to int
    1.2 input validation of string to float
    1.3 input validation of string (must be strictly string)
    1.4 general validation
        1.4.1 input musn't be all spaces
        1.4.2 input musnt't be empty -->
    1.5 validation for student_info
        1.5.1 check if the inputted name is a valid name
        1.5.2 check if inputted course is part of the course of the "school"
        1.5.3 check if the gpa is a valid gpa

2. finalize data structure to use (dictionary). idea:
    {
        student_uuid_1: {
            "student_name": string,
            "student_age": integer
            "student_course": string,
            "student_gpa": float
        },
    }


3. add_student function
    3.1 generate uuid
    3.2 input name
    3.3 input age
    3.4 input course
    3.5 input gpa


4. update_student function
    4.1 be able to pick an option on what to update: name, age, course, gpa
    4.2 option to also update all
    4.3 input student_id to check




## DATABASE
