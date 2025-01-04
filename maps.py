atlas = map(lambda x: x ** 2, [1, 2, 4, 6, 8])
print(atlas)

for obj in atlas:
    print(obj)


power = map(str.upper, "i am")
for obj in power:
    print(obj, end="")
