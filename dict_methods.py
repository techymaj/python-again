import copy

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

case_copy: dict = case.copy()  # creates a shallow copy
print(case_copy)
print("*" * 120)

clubs = top_5_football_clubs.copy()  # creates a shallow copy
print(top_5_football_clubs)

top_5_football_clubs["EPL"][5] = "Aston Villa"  # copies references so the copied dict is also affected
print(clubs)

print()

# shallow copy demo. nested gives you references
animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": {
        1: "cuddly"
    },
}

# deep copy demo
animals_deep = {
    "lion": "scary",
    "elephant": "big",
    "teddy": {
        1: "cuddly"
    },
}

# shallow
things = animals.copy()
# animals["teddy"][1] = "toy"
# print(things["teddy"][1])
# print(animals["teddy"][1])

# deep. complete independence between animals_deep & into_the_deep
# into_the_deep = copy.deepcopy(animals_deep)
# animals_deep["teddy"][1] = "cute & cuddly"
# print(animals_deep)
# print(into_the_deep)

# at level 1, copy() gives you a "deep copy" unless the value is mutable
wild_animals = {
    "lion": ["scary"],  # I am mutable, share me
    "elephant": "big",
    "cheetah": "fast",
}

copied = wild_animals.copy()
wild_animals["lion"].append("king of the jungle")
wild_animals["cheetah"] = "super fast"

print(wild_animals)
print(copied)
