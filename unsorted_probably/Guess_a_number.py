import random


def ask_for_number_in_range(l_bound, u_bound):
    while True:
        try:
            guess = int(input("<Guess what number I'm thinking about?> "))
            if guess >= l_bound and guess <= u_bound:
                return guess
            else:
                print(f'Remember, You should use numbers in range from {l_bound} to {u_bound} only.')
                print(f"I won't charge you for that. You have still {8 - guess_count} tries left. ")
        except ValueError:
            print(f'Remember, You should use numbers in range from {l_bound} to {u_bound} only.')


def play_again_question(name):
    if input(f'<{name}, do You want to play again? (Y)es/(N)o.> ').lower() == 'n':
        print('Goodbye, see you soon!')
        exit(0)


lower_bound = 1
upper_bound = 101
the_number = random.randint(lower_bound, upper_bound)
guess_count = 0

player_name = input('<What is Your name?> ').capitalize()
print(f"Hello {player_name}, this is a guess game. Here are The Rules:")
print(f"I'm thinking of a random number from {lower_bound} to {upper_bound}.")
print("You have to find the number I'm thinking about. ")
print("Please remember that You have only 8 attempts.")

while True:
    player_guess = ask_for_number_in_range(lower_bound, upper_bound-1)
    if player_guess > the_number:
        guess_count += 1
        print('Your guess is higher than my number.')
    elif player_guess < the_number:
        guess_count += 1
        print('Your guess is lower than my number.')
    else:
        print('Your number equals mine! You won! ')
        if play_again_question(player_name):
            break
        else:
            guess_count = 0
            the_number = random.randint(lower_bound, upper_bound)
            continue
    if guess_count == 7:
        print(f'---Focus! This is Your last chance!---')
    else:
        print(f'---You have {8-guess_count} tries left---')
    if guess_count == 8:
        print('Unfortunately You’ve reached the maximum number of attempts. You lost. ')
        print(f'By the way my number was {the_number}.')
        if play_again_question(player_name):
            break
        else:
            guess_count = 0
            the_number = random.randint(lower_bound, upper_bound)
