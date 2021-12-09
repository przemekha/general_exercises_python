nested_list = []
starting_number = 0

while starting_number < 100:
    following_number = starting_number + 3
    natural_numbers = list(range(starting_number, 101))
    natural_numbers_modified = list(range(following_number, 101))
    nested_list.append(natural_numbers[0:3])
    nested_list.append(natural_numbers_modified[0:3])
    starting_number += 6
print(nested_list)
