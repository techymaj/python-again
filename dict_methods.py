pantry: list[str] = ["chicken", "spam", "egg", "bread", "lemon"]

# creates a new dict from iterable with default values
new_dictionary: dict[str, str] = dict.fromkeys(pantry)
print(new_dictionary)


case = {
    "beer": 2,
    "kegs": 4,
    "soda": 3
}

new_case = dict.fromkeys(case, 20)
print(new_case)
