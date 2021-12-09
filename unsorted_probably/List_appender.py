growing_list = []

while True:
    human_ingredient = input("<Please write something and I'll append this to the list. "
                             "Write \"No\" to stop the program.> ").lower()
    if human_ingredient != 'no':
        growing_list.append(human_ingredient)
    else:
        print(growing_list)
        exit(0)
