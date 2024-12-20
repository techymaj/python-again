def factorial(n: int) -> int:
    """
    Generates the factorial of a number.

    :params n: The number whose factorial to generate.
    :returns: The factorial of n as an `int`
    """

    if n == 0:
        return 1

    if n < 0:
        return -1

    fact = 1
    for i in range(n):
        print(f"{i} * {fact * (i + 1)}")
        fact = fact * (i + 1)

    return fact


factored = factorial(35)
print(factored)
