def multiply():
    print(5 * 8)
    return None


multiplied = multiply()
print(multiplied)


def add():
    result = 4 * 2
    return result


added = add()
print(added)


def subtract(x, y):
    result = x - y
    return result


subtracted = subtract(4.23, 2)
print(f"Subtracted: {subtracted:.2f}")


def divide(numerator=0, denominator=1):
    return numerator / denominator


divided = divide(denominator=7, numerator=22, )
print(divided)

default_divide = divide()
print(default_divide)


def f(a_list):
    a_list.append(1)  # Modifies the original list in place


m = []
f(m)
print(f"append(1) {m}")


def f(a_list):
    # because the + operation doesn't modify lists in place,
    # it always creates a new one.
    a_list = a_list + [1]  # Creates a new list, does NOT modify the original
    print(f"a_list = ... {a_list}")  # [1]


m = []
f(m)
print(m)  # []
