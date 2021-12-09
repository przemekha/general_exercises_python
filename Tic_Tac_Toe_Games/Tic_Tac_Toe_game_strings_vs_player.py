"""Wymagania:
Zrób grę w kółko i krzyżyk. - dla dwóch graczy

Nie używaj list.

Używaj jedynie modyfikacji stringa do wypełniania pól.
"""


def user_data_in_check(player_one_name, player_two_name):
    while True:
        statement = input(f"<Hello {player_one_name}, this is a simple Tic-Tac-Toe game. "
                          f"You'll play versus {player_two_name}. Give me a x or o:> ").lower()
        if statement == "x" or statement == "o":
            return statement
        else:
            print("Remember to use ""x"" or ""o"" only. ")


def user2_data_in_check(player_two_name, player_one_name):
    while True:
        statement = input(f"<Hello {player_two_name}, this is a simple Tic-Tac-Toe game. "
                          f"You'll play versus {player_one_name}. Give me a x or o:> ").lower()
        if statement == "x" or statement == "o":
            return statement
        else:
            print("Remember to use ""x"" or ""o"" only. ")


def sentence_searcher(sentence_to_check):
    if sentence_to_check.find("xxx") == 0 or sentence_to_check.find("xxx") == 3 or sentence_to_check.find("xxx") == 6:
        return True, print(f"The game looks like that: {' - '.join(sentence_to_check)}."), print("X's won! ")
    elif sentence_to_check.find("ooo") == 0 or sentence_to_check.find("ooo") == 3 or sentence_to_check.find("ooo") == 6:
        return True, print(f"The game looks like that: {' - '.join(sentence_to_check)}."), print("O's won! ")


omni_sentence = ""
player1_name = input("<What is Your name Player1?> ").capitalize()
player2_name = input("<What is Your name Player2?> ").capitalize()

for _ in range(5):
    player_one_data = user_data_in_check(player1_name, player2_name)
    omni_sentence += player_one_data
    if _ != 4:
        player_two_data = user2_data_in_check(player2_name, player1_name)
        omni_sentence += player_two_data
    if sentence_searcher(omni_sentence):
        break
    else:
        print(f"The game looks like that till now: {' - '.join(omni_sentence)}. ")
        if len(omni_sentence) == 9:
            print("No one won. ")
