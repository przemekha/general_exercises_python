"""
Wymagania:
Użyj pętli for, żeby:
1. Stworzyć listę szceścianów liczb jeśli liczba bazowa jest podzielna przez 5 (1 od 1 do 500)
2. Mając do dyspozycji tuplę (1, 2) stworzyć listę wszystkich kombinacji.
   Wynik: (1, 1), (1, 2), (2, 1), (2, 2)
3. Stworzyć listę list zawierającą liczby podzielone przez 2, podzielone przez 3 oraz bazowe liczby
   gdy liczba bazowa w zakresie
   daje resztę 3 przy dzielenie przez 4 (zakres od 1 to 500) (to pierwotna lista, apóżniej lista przez2 i przez 3(jedna) i robię podlistę)
   Wynik:
   [[1.5, 1, 3], [3.5, 2.3333333, 7], ...]
4. Stworzyć listę list, w której listy wewnętrzne zawierają liczby z zakresu pierwszej
   listy podzielone przez liczby z zakresu drugiej listy
   Przykład:
   lista_1 = [1, 2, 3]
   lista_2 = [1, 2, 3, 4]
   wynik => [[1.0, 0.5, 0.3333333333333333, 0.25], [2.0, 1.0, 0.6666666666666666, 0.5], [3.0, 1.5, 1.0, 0.75]]
"""


# 1gfgfgf
exponentiation_list = []

for plain_numbers in range(1, 501):
    if plain_numbers % 5 == 0:
        exponentiation_list.append(plain_numbers**3)

# 2
__little_tuple = (1, 2)
new_list = []
for tuple_num in __little_tuple:
    for num_tuple in __little_tuple:
        new_list.append((tuple_num, num_tuple))
        # print(f"({tuple_num}, {num_tuple})", end= ", ")
print(new_list)

# 3

dividable_2_list = []
dividable_3_list = []
dividable_base_list = []
mighty_list = [dividable_2_list, dividable_3_list, dividable_base_list]

for dividable_numbers in range(0, 501):
    if dividable_numbers % 4 == 3:
        dividable_base_list.append(dividable_numbers)
for some in dividable_base_list:
    dividable_2_list.append(some/2)
for something in dividable_2_list:
    dividable_3_list.append(something/3)
print(mighty_list)

lista1 = [1, 2, 3]
lista2 = [1, 2, 3, 4, 5]
lista3 = []
lista4 = []


for i in lista1:
    lista4.append([])
    for e in lista2:
        lista4[i].append(i/e)
print(lista4)