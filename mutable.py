shopping_list = ["PC", "Table", "Chair"]
another_list = shopping_list

print(shopping_list is another_list)

shopping_list.append("Raspberry Pi 5")
shopping_list[1] = "Cooling Cage"
print(another_list)

print(shopping_list is another_list)

wider_list = another_list[::]
print(wider_list)

print(f"Wider list ID: {id(wider_list)}")
print(f"shopping list ID: {id(shopping_list)}")

del wider_list[3::]
print(wider_list)

extended_list = [1, 2, 3, 4, 5]
extended_list.extend(wider_list)
print(extended_list)

print(extended_list is wider_list)

print("Majaliwa".count("a"))
