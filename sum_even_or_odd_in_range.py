def sum_eo(n=0, t=""):
    """
    Generates the sum of even or odd numbers.

    :param n: The range of numbers to generate the sum from.
    :param t: Even or odd toggle.
    :return: The sum of either e(even) or o(odd) or -1 for invalid.
    """
    if t == "e":
        return sum((even for even in range(n) if even % 2 == 0))
    elif t == "o":
        return sum((odd for odd in range(n) if odd % 2 != 0))
    else:
        return -1


summed = sum_eo(11, 'e')
print(summed)
print("*" * 80)
# print(sum_eo.__doc__)
help(sum_eo)
print("*" * 80)
