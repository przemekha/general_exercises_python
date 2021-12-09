"""Wymagania:
Uzywajac funkcji napisz program
obliczajacy ciag fibonacciego rekurencyjnie"""

n_1, n_2 = 0, 1

while True:
    user_number = int(input("<Insert a number to print Fibonacci sequence:> "))
    if user_number <= 0:
        print("Please use positive number. ")
        continue
    else:
        print("Fibonacci sequence:")
        for _ in range(user_number):
            print(n_1)
            n_formula = n_1 + n_2
            n_1 = n_2
            n_2 = n_formula
    break

