# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
split_text = text.split()
join_text = "".join(split_text)
lower_case_text = join_text.casefold()
remove_alnum = "".join(
    c for c in lower_case_text if c.isalnum() is True
)

for character in remove_alnum:
    if character not in word_count:
        # key doesn't exist, create key & set default count to 1
        word_count.setdefault(character, 1)
    else:
        # key exists, update count
        update = word_count.get(character) + 1
        word_count.update({character: update})


# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
