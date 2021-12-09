"""pobrać od użytkownika miesiąc i dzień
Określić porę roku.

Zadania 1 i 2 mozesz wykorzysta w pogodyn"""


def exit_question(name):
    if input(f"<Do You want to check another date {name}? (Y)es/(N)o?> ").lower() == "n":
        print("Have a nice day! ")
        exit(0)


def month_question(my_dict):
    while True:
        the_month = input("<Give me a name of the month:> ").lower()
        if the_month in my_dict.keys():
            try:
                the_day = int(input("<What day is it now: > "))
                return the_day, the_month
            except ValueError:
                print("Something went wrong. Remember to use only numbers and data field can't be empty!. ")
        else:
            print("Something went wrong. Typing field might be empty. Check for misspelled letters!. ")


def season_chooser(the_month, the_day, the_dict):
    if the_month == "march" and the_day >= 20:
        time_of_year = "Spring"
    elif the_month == "june" and the_day >= 21:
        time_of_year = "Summer"
    elif the_month == "september" and the_day >= 22:
        time_of_year = "Autumn"
    elif the_month == "december" and the_day >= 21:
        time_of_year = "Winter"
    else:
        time_of_year = the_dict[the_month]
    return time_of_year


months_dictionary = {"january": "winter", "february": "winter", "march": "winter",
                     "april": "spring", "may": "spring", "june": "spring",
                     "july": "summer", "august": "summer", "september": "summer",
                     "october": "autumn", "november": "autumn", "december": "autumn"}

name_answer = input("<What is Your name?> ").capitalize()

while True:
    day_answer, month_answer = month_question(months_dictionary)
    season = season_chooser(month_answer, day_answer, months_dictionary)
    print(f"It looks like we've got a beautiful {season.capitalize()} this {month_answer.capitalize()}.")
    exit_question(name_answer)
