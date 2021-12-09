"""
Przy użyciu funkcji napisz program
dodajacy do listy pojedynczy znak alfanumeryczny
jesli znak jest nie alfanumeryczny - odrzuc go i powtorz procedure wpisywania znaku
jesli jest alfanumeryczny sprawdz czy juz istnieje w liscie
- jesli znak nie istenieje - dodaj go do listy
- jesli istnieje to dodaj do listy tekst "Znak <znak> istnieje w liscie na pozycji <n>"
kontynuuj wprowadzanie dopoki nie bedzie 10 znakow w liscie
wypisz zawartosc listy na ekran
"""


def quest(sign, your_list):
    if not sign.isalnum() or len(sign) != 1:
        print("Your sign is not alphanumeric or longer than one. Please enter an alphanumeric or single-digit sign. ")
    else:
        if len(your_list) != 0:
            for element in your_list:
                if element == sign:
                    your_list.append([f"Sign {sign} already exist in list on {your_list.index(sign)} position."])
                    break
            else:
                your_list.append(sign)
        else:
            your_list.append(sign)


def count(sample_list):
    encirclement = 0
    for value in sample_list:
        if len(str(value)) == 1:
            encirclement += 1
    return encirclement


user_list = []
counter = 0

while counter != 10:
    your_sign = input("<Please enter Your single-digit alphanumeric sign and I'll append it to Your list:> ")
    quest(your_sign, user_list)
    counter = count(user_list)
print(user_list)
