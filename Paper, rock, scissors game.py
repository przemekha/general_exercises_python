import random

print("Hello, let's play a game called Paper, Rock and Scissors.")
print("You'll play against clever algorithm but remember - nobody's infallible. Even me.")
print("But mostly I'm right.")
print('''
The Rules:
Rock beats Scissors,
Scissors beats Paper,
Paper beats Rock.
''')

options = ['rock', 'paper', 'scissors']

player_name = input('<Give me Your name:> ').capitalize()
bot = random.choice(options)

while True:
    players_choice = input(f'<Hey {player_name}, hit me with "scissors", "paper" or "rock":> ').lower()
    bot_choice = bot
    if players_choice == bot_choice:
        print("It's a draw!. ")
    elif players_choice == 'rock':
        if bot_choice == 'scissors':
            print(f'You are the winner {player_name} - Rock wins. ')
        else:
            print('I win! - Paper wins. ')
    elif players_choice == 'scissors':
        if bot_choice == 'paper':
            print(f'You are the winner {player_name} - Scissors wins. ')
        else:
            print('I win! - Rock wins.')
    elif players_choice == 'paper':
        if bot_choice == 'rock':
            print(f'You are the winner {player_name} - Paper wins. ')
        else:
            print('I win! - Scissors wins. ')
    else:
        print("Something went wrong, let's try again. ")
        print('''
But remember to choose only between:
"paper"
"rock" or 
"scissors".
        ''')
        continue
    if input('<Do You want to try again (Y)es/(N)o?> ').lower() == 'n':
        print('Goodbye! ')
        break
    else:
        print("Let's try again then! ")
