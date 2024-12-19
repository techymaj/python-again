def multiply():
    """
    Multiplies 5 by 8 and prints the result.

    Returns:
        None
    """
    print(5 * 8)
    return None


multiplied = multiply()
print(multiplied)


def add():
    """
    Adds 4 and 2, and returns the result.

    Returns:
        int: The result of 4 * 2.
    """
    result = 4 * 2
    return result


added = add()
print(added)


def subtract(x, y):
    """
    Subtracts y from x and returns the result.

    Args:
        x (float): The number to be subtracted from.
        y (float): The number to subtract.

    Returns:
        float: The result of x - y.
    """
    result = x - y
    return result


subtracted = subtract(4.23, 2)
print(f"Subtracted: {subtracted:.2f}")


def divide(numerator=0, denominator=1):
    """
    Divides the numerator by the denominator and returns the result.

    Args:
        numerator (float, optional): The numerator. Defaults to 0.
        denominator (float, optional): The denominator. Defaults to 1.

    Returns:
        float: The result of numerator / denominator.
    """
    return numerator / denominator


divided = divide(denominator=7, numerator=22)
print(divided)

default_divide = divide()
print(default_divide)


def f(a_list):
    """
    Appends 1 to the provided list.

    Args:
        a_list (list): The list to be modified.
    """
    a_list.append(1)  # Modifies the original list in place


m = []
f(m)
print(f"append(1) {m}")


def f(a_list):
    """
    Creates a new list by adding 1 to the provided list and prints it.

    Args:
        a_list (list): The list to be used for creating a new list.
    """
    # because the + operation doesn't modify lists in place,
    # it always creates a new one.
    a_list = a_list + [1]  # Creates a new list, does NOT modify the original
    print(f"a_list = ... {a_list}")  # [1]


m = []
f(m)
print(m)  # []
