"""
mając listę owoców
stwórz słowniki mające jako klucze nazwy rozpoczynające się wielką literą
klucz = nazwa "apple itd
dwa różne słowniki
1. jako warotści długości nazw
2. jako wartości ceny będące sumą kodów ASCII pierwszej i ostatniej litery podzieloną przez długość nazwy
pierwsza i ostatnia litera (suma wartosci ascii funkcja ord)
fruits = ['apple', 'mango', 'banana', 'cherry', 'passionfruit', 'dragonfruit', 'date']
"""

fruits = ['apple', 'mango', 'banana', 'cherry', 'passionfruit', 'dragonfruit', 'date']

new_dictionary = {}
second_dictionary = {}

for name in fruits:
    new_dictionary.update({name.capitalize(): len(name)})

for second_name in fruits:
    calculated_value = (ord(second_name[0]) + ord(second_name[-1]))/len(second_name)
    second_dictionary.update({second_name.capitalize(): calculated_value})

print(new_dictionary)
print(second_dictionary)
