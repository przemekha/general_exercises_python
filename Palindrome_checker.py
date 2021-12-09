def reverse_string(your_string):
    rev_string = your_string[::-1]
    return rev_string


name = input('<What is Your name?> ').capitalize()

while True:
    word = input(f'<Hi {name}, please give me a word then I will check if that word is a palindrome:> ')
    if word == reverse_string(word):
        print('Your word is a palindrome!')
    else:
        print('Your word is not a palindrome.')
    if input('<Do You want to check some other word? (Y)es/(N)o> ').lower() == 'n':
        print("Goodbye!")
        break
