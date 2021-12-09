"""
Wymagania:
Stwórz listę kolorów.
Wypisz je w kolejności.

NAstępnie wybierz losowo jeden z kolorów,
przypisz go do nowej zmiennej i wypisz na ekran."""
import random

my_colour_list = ["black", "white", "red", "green", "blue", "cyan", "yellow", "orange", "green"]
# my_colour_list.sort() zmienia listę
# sorted (funkcja) zwraca pos. listę
print(sorted(my_colour_list))
print(my_colour_list)
# the_colour = my_colour_list[random.randint(1, len(my_colour_list)-1)]
the_colour = random.choice(my_colour_list)
print(the_colour)