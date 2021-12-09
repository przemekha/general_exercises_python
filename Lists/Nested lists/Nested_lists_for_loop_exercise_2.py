"""Wymagania:
Stwórz dwuwymiarową listę, w której listy wewnętrzne będą zawierały
3 kolejne liczby naturalne w zakresie do 100 - w każdej kolejnej subliście
pierwza liczba ma być o 1 większa niż OSTATNIA w poprzedniej

Wynik:
[[0, 1, 2], [3, 4, 5], ...
"""

nested_list = []

for numbers in range(0, 100, 3):
    nested_list.append(list(range(numbers, numbers+3)))

nested_list[-1].remove(101)
print(nested_list)
