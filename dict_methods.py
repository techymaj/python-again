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
print(f"Not so empty, now, are ya? {empty_case}")
