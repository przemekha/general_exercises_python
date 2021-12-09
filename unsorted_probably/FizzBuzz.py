for a_number in range(1, 100):
    if a_number % 3 == 0 and a_number % 5 == 0:
        print('Fizzbuzz')
    elif a_number % 3 == 0:
        print('Fizz')
    elif a_number % 5 == 0:
        print('Buzz')
    else:
        print(a_number)
