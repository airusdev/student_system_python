# start the system loop

def main_menu():
    print("\nStudent Record System")
    print("─────────────────────", end="\n")
    print("[1] Add Student")
    print("[2] Update Student")
    print("[3] Delete Student")
    print("[4] Search Student")
    print("[5] List All Students")
    print("[6] Sort Students")
    print("[7] Exit", end="\n")

    user_choice = int(input("\nChoice: "))
    return user_choice


valid_choice = False

# system loop
while True:
    valid_choice = False

    while not valid_choice:
        user_choice = main_menu()
        print(user_choice)
        valid_choice = True
    
        break   