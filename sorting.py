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

pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram) # Uppercase and spaces sort first
print(letters)

sentence = "Majaliwa M. Wilfried"
sorted_pangram = sorted(pangram)

splits = sorted_pangram
del splits[:8]
print(splits)
# for word in splits:
#     for letter in word:
#         print(letter)

names = ["Jax",
         "Maria",
         "brian",
         "Calisto",
         "Ganymede"]

names.sort(key=str.casefold)
print(names)
