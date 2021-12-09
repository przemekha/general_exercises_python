"""
Wymagania:
Napisz klasę mającą dwie metody:
- get_string
- print_string

get_string - pobiera od użytkownika stringa
print_string - wypisuje stringa na ekran - co druga litera powinna być wielka.

Przykład:
asdasdasdasd -> 'AsDaSdAsDaSd'

Użyj:
wersja 1: użyj pętli
wersja 2:string slicing, oraz metody zip() oraz
operatora * do rozpakowania kolekcji
metody join do połączenie elementów kolekcji w stringa
NIE używaj pętli
"""
from itertools import zip_longest


class WordsHandler:
    def __init__(self):
        self.users_word = input("<Give me some word: >")

    def get_word(self):
        return self.users_word

    def print_string(self):
        new_word = ""
        marker = True
        for letter in self.users_word:
            if marker:
                new_word += letter.lower()
            else:
                new_word += letter.upper()
            if letter != " ":
                marker = not marker
        return new_word

    def print_string2(self):
        zipped_one = zip_longest(self.users_word[::2].lower(), self.users_word[1::2].upper(), fillvalue='')
        unzipped_one = *zipped_one,
        new_word = str()
        for i in unzipped_one:
            new_word += "".join(i)
        return new_word


new_instance = WordsHandler()
print(new_instance.get_word())
print(new_instance.print_string())
print(new_instance.print_string2())

