import sys


def my_range(n: int):
    """A simple generator"""
    start = 0
    while start < n:
        yield start
        start += 1


# big_range = range(5) # 48 bytes
big_range = my_range(5) # 192 bytes. why?
print(f"Big range is: {sys.getsizeof(big_range)}")

# create a list containing all the values in range
values = [val for val in big_range]
# print(values)
print(f"List size is: {sys.getsizeof(values)}")

# big_list = []
# for val in big_range:
#     big_list.append(val)
#
# # print(big_list)
# print(f"Size of list: {sys.getsizeof(big_list)}")

print(big_range)
print(values)
