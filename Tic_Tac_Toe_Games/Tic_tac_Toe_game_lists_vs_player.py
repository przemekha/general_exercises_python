"""
Wymagania:
Zrób grę w kółko i krzyżyk. - dla dwóch graczy

Podpowiedź:
Posłuż się listami i pętlami
"""


def user_data_in_check(player_one_name: str, player_two_name: str) -> int:
    """
    :param player_one_name:
    :param player_two_name:
    :return: int in real range 1-9
    """
    while True:
        statement = int(input(f"<Hello {player_one_name}, this is a simple Tic-Tac-Toe game. "
                              f"You'll play versus {player_two_name}. Your sign is \"X\". "
                              f"Please give me a number to place Your \"X\" in suitable bracket:> "))
        if statement in range(1, 10):
            return statement
        else:
            print("Remember to use numbers in range from 1 to 9. ")


def user2_data_in_check(player_two_name, player_one_name) -> int:
    """
    :param player_two_name:
    :param player_one_name:
    :return: int in real range 1-9
    """
    while True:
        statement = int(input(f"<Hello {player_two_name}, this is a simple Tic-Tac-Toe game. "
                              f"You'll play versus {player_one_name}. Your sign is \"O\". "
                              f"Please give me a number to place Your \"O\" in suitable bracket:> "))
        if statement in range(1, 10):
            return statement
        else:
            print("Remember to use numbers in range from 1 to 9. ")


def winner_checker(package_to_check, value_to_check: str):
    """
    Funkcja tworzy kopię zbioru package_to_check, porównuje odpowiednie plasterki z frazą value_to_check,
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
    else:
        print("For now no one won. ")

def the_board(package_to_compare):
    board = f"""
This is how the game looks like now:
{package_to_compare[0]} | {package_to_compare[1]} | {package_to_compare[2]} 
{package_to_compare[3]} | {package_to_compare[4]} | {package_to_compare[5]} 
{package_to_compare[6]} | {package_to_compare[7]} | {package_to_compare[8]} 
        """
    return board


player1_name = input("<What is Your name Player1?> ").capitalize()
player2_name = input("<What is Your name Player2?> ").capitalize()
starting_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    print(the_board(starting_list))
    position_for_user1 = user_data_in_check(player1_name, player2_name)
    starting_list[position_for_user1 - 1] = "X"
    if winner_checker(starting_list, "XXX"):
        break
    print(the_board(starting_list))
    position_for_user2 = user2_data_in_check(player2_name, player1_name)
    starting_list[position_for_user2 - 1] = "O"
    if winner_checker(starting_list, "OOO"):
        break


print(the_board(starting_list))

# for _ in range(5):
#     player_one_data = user_data_in_check(player1_name, player2_name)
#     omni_sentence.append(player_one_data)
#     if _ != 4:
#         player_two_data = user2_data_in_check(player2_name, player1_name)
#         omni_sentence.append(player_two_data)
#     if sentence_searcher(omni_sentence):
#         break
#     else:
#         print(f"The game looks like that till now: {' - '.join(omni_sentence)}. ")
#         if len(omni_sentence) == 9:
#             print("No one won. ")
