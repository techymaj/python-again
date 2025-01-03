def fibonacci(n: int):
    start = 0
    next_number = 1
    for i in range(n):
        yield start
        start, next_number = next_number, (next_number + start)


for num in fibonacci(10):
    print(num)
