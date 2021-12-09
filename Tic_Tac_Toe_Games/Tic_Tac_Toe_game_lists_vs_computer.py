"""Wymagania:
Zrób grę w kółko i krzyżyk. - gracz vs komputer
Napisz algorytm decyzyjny dla komputerowego gracza.

Podpowiedź:
Posłuż się listami i pętlami
"""
import random


def user_data_in_check(the_user_letter) -> int:
    """
    :param the_user_letter: Pobiera od gracza "X" lub "O".
    :return: Int in real range 1-9
    """
    while True:
        try:
            number = int(input(f"You'll play versus computer. Your sign is {the_user_letter}. "
                               f"Please give me a number to place Your {the_user_letter} in suitable bracket:> "))
        except ValueError:
            print("Remember to use only numbers in range from 1 to 9. ")
            continue
        if number in range(1, 10):
            # w przypadku większych zakresów lepiej używac < >
            return number
        else:
            print("Remember to use only numbers in range from 1 to 9. ")


def computer_algorithm(user_letter, package_to_check):
    """
    :param user_letter: Pulling the user's letter.
    :param package_to_check: Pulling the Tic Tac Toe list.
    :return: Str letter "X" or "O" and int with bracket number.
    """
    # computer_letter = "X"
    # if user_letter == "X":
    #     computer_letter = "O"
    computer_letter = "O" if user_letter == "X" else "X"
    # only_numbers = []
    # for numbers in package_to_check:
    #     if numbers in range(1, 10):
    #         only_numbers.append(numbers)
    # LIST COMPREHENTION daje ten sam wynik, co stworzenie świeżej listy., kod jest czytelniejszy,
    # w przypadku np. wypełnienia listy/przefiltrtowanie - lepiej l. comprehention, inczaje- użycie rozgałęzionego fora
    only_numbers = [number for number in package_to_check if number in range(1, 10)]
    computer_number = random.choice(only_numbers)
    return computer_letter, computer_number


def winner_checker(package_to_check, value_to_check: str):
    """
    Funkcja tworzy zmodyfikowany string bez spacji ze zbioru package_to_check,
    porównuje odpowiednie plasterki z frazą value_to_check,
    w wyniku zwraca True wraz z informacją lub zwraca jedynie False.
    :param package_to_check: Pełna lista, którą sprawdza funkcja.
    :param value_to_check: Str, wyrażenie porównawcze do wybranego elementu listy.
    :return: True z informacją lub False z informacją
    """
    value_to_check *= 3
    line_to_check = "".join(str(element) for element in package_to_check)
    new_one = [line_to_check[0:3], line_to_check[3:6], line_to_check[6:9], line_to_check[0:7:3], line_to_check[1:8:3],
               line_to_check[2:9:3], line_to_check[0:9:4], line_to_check[2:7:2]]
    winner = value_to_check in new_one
    # winner = line_to_check[0:3] == value_to_check or line_to_check[3:6] == value_to_check or \
    #          line_to_check[6:9] == value_to_check or line_to_check[0:7:3] == value_to_check \
    #          or line_to_check[1:8:3] == value_to_check or line_to_check[2:9:3] == value_to_check \
    #          or line_to_check[0:9:4] == value_to_check or line_to_check[2:7:2] == value_to_check
    if winner:
        print(f"{value_to_check}'s won! ")
    else:
        print("For now no one won. ")
    return winner
    #zwróci albo Flase albo True (alternatywa dla return True - zamknięcie w zmiennej)


def the_board(package_to_compare):
    return f"""
This is how the game looks like now:
{package_to_compare[0]} | {package_to_compare[1]} | {package_to_compare[2]} 
{package_to_compare[3]} | {package_to_compare[4]} | {package_to_compare[5]} 
{package_to_compare[6]} | {package_to_compare[7]} | {package_to_compare[8]} 
        """


starting_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
_letters = ("X", "O")
randomly_chosen_player_letter = random.choice(_letters)  # choose random letter for player
print(f"Hello, this is a easy Tic Tac Toe game. At first lets choose which letter will be Yours... "
      f"Your letter is {randomly_chosen_player_letter}. ")
print(the_board(starting_list))

for _ in range(5):
    the_user_number = user_data_in_check(randomly_chosen_player_letter)
    starting_list[the_user_number - 1] = randomly_chosen_player_letter
    if winner_checker(starting_list, randomly_chosen_player_letter):
        break
    if _ != 4:
        print("It's time for computer! ")
        the_computer_letter, the_computer_number = computer_algorithm(randomly_chosen_player_letter, starting_list)
        starting_list[the_computer_number - 1] = the_computer_letter
        print(the_board(starting_list))
        if winner_checker(starting_list, the_computer_letter):
            break
print(the_board(starting_list))


# TODO także zablokowanie możliwości
#  wprowadzania x i o na już wcześniej używane pole przez użytkownika, info jeszcze kto wygrał oraz
