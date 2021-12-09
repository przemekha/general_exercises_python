correct_password = "admin1"
counter = 4

while True:
    password_answer = input('<Hello, welcome to SpaceY, to launch the space rocket enter a valid password: > ')
    if password_answer != correct_password:
        print("Something went wrong, try again. ")
        counter = counter - 1
        if counter in range(2, 5):
            print(f"You got only {counter} tries left. ")
            continue
        elif counter == 1:
            print(f"This is Your last try. ")
            continue
        else:
            print("It looks like We've got an impostor among us.")
            print("Goodbye (in an unpleasant way)!")
    else:
        print("Password accepted, welcome to the future.")
    exit(0)