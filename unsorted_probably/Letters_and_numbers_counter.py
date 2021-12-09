import string


def exit_question():
    if input(f"<Do You want to try again? (Y)es/(N)o?> ").lower() == "n":
        print("Have a nice day! ")
        exit(0)


all_possible_numbers = string.digits
all_possible_letters = string.ascii_letters

letters_list = []
numbers_list = []

while True:
    question = input("<Write something and I'll tell You how many letters and numbers Your string contain: > ")
    for elements in question:
        if elements in all_possible_letters:
            letters_list.append(elements)
        if elements in all_possible_numbers:
            numbers_list.append(elements)
    print(f"There are {len(numbers_list)} numbers and {len(letters_list)} letters in Your string.")
    exit_question()


