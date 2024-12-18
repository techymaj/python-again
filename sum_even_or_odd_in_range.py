def sum_eo(n=0, t=""):
    if t == "e":
        return sum((even for even in range(n) if even % 2 == 0))
    elif t == "o":
        return sum((odd for odd in range(n) if odd % 2 != 0))
    else:
        return -1

summed = sum_eo(11, 'e')
print(summed)
