a = b = c = d = e = f = 781227
print(c)

*x, y, z = 1, 2, 3, 4, 5
print(*x, y, z, sep=", ")

names = ["maria", "jax", "brian"]
m, j, br = names
print(m, j, br, sep=", ")

# names.append("king")
# print(names)
# m, j, br = names # error: too many values to unpack (expected 3)
# print(m, j, br, sep=", ")

# each time around the loop, i and character are unpacked from the tuple
# that enumerate creates
for i, character in enumerate("abcdefg"):
    print(i, character)
print("-" * 80)
for t in enumerate("abcdefg"):
    i, character = t # same as above, just longer
    print(i, character)

for t in enumerate("abcdefg"):
    print(t)
