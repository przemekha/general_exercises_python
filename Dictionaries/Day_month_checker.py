"""
Pobierz od użytkownika nazwę miesiąca.
Pobierz od użytkownika rok.
Wskaż liczbę dni w miesiącu"""

def exit_question(name):
    if input(f"<Do You want to check another date {name}? (Y)es/(N)o?> ").lower() == "n":
        print("Have a nice day! ")
        exit(0)


def is_leap_year(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap


months_dictionary = {"january": 31, "february": 28, "march": 31,
                     "april": 30, "may": 31, "june": 30,
                     "july": 31, "august": 31, "september": 30,
                     "october": 31, "november": 30, "december": 31}

name_answer = input("<What is Your name?> ").capitalize()

while True:
    month_answer = input("<Give me a name of the month:> ").lower()
    if month_answer in months_dictionary.keys():
        try:
            year_answer = int(input("<What year is it now:> "))
        except ValueError:
            print("Something went wrong. Remember to use only numbers and data field can't be empty!. ")
            continue
    else:
        print("Something went wrong. Check for misspelled letters. ")
        continue

    if month_answer == "february" and is_leap_year(year_answer):
        # print(f"February has {months_dictionary.get('february') + 1} days this year. ") get ma sens przy uzyciu
        # dwóch argumentów np. months_dictionary.get('februyry', 'january'), w związku z tym to februyry nie istnieje
        # domyslnie zostanie wzrócona druga wartość - january
        print(f"February has {months_dictionary['february'] + 1} days this year. ")
    else:
        print(f"{month_answer.capitalize()} has {months_dictionary[month_answer]} days. ")
    exit_question(name_answer)
