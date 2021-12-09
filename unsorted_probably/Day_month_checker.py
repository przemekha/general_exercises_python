def exit_question(name):
    if input(f"<Do You want to check another date {name}? (Y)es/(N)o?> ").lower() == "n":
        print("Have a nice day! ")
        exit(0)


months_dictionary = {"january": 31, "february": 28, "march": 31,
                     "april": 30, "may": 31, "june": 30,
                     "july": 31, "august": 31, "september": 30,
                     "october": 31, "november": 30, "december": 31}

name_answer = input("<What is Your name?> ").capitalize()
leap_year = False

while True:
    month_answer = input("<Give me a name of the month:> ").lower()
    if month_answer in months_dictionary.keys():
        try:
            year_answer = int(input("<What year is it now:> "))
        except ValueError:
            print("Something went wrong. Remember to use only numbers and data field can't be empty!. ")
            continue
        if year_answer % 4 == 0:
            if year_answer % 100 == 0:
                if year_answer % 400 == 0:
                    leap_year = True
                else:
                    leap_year = False
            else:
                leap_year = True
        else:
            leap_year = False
    else:
        print("Something went wrong. Check for misspelled letters. ")
        continue

    if month_answer == "february" and leap_year is True:
        print(f"February has {int(months_dictionary.get('february')) + 1} days this year. ")
    else:
        print(f"{month_answer.capitalize()} has {months_dictionary.get(month_answer)} days. ")
    exit_question(name_answer)
