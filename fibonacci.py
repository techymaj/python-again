def fibonacci_sequence(n: int) -> list[int]:
    """
    Generate a fibonacci sequence up to `Fn-1`. n should be positive.

    Fibonacci sequence is a sequence in which each number is the sum of
    the two numbers that precede it.

    :param n: The number of fibonacci numbers to generate.
    :return: A list of fibonacci numbers.
    """

    start = 0
    next_number = 1
    fib = []
    for index in range(n):
        fib.append(start)
        start, next_number = next_number, start + next_number
    return fib

seq = fibonacci_sequence(36)
print(seq)
