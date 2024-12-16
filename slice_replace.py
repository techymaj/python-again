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
