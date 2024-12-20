def sum_numbers(*numbers: float) -> float:
    """
    Calculates the sum of all numbers passed as its arguments.

    :param numbers: A tuple of numbers.
    :return: The sum as a float.
    """

    added_up = sum(numbers)
    return added_up


added = sum_numbers(8, 20, 2)
print(added)
