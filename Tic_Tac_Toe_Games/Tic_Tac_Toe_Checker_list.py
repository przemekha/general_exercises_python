"""Wymagania:
Sprawdź rezultat gry w kółko i krzyżyk
input: string 9 znaków skłądających się z: x, o, -
(na przyład: xxxo-oo-)
znaki oznaczają pozycje wierszami od górnego wiersza
Rezultat wypisz na ekran."""


def winner_checker(package_to_check, value_to_check: str):
    """
    Funkcja przekształca zbiór package_to_check na obiekt str, porównuje odpowiednie plasterki z frazą value_to_check,
    w wyniku zwraca True wraz z informacją lub zwraca jedynie False.
    :param package_to_check: pełna lista, którą sprawdza funkcja, konwertowana na str i kopię
    :param value_to_check: wyrażenie porównawcze do wybranego elementu listy
    :return: True or False
    """
    line_to_check = "".join(str(element) for element in package_to_check)
    if line_to_check[0:3] == value_to_check or line_to_check[3:6] == value_to_check or \
            line_to_check[6:9] == value_to_check or line_to_check[0:7:3] == value_to_check \
            or line_to_check[1:8:3] == value_to_check or line_to_check[2:9:3] == value_to_check \
            or line_to_check[0:9:4] == value_to_check or line_to_check[2:7:2] == value_to_check:
        return True, print(f"{value_to_check[0].title()}'s won! ")


def the_board(package_to_compare):
    return print(f"""
This is how the game looks like now:
{package_to_compare[0]} | {package_to_compare[1]} | {package_to_compare[2]} 
{package_to_compare[3]} | {package_to_compare[4]} | {package_to_compare[5]} 
{package_to_compare[6]} | {package_to_compare[7]} | {package_to_compare[8]} 
        """)


starting_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


while True:
    the_board(starting_list)
    the_line = input("<This is a simple Tic Tac Toe game! Give me a x or o:> ").lower()
    if the_line not in ("x", "o"):
        continue
    try:
        position = int(input("And number of bracket to put it into:> "))
    except ValueError:
        print("Remember to use only numbers in range 1-9! ")
        continue
    starting_list[position - 1] = the_line
    if winner_checker(starting_list, "xxx") or winner_checker(starting_list, "ooo"):
        break
    else:
        print("For now no one won.")

the_board(starting_list)
# problem z momentem definiowania