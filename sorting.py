even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

# list.extend() does not return a new list. it returns None
even.extend(odd)
# combined = even.copy()
combined = even[:]
print(combined)

combined.sort(reverse=True)
print(combined)

print(combined is even)
