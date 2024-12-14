for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}"
          .format(i, i ** 2, i ** 3))
# ** exponent operator

print("Pi is app: {0:12}".format(22 / 7)) # width of 12 no cut off
print("Pi is app: {0:12f}".format(22 / 7)) # width of 12 with cut off
print("Pi is app: {0:12.50f}".format(22 / 7)) # width of 12 with 50 dec places. precision is more important than width
print("Pi is app: {0:52.50f}".format(22 / 7)) # width of 52 with 50 dec places
print("Pi is app: {0:62.50f}".format(22 / 7)) # width of 62 with 50 dec places
print("Pi is app: {0:72.50f}".format(22 / 7)) # width of 72 with 50 dec places
