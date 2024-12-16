numbers = [5,4,3,2,1]
del numbers[-1]
numbers[0] = "a"
print(numbers)
numbers[0] = ["a"]
print(numbers)
numbers[:3] = ["a", "b", "c"]
print(f"sliced: {numbers}")

numbers[::] = []
print(numbers)

name = "Wilfried" # immutable. can't do much to it
numbers = [*name]
numbers.insert(5, "x")
print(numbers)
numbers.pop(5)
print(numbers)
numbers.pop(5)
print(numbers)


DATA = [2, 4, 101, 100, 123, 133, 144, 112, 133, 200, 201, 404, 500]

for data in DATA[:]: # enumerate over a copy
    if data not in range(140, 201):
        print(f"Removing {data}")
        DATA.remove(data)
else:
    print(DATA)

# using a list comprehension
# syntax: [expression for item in iterable if condition]
# apply this expression for each item in the iterable that matches the condition
DATA = [2, 4, 101, 100, 123, 133, 144, 112, 133, 200, 201, 404, 500]
DATA = [data + 1 for data in DATA if data in range(140, 201)]
print("Final DATA:", DATA)

my_awesome_list = [x for x in range(11) if x % 2 == 0 and x != 0]
print(my_awesome_list)

first_name = [character.upper() for character in "Wilfried"]
print(first_name)

lucky_numbers = ["even" if x % 2 == 0 else "odd" for x in range(11)]
print(lucky_numbers)

name = "wilfried".upper()
print(name)

# Filter backwards
DATA = [2, 4, 101, 100, 123, 133, 144, 112, 133, 200, 201, 404, 500]
for i in range(len(DATA) - 1, -1, -1):
    if DATA[i] not in range(140, 201):
        print(f"Removing {DATA[i]}")
        del DATA[i]
print(DATA)

DATA = [2, 4, 101, 100, 123, 133, 144, 112, 133, 200, 201, 404, 500]
top_index = len(DATA) - 1
for i, value in enumerate(reversed(DATA)):
    if value not in range(140, 201):
        print(f"Deleting: {value}")
        del DATA[top_index - i]
else:
    print(DATA)
