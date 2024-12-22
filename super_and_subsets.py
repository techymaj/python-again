birds = {
    "stirling",
    "geese",
    "raven",
    "dove"
}

animals = {
    "lion",
    "tiger",
    "geese",
    "raven",
    "dove",
    "stirling",
    "leopard"
}

nothing = {
    "peacock",
    "chicken",
    "duck"
}

print(f"birds is a subset of animals: {birds.issubset(animals)}")
print(f"birds is a proper subset of animals: {birds < animals}")
print()
print(f"animals is a superset of birds: {animals >= birds}")
print(f"animals is a proper superset of birds: {animals > birds}")

print()
print(animals.isdisjoint(nothing))


odd = {1, 3, 5}
even = {0, 2, 4}

even ^= odd

print(even)  # what will be the output
