def exit_question(name):
    if input(f"<Do You want to check another date {name}? (Y)es/(N)o?> ").lower() == "n":
        print("Have a nice day! ")
        exit(0)


months_dictionary = {"january": "winter", "february": "winter", "march": "winter",
                     "april": "spring", "may": "spring", "june": "spring",
                     "july": "summer", "august": "summer", "september": "summer",
                     "october": "autumn", "november": "autumn", "december": "autumn"}

name_answer = input("<What is Your name?> ").capitalize()
season = None

while True:
    month_answer = input("<Give me a name of the month:> ").lower()
    if month_answer in months_dictionary.keys():
        try:
            day_answer = int(input("<What day is it now: > "))
        except ValueError:
            print("Something went wrong. Remember to use only numbers and data field can't be empty!. ")
            continue
    else:
        print("Something went wrong. Check for misspelled letters. ")
        continue
    if month_answer == "march" and day_answer >= 20:
        season = "Spring"
    elif month_answer == "june" and day_answer >= 21:
        season = "Summer"
    elif month_answer == "september" and day_answer >= 22:
        season = "Autumn"
    elif month_answer == "december" and day_answer >= 21:
        season = "Winter"
    else:
        season = str(months_dictionary[month_answer]).capitalize()
    print(f"It looks like we've got a beautiful {season.capitalize()} this {month_answer.capitalize()}.")
    exit_question(name_answer)
