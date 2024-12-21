wild_animals:set[str] = {"Horse", "Tiger", "Lion", "Panther", "Snake"}
farm_animals:set[str | int] = {"Cow", "Sheep", "Horse", "Dog", "Cat", 2}

intersection = wild_animals & farm_animals
print(intersection)

all_together = wild_animals | farm_animals
print(all_together)

wild_animals.remove("Snake")
wild_animals.add("Buffalo")

print(wild_animals)
print(farm_animals)

# lists are not hashable in Python.
# Hashability is a requirement for elements in a set
# farm_animals.add(["3.2"])

farm_animals.add((1, 2, 3))  # tuples are hashable, so they pass
print(farm_animals)


new_set_comprehension = {
    unique_value for unique_value
    in wild_animals | farm_animals
    if isinstance(unique_value, str)
    or isinstance(unique_value, tuple)
}

print(new_set_comprehension)

new_set_comprehension.discard("Reindeer") # remove but raise no error if not in set
print(new_set_comprehension)

new_set_comprehension.discard("Horse") # remove but raise no error if not in set
print(new_set_comprehension)

print()
print(f"Wild animals: {wild_animals}")
print(f"Farm animals: {farm_animals}")

# from farm animals, remove any elements present in wild animals
# same as farm_animals.difference(wild_animals)
everything_else = farm_animals - wild_animals
print(f"The difference: {everything_else}")

# set_one.intersection(set_two) --- set_one & set_two
# set_one.union(set_two) --- set_one | set_two
# set_one.difference(set_two) --- set_one - set_two
# set_one.symmetric_difference(set_two) --- set_one ^ set_two

print()

# symmetric difference is the opposite of the intersection of 2 or more sets
symm_diff = farm_animals.symmetric_difference(wild_animals)
print(symm_diff)
print("OR")
symm_fancy_diff = wild_animals ^ farm_animals
print(symm_fancy_diff)


animals = {"cow", "chicken", "cow", "goat"} # dict is k:v
print(animals)

print()

set_one = {1, 2, 3, 4, 5}
set_two = {5, 4, 3, 2, 1}

if set_two == set_one:
    print("Equal, yes")
else:
    print("Not equal")


if set_two is set_one:
    print("Same, yes")
else:
    print("But different")

print()


ns = set("12345")
print(ns)
