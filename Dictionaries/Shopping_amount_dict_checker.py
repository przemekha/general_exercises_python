"""Zadanie z treścią:
Ania chce kupić klawiaturę k oraz pendrive p.
Posiada ustaloną kwotę pieniędzy p.
W sklepie są podane ceny w listach klawiatury i pendrivy.
Ania chce wykorzystać możliwie całą gotówkę, aby kupić klawiaturę i pendrive.


Weż pod uwagę, że Ania potrzebuje zarówno klawiatury jak i pendrive -
zakupienie jednej rzeczy nie wchodzi w grę.
Sprawdź czy uda jej się to zrobić - jeśli tak, wypisz wydaną sumę pieniędzy,
jeśli nie - podaj stosowny komunikat.

Przykładowe dane i wynik:
k = [500 ,125 ,50, 21, 13]
p = [10, 17, 28, 75]
s = 50

wynik:
Ania wydała 50zł na klawiaturę i pendrive (klawiatura kosztowała 21zł, a pendrive 28zł)
wydała 50zł na klawiaturę i pendrive (klawiatura kosztowała 21zł, a pendrive 28zł
########################################################################################################################

k = [500 ,125 ,450, 21, 66]
p = [100, 170, 30, 75]
s = 50

wynik:
Ani nie udało się zrobić zakupów za 50zł.
"""

keyboards = [500, 125, 50, 21, 13]
pen_drives = [10, 17, 28, 75]
pocket = 50
total_amount_dict = {}

# simple

for i in keyboards:
    for e in pen_drives:
        if e+i <= pocket:
            print(f"Anne spent {e+i}zł on keyboard and pen drive. (Keyboard cost {i}zł and pen drive {e}zł.)")
            break
            # wyrzuca dwa printy, chyba iteracja dla drugiego warunku jeszcze się nie zakończyła?

# actually working

for i in keyboards:
    for e in pen_drives:
        if e+i <= pocket:
            total_amount_dict[i] = e
            # tu przyjmie wg. list tylko dwie pary

if not total_amount_dict:
    print(f"Anne didn't menage to shop for {pocket}zł. ")
else:
    for key_w, val in total_amount_dict.items():
        all_together = key_w + val
    print(f"Anne spent {all_together}zł on keyboard and pen drive. (Keyboard cost {key_w}zł and pen drive {val}zł.)")


