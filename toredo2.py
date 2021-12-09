# name = (input('Podaj swoje imię: '))
# age = int(input('Podaj swój wiek: '))
# times_number = int(input(' Podaj jakąś liczbę: '))
# print((f'Hej {name}, w roku {100-age+2020} skończysz sto lat.\n')*times_number)


# number = int(input('Podaj jakąś liczbę: '))
# check = int(input('Podaj liczbę sprawdzającą: '))
# rest = number % 2
# dividedbyfour = number % 4
# checker = check % number
#
# if rest == 0:
#     print('Liczba 1 jest parzysta. ')
# if dividedbyfour == 0:
#     print('Liczba 1 jest podzielna przez cztery. ')
# else:
#     print('Liczba 1 jest nieparzysta. ')
#
#
# if checker == 0:
#     print('Podane liczby się przez siebie dzielą!')
# else:
#     print('Podane liczby się przez siebie nie dzielą.')

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# user_number = int(input('Podaj swój numer: '))
#
# new_a=[]
# for i in a:
#     if i < user_number:
#         new_a.append(i)
# print(new_a)
#
# print([i for i in a if i<55])
# # print(własciwy print (output) konktrukcja for element in lista if filtr)

# number = int(input('Podaj liczbę: '))
#
# divisor = range(1, number+1)
#
# divisors_list = []
#
# for i in divisor:
#     rest = number % i
#     if rest == 0:
#         divisors_list.append(i)
#     else:
#         pass
# print(divisors_list)


# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# even = [i for i in a if i % 2 == 0]
# print(even)
#
# # LUB INACZEJ
#
# import random
#
# lista = []
# dlugosc = random.randint(5, 50)
#
# # dopóki
#
# while len(lista) < dlugosc:
#     lista.append(random.randint(1,75))
#
#
# even = [i for i in lista if i % 2 == 0]
# print(even)

"""gra w zgadywanie liczb - max 8 kroków
zakres 1 - 100 włącznie
komputer losuje liczbę a ty masz zgadnąć w max 8 krokach

1. oparta na pętli while (jak dotychczas)
2. oparta na pętli for

- odpytywanie użytkownika o dane
- jasne i czytelne komuniakty
- ograniczenie możliwości zgadywania
- * obsluga wyjatkow
- * zadanie specjalne - wymyslam sobie liczbe, moj algorytm zgaduje te liczby
- komputer podaje liczbe, ktora zgaduje, a uzytkownik mowi, czy jest mniejsza, czy wieksza
"""







# import random
#
#
# random_list_one = []
# for i in range(0, 15):
#     n = random.randint(0, 100)
#     random_list_one.append(n)
#
#
# random_list_two = []
# for i in range(0, 15):
#     n = random.randint(0, 100)
#     random_list_two.append(n)
#
#
# common_elements = []
#
# for i in random_list_one:
#     for it in random_list_two:
#         if i==it:
#             common_elements.append(i)
# print(common_elements)

# LUB

# import random
#
# a = random.sample(range(1, 30), 12)
# b = random.sample(range(1, 30), 12)
# result = [i for i in a if i in b]
# print(result)



import random

ranlist = random.sample(range(0, 20), 10)

print(min(ranlist), max(ranlist))

num = 91119

for i in str(num):
    res = [int(i)]
    for i in res:
        sq = i**2
        wynik = sq*len(res)
    print(wynik)




