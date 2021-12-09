"""Wymagania:
Napisz program, który wczytuje od użytkownika stringi w postaci klucz - wartość
Dodaj je do słownika.
Jeśli dany klucz istnieje w słowniku - nie rób nic.

Zapewnij możliwość podania kolejnych par klucz-wartość lub zaprzestawania ich podawania.

Wypisz elementy słownika na ekran w formie "klucz -> wartość"""

user_dictionary = {}
print("Hello, give me Your keyword and value below and I'll stack them together as a dictionary! ")
while True:
    user_key = input("<Please give me Your key:> ")
    user_value = input("<Please give me Your value:> ")
    if user_key not in user_dictionary:
        # user_dictionary.update({user_key: user_value})
        # to samo co niżej
        user_dictionary[user_key] = user_value
    for keyword, value in user_dictionary.items():
        # print("{} -> {}".format(keyword, value))
        # to samo co niżej
        print(f"{keyword} -> {value}")
    if input(f"<Do You want to add some new entries? (Y)es/(N)o?> ").lower() == "n":
        print("Have a nice day! ")
        exit(0)
