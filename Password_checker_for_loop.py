correct_password = "admin1"

# for counter in range(1, 5):
#     password_answer = input('<Hello, welcome to SpaceY, to launch the space rocket enter a valid password: > ')
#     if password_answer != correct_password:
#         if counter < 4:
#             print("Something went wrong, try again. ")
#             print(f"You've got only {4 - counter} tries left. ")
#         else:
#             print("It looks like We've got an impostor among us.")
#             print("Goodbye (in an unpleasant way)!")
#     else:
#         print("Password accepted, welcome to the future.")
#         break

for counter in range(4, -1, -1):
    password_answer = input('<Hello, welcome to SpaceY, to launch the space rocket enter a valid password: > ')
    if password_answer == correct_password:
        print("Password accepted, welcome to the future.")
        break
    else:
        print("Something went wrong, try again. ")
        print(f"You've got only {counter} tries left. ")
else:
    print("It looks like We've got an impostor among us.")
    print("Goodbye (in an unpleasant way)!")
