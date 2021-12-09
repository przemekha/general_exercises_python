"""Stwórz dwuwymiarową listę, w której listy wewnętrzne będą zawierały
3 kolejne liczby naturalne w zakresie do 100 - w każdej kolejnej subliście
pierwza liczba ma być o 1 większa niż PIERWSZA w poprzedniej

Wynik ma mie formę:
[[0, 1, 2], [1, 2, 3], ..."""

nested_list = []

for number in range(99):
    # nested_list.append([number, number + 1, number + 2])
    nested_list.append(list(range(number, number + 3)))

print(nested_list)

