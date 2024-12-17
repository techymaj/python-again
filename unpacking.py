a = b = c = d = e = f = 781227
print(c)

*x, y, z = 1, 2, 3, 4, 5
print(*x, y, z, sep=", ")

names = ["maria", "jax", "brian"]
m, j, br = names
print(m, j, br, sep=", ")

names.append("king")
print(names)
m, j, br = names # error: too many values to unpack (expected 3)
print(m, j, br, sep=", ")
