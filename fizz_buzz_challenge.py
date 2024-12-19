def fizz_buzz(n: int) -> str:
    """
    Prints fizz, buzz or fizzbuzz depending on the value of n.

    :param n: The number to test
    :return: Returns a string
    """
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 5 == 0:
        return "buzz"
    elif n % 3 == 0:
        return "fizz"
    else:
        return str(n)


for i in range(1, 101):
    print(fizz_buzz(i))
