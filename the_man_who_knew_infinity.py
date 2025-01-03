def odd_infinite():
    next_odd = 1
    while True:
        yield next_odd
        next_odd += 2


odds = odd_infinite()

for _ in range(100):
    print(next(odds))
