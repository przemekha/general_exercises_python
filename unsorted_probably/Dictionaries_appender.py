user_dictionary = {}
print("Hello, give me Your keyword and value below and I'll stack them together as a dictionary! ")
while True:
    user_key = input("<Please give me Your key:> ")
    user_value = input("<Please give me Your value:> ")
    if user_key not in user_dictionary:
        user_dictionary.update({user_key: user_value})
    for all_keywords, all_values in user_dictionary.items():
        print("{} -> {}".format(all_keywords, all_values))
    if input(f"<Do You want to add some new entries? (Y)es/(N)o?> ").lower() == "n":
        print("Have a nice day! ")
        exit(0)
