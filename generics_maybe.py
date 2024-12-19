def sum_of_floats(it: list[str]) -> float:
    """
    Sums up a list of strings that are numbers

    :param it: The list of strings to transform
    :return: A single float value that is the sum
    """
    appended = []
    for i in it:
        appended.append(int(i))
    return sum(appended)

# compiler will complain it's not ["5", "4", "3", "2", "1"]
# but still be able tu run the code. so not strict generics
sums = sum_of_floats([5, 4, 3, 2, 1])
print(sums)
