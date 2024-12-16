import random

random_number = random.randint(0, 10)
print(random_number)

rand_float = round(random.random(), 2)
print(rand_float)  # Output is between 0.0 and 1.0

# Generate a random float between two values
rand_float = random.uniform(1.5, 5.5)
print(rand_float)

print(2 ** 10)
