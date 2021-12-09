"""
Wymagania:
Napisz funkcję, sprawdzającą czy dana liczba jest w podanym zakresie liczb.

1. Weź pod uwagę zakres jako przekazywaną kolekcję (listę)
2. Weż pod uwagę zakres jako range(liczba)

Nie zapomnij o dokumentacji
Przygotuj zestaw danych testowych
"""


def range_checker(user_number, range_input):
    if range_input == type(list):
        for number in range_input:
            if number == user_number:
                return True
            else:
                return False
    else:
        if user_number in range_input:
            return True
        else:
            return False


if range_checker(6, range(14)):
    print("Supplied numbers range include Your number. ")
else:
    print("Supplied numbers range doesn't include Your number. ")

# mozna rozszerzyć o wychwyt Type error za podanie pojedynczego inta, który nie przechodzi przez iterację