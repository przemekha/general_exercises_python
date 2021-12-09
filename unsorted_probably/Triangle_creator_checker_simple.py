customer_name = input("<What is Your name?> ").capitalize()
print(f"Hello {customer_name}, using submitted data I'll inform You if You are able to create a triangle. ")
print("Give me three values representing each triangle side length.")

while True:
    sides_answer = input("<Please enter values in ""A,B,C"" format, when two first values usually represent sides "
                         "lengths of triangle and the last one represents its basis:> ")
    side1, side2, basis = map(int, sides_answer.split(","))
    lengths_list = [side1, side2, basis]
    the_highest_length = max(lengths_list)
    lengths_list.remove(the_highest_length)
    rest_sum_lengths_list = sum(lengths_list)
    if rest_sum_lengths_list >= the_highest_length:
        print("You're able to create a triangle! ")
        if side1 and side2 == basis:
            print('Your triangle is equilateral. ')
        if side1 == side2 or basis:
            print("Your triangle is isosceles. ")
        else:
            print("Your triangle is scalene. ")
        if input(f"<Do You want to check again {customer_name}? (Y)es/(N)o?> ").lower() == "n":
            print("Have a nice day! ")
            exit(0)
        else:
            continue
    else:
        print("You're not able to create a triangle. ")
        if input(f"<Do You want to check again {customer_name}? (Y)es/(N)o?> ").lower() == "n":
            print("Have a nice day! ")
            exit(0)
        else:
            continue
