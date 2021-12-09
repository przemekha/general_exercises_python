"""Wymagania:
Zrób grę w kółko i krzyżyk. - gracz vs komputer

Nie używaj list.

Używaj jedynie modyfikacji stringa do wypełniania pól.
"""
import random


def user_data_in_check():
    while True:
        statement = input(
            "<This is a simple Tic-Tac-Toe game. You'll play versus computer. Give me a x or o:> ").lower()
        if statement == "x" or statement == "o":
            return statement
        else:
            print("Remember to use ""x"" or ""o"" only. ")


# def computer_algorithm_simple(user_input):
#     letter_sign = ""
#     if user_input == "x":
#         print("I'll try with \"o\".")
#         letter_sign += "o"
#     else:
#         print("I'll try with \"x\".")
#         letter_sign += "x"
#     return letter_sign


def computer_algorithm_random():
    x_o_signs = "xo"
    letter_sign = random.choice(x_o_signs)
    return letter_sign


def sentence_searcher(sentence_to_check):
    if sentence_to_check.find("xxx") == 0 or sentence_to_check.find("xxx") == 3 or sentence_to_check.find("xxx") == 6:
        return True, print(f"The game looks like that: {sentence_to_check}."), print("X's won! ")
    elif sentence_to_check.find("ooo") == 0 or sentence_to_check.find("ooo") == 3 or sentence_to_check.find("ooo") == 6:
        return True, print(f"The game looks like that: {sentence_to_check}."), print("O's won! ")


omni_sentence = ""

for _ in range(5):
    the_line = user_data_in_check()
    omni_sentence += the_line
    if _ != 4:
        omni_sentence += computer_algorithm_random()
        # omni_sentence += computer_algorithm_simple(the_line)
    if sentence_searcher(omni_sentence):
        break
    else:
        print(f"The game looks like that till now: {omni_sentence}. ")
        if len(omni_sentence) == 9:
            print("No one won. ")
