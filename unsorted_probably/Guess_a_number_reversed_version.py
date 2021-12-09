import random


def play_again_question(name):
    if input(f'<{name}, do You want to play again? (Y)es/(N)o.> ').lower() == 'n':
        print('Goodbye, see you soon!')
        exit(0)


lower_bound = 1
upper_bound = 101
guess_count = 0


player_name = input('<What is Your name?> ').capitalize()
print(f"Hello {player_name}, let's play a game. The thing is that:")
print(f"You'll type a random number in range from {lower_bound} to {upper_bound}. I'll keep it a secret.")
print("My job is to find Your number. Only thing i'll need is the information is Your number higher or lower than mine.")
print("To spice things up I'll have only 8 attempts to find Your number.")
print("But please remember - don't cheat. I'm a simple machine.")

while True:
    try:
        my_number = int(input(f"<Choose a number in range from {lower_bound} to {upper_bound}.> "))
        if my_number <= 0 or my_number > 100:
            print(f'Remember, You should use numbers in range from {lower_bound} to {upper_bound} only.')
        else:
            break
    except ValueError:
        print(f'Remember, You should use numbers in range from {lower_bound} to {upper_bound} only.')

while True:
    the_number = random.randint(lower_bound, upper_bound)
    print(f"This is my number: {the_number}.")
    print("Please tell me: is my number higher or lower thant Yours? Or maybe equal? ")
    higher_or_lower = input("<(H)igher/(L)ower/(E)qual>").lower()
    if higher_or_lower == "h":
        guess_count += 1
        upper_bound = the_number
        the_number = random.randint(lower_bound, upper_bound)
        print("It seems like my number is higher than Your number...")
    elif higher_or_lower == "l":
        guess_count += 1
        lower_bound = the_number
        the_number = random.randint(lower_bound, upper_bound)
        print("It seems like my number is lower than Your number...")
    elif higher_or_lower == "e":
        print('My number equals Yours! I won! Woohoo! ' )
        if play_again_question(player_name):
            break
        else:
            guess_count = 0
            continue
    else:
        print(f'Please, use only letters "H", "L" or "E".')
        print('OK, lets start from beginning. ')
    if guess_count == 7:
        print(f'---OK! This is my last chance!---')
    else:
        print(f'---I have {8-guess_count} tries left---')
    if guess_count == 8:
        print("Unfortunately I've reached the maximum number of attempts. I lost.")
        if play_again_question(player_name):
            break
        else:
            guess_count = 0