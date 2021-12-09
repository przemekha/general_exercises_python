import random

lower_bound = 1
upper_bound = 100
thenumber = random.randint(lower_bound, upper_bound)
guess_count = 0

player_name = input('<What is Your name?> ').capitalize()
print(f"Hello {player_name}, this is a guess game. Here are The Rules:")
print(f"I'm thinking of a random number from {lower_bound} to {upper_bound}.")
print("You have to find the number I'm thinking about. ")
print("Please remember that You have only 8 attempts.")


def counter(number_of_guesses: int):
    if number_of_guesses < 7:
        print(f"I won't charge you for that. You have still {8 - number_of_guesses} tries left. ")
    else:
        print(f"I won't charge you for that. But remember - this is Your last try!")


while True:
    try:
        player_guess = int(input("<Guess what number I'm thinking about?> "))
    except ValueError:
        print(f'Remember, You should use numbers in range from {lower_bound} to {upper_bound} only.')
        counter(guess_count)
        continue
    if player_guess <= 0 or player_guess > 100:
        print(f'Remember, You should use numbers in range from {lower_bound} to {upper_bound} only.')
        counter(guess_count)
        continue
    if player_guess > thenumber:
        guess_count += 1
        print('Your guess is higher than my number.')
    elif player_guess < thenumber:
        guess_count += 1
        print('Your guess is lower than my number.')
    else:
        print('Your number equals mine! You won! ')
        break
    if guess_count == 7:
        print(f'---Focus! This is Your last chance!---')
    elif guess_count == 8:
        pass
    else:
        print(f'---You have {8-guess_count} tries left---')
    if guess_count < 8:
        pass
    else:
        print('Unfortunately You’ve reached the maximum number of attempts. You lost. ')
        print(f'By the way my number was {thenumber}.')
        if input(f'<{player_name}, do You want to play again? (Y)es/(N)o.> ').lower() == 'n':
            break
        else:
            guess_count = 0
            pass