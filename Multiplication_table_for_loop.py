"""Wymagania:
Napisz program wypisujący tabliczkę mnozenia (1 do 10)
dla podanej przez użytkownika liczby

Wynik powinien wyglądać tak:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
itd.
"""

user_number = int(input("<Please give me a number and I'll print multiplication table for Your number:> "))

for numbers in range(1, 11):
    print(f"{user_number} x {numbers} = {user_number*numbers}")
