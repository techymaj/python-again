integers_entered = input("Enter three integers separated by a comma ',' ")

split_ints = integers_entered.split(",")
a, b, c = split_ints

print(int(a) + int(b) - int(c))
