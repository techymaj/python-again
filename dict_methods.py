from dict_intro import top_5_football_clubs

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

keys = new_case.keys()
print(keys)

for item in new_case.keys():
    print(item)

empty_case = {

}

# update can also take an iterable of tuples. don't unpack the tuple
empty_case.update(
    slot for slot in case.items()
)

# also possible but will base keys on new index values
# empty_case.update(
#     enumerate(case)
# )

case["safi"] = 100

print(f"Not so empty, now, are ya? {empty_case}")

print(case.values())

for val in case.values():
    print(val)

case_copy: dict = case.copy() # creates a shallow copy
print(case_copy)
print("*" * 120)

clubs = top_5_football_clubs.copy() # creates a shallow copy
print(clubs)

top_5_football_clubs["EPL"][5] = "Aston Villa" # copies references so the copied dict is also affected
print(clubs)
