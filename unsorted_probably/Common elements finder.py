import random

random_list_1 = []

for single_number_1 in range(0, 20):
    random_number = random.randint(0, 100)
    random_list_1.append(random_number)

random_list_2 = []

for single_number_2 in range(0, 20):
    random_number = random.randint(0, 100)
    random_list_2.append(random_number)

common_list = []

for single_number_3 in random_list_1:
    for single_number_4 in random_list_2:
        if single_number_3 == single_number_4:
            if single_number_3 not in common_list:
                common_list.append(single_number_4)
print(common_list)
