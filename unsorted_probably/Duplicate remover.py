import random

random_list = []

for single_number in range(0, 20):
    random_number = random.randint(0, 100)
    random_list.append(random_number)

clean_list = []

for a_number in random_list:
    if a_number not in clean_list:
        clean_list.append(a_number)
    else:
        clean_list.remove(a_number)
print(clean_list)
