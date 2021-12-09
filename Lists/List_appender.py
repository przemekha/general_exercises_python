"""Napisz program, który wczytuje od użytkownika wartości
i dodaje je do listy dopóki użytkownik nie poda wartości 'nie'

Wypisz listę na ekran."""

growing_list = []

while True:
    human_ingredient = input("<Please write something and I'll append this to the list. "
                             "Write \"No\" to stop the program.> ").lower()
    if human_ingredient != 'no':
        growing_list.append(human_ingredient)
    else:
        break

print(growing_list)