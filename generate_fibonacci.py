def fibonacci(n: int):
    start, next_number = 0, 1
    for i in range(n):
        yield start
        start, next_number = next_number, (next_number + start)


for num in fibonacci(10):
    print(num)
