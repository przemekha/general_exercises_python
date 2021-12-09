"""
Mając słownik inventory
Stwórz klucz "pocket" w którym będzie lsita stringów: 'seashell', 'strange berry', and 'lint'.
usuń sztylet z plecaka
dodaj 340 monet
wypisz listę wszystkich posiadanych przedmiotów
"""
inventory = {}
inventory["dagger"] = 1
inventory["coins"] = 0
inventory["pocket"] = ["seashell", "strange berry", "lint"]
for _ in range(340):
    if "coins" in inventory.keys():
        inventory["coins"] += 1

# print(inventory["coins"])
# inventory["pocket"].remove("dagger")
inventory["pocket"].append("stone")
print(inventory)
# del inventory["dagger"]
# print(inventory)
print(*inventory["pocket"], sep=', ')
print(f"There are {', '.join(inventory['pocket'])} in Your backpack.")
print(list(inventory.keys())[1])
print(len(list(inventory.keys())))

for item_name, item_amount in inventory.items():
    # print(f"{item_name=} ===> {item_amount=}")
    # print(f"{item_name} ===> {item_amount}")
    if isinstance(item_amount, list):
        print(f"There are {', '.join(inventory[item_name])} in Your backpack.")
    else:
        print(f"I have {item_amount} {item_name}. ")