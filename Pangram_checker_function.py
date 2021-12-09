"""
Wymagania:
Sprawdz czy strint jest pangramem –
zawiera wszystkie litery z alfabetu angielskiego
Np.:
"The quick brown fox jumps over the lazy dog"

Nie zapomnij o dokumentacji
Przygotuj zestaw danych testowych
"""
import string


def pangram_check(sentence_checked):
    sentence_checked = "".join(sentence_checked.split()).lower()
    all_letters = string.ascii_lowercase
    for letter in all_letters:
        if letter not in sentence_checked:
            return False
    return True


sentence = "The quick brown fox jumps over the lazy dog"

if pangram_check(sentence):
    print("Your sentence is a pangram! ")
else:
    print("Yours sentence is not a pangram. ")
