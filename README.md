# Student Management System

This is my second **Student Management System** project, created with the goal of improving my proficiency in Python. Through this project, I focused on writing cleaner, more organized code while applying programming concepts such as modularization, file handling, dictionaries, and CRUD (Create, Read, Update, Delete) operations.

This project also serves as the starting point of my journey into **backend development**, where I aim to build a strong foundation in designing applications, managing data, and creating scalable software systems.


# How the Program Works

When the program starts, it enters a continuous system loop. This loop keeps running until the user provides a valid menu option (an integer from **1** to **7**). Invalid inputs are rejected, and the user is prompted again until a valid choice is entered.

Once a valid option is selected, the program calls `pick_option()` from `utils.py`. This function uses a dictionary that maps each menu option (`1`–`7`) to its corresponding function.

Instead of storing function calls (e.g., `add_student()`), the dictionary stores **function references** (e.g., `add_student`). This prevents the functions from executing immediately when the dictionary is created. After retrieving the appropriate function from the dictionary, `pick_option()` calls it by appending `()`.

The functions in `utils.py` are responsible for handling user interaction, but they do not directly manipulate the database. Instead, each function calls its corresponding function in `db_access.py`, which serves as the data access layer. This separation between the user interface and the database logic makes the program easier to maintain and organize.

## Database Management

The application's data is stored in a JSON file. Since JSON files cannot be modified directly in memory, the file is first loaded and converted into a Python dictionary. This dictionary acts as the program's in-memory database.

Whenever an operation such as adding, updating, or deleting a student is performed, the corresponding changes are made to the in-memory dictionary. After the modification is complete, `save_db()` is called to overwrite the JSON file with the updated data, ensuring that all changes are permanently saved.

## Student ID Generation

Each student is assigned a unique ID when they are first added to the database. The ID follows the format:

```text
<CurrentYear>S<Number>
```

For example:

```text
2026S15
```

Where:

* `2026` represents the current year.
* `S` indicates that the record belongs to a student.
* `15` indicates that the student is the 15th student added to the database.

The student ID is also used as the key in the in-memory dictionary. Because Python dictionaries are implemented as hash tables, retrieving a student's information by their ID has an average time complexity of **O(1)** (constant time). This means the program can directly access a student's record without searching through every entry, allowing lookups to remain efficient even as the database grows.
