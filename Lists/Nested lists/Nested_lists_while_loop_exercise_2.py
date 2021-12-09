"""Wymagania:
Stwórz dwuwymiarową listę, w której listy wewnętrzne będą zawierały
3 kolejne liczby naturalne w zakresie do 100 - w każdej kolejnej subliście
pierwza liczba ma być o 1 większa niż OSTATNIA w poprzedniej

Wynik:
[[0, 1, 2], [3, 4, 5], ...
"""

nested_list = []
starting_number = 0

while starting_number < 100:
    following_number = starting_number + 3
    natural_numbers = list(range(starting_number, 101))
    natural_numbers_modified = list(range(following_number, 101))
    nested_list.append(natural_numbers[0:3])
    nested_list.append(natural_numbers_modified[0:3])
    starting_number += 6
print(nested_list)
