"""Stwórz dwuwymiarową listę, w której listy wewnętrzne będą zawierały
3 kolejne liczby naturalne w zakresie do 100 - w każdej kolejnej subliście
pierwza liczba ma być o 1 większa niż PIERWSZA w poprzedniej

Wynik ma mie formę:
[[0, 1, 2], [1, 2, 3], ..."""

nested_list = []

starting_number = 0

while starting_number < 99:
    following_number = starting_number + 1
    natural_numbers = list(range(starting_number, 101))
    natural_numbers_modified = list(range(following_number, 101))
    nested_list.append(natural_numbers[0:3])
    nested_list.append(natural_numbers_modified[0:3])
    starting_number += 2
print(nested_list)


