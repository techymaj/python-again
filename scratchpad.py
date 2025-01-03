a = 3
b = 2

print(f"a is {a}, b is {b}")

#  relies on the fact that the right hand is evaluated first
a, b = b, a

print(f"a is {a}, b is {b}")
