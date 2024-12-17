import timeit

def sanitize_1():
    DATA = [data for data in range(100000000)]

    for data in DATA[:]:  # enumerate over a copy
        if data not in range(140, 201):
            # print(f"Removing {data}")
            DATA.remove(data)
    else:
        # print(DATA)
        pass

def sanitize_with_list_comprehension():
    # using a list comprehension
    # syntax: [expression for item in iterable if condition]
    # apply this expression for each item in the iterable that matches the condition
    DATA = [data for data in range(100000000)]
    DATA = [data + 1 for data in DATA if data in range(140, 201)]
    new_data = DATA


def sanitize_backwards_manually_with_range():
    # Filter backwards
    DATA = [data for data in range(100000000)]
    for i in range(len(DATA) - 1, -1, -1):
        if DATA[i] not in range(140, 201):
            # print(f"Removing {DATA[i]}")
            del DATA[i]
    # print(DATA)



def sanitize_backwards_with_enumerate_and_reversed():
    DATA = [data for data in range(100000000)]
    top_index = len(DATA) - 1
    for i, value in enumerate(reversed(DATA)):
        if value not in range(140, 201):
            # print(f"Deleting: {value}")
            del DATA[top_index - i]
    else:
        # print(DATA)
        pass
if __name__ == "__main__":
    print("Timing")

    a = timeit.timeit("sanitize_1()",
                      setup="from __main__ import sanitize_1",
                      number=1)
    print(f"{a:15.15f} - enumerate over a copy")

    b = timeit.timeit("sanitize_with_list_comprehension()",
                      setup="from __main__ import sanitize_with_list_comprehension",
                      number=1)
    print(f"{b:15.15f} - use a list comprehension")

    c = timeit.timeit("sanitize_backwards_manually_with_range()",
                      setup="from __main__ import sanitize_backwards_manually_with_range",
                      number=1)
    print(f"{c:15.15f} - filter backwards with range")

    d = timeit.timeit("sanitize_backwards_with_enumerate_and_reversed()",
                      setup="from __main__ import sanitize_backwards_with_enumerate_and_reversed",
                      number=1)
    print(f"{d:15.15f} - filter backwards with enumerate & reversed")
