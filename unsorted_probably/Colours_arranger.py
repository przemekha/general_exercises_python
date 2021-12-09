import random

my_colour_list = ["black", "white", "red", "green", "blue", "cyan", "yellow", "orange", "green"]
my_colour_list.sort()
print(my_colour_list)
the_colour = my_colour_list[random.randint(1, len(my_colour_list)-1)]
print(the_colour)