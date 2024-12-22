
drinks = {
    "coke",
    "fanta",
    "pepsi",
    "dew",
}

liquor = {
    "gin",
    "vodka",
    "wine",
    "spirit",
    "coke",
}

brewing = {"whiskey", "scotch", "rum", "brandy"}

liquor |= brewing
# liquor.update(brewing) same same -> Update the set, adding elements from brewing.

print(liquor)

liquor -= brewing # Update the set, removing elements found in brewing.

print(liquor)

drinks &= liquor # Update the set, keeping only elements found in it and liquor.

print(drinks)

drinks ^= liquor # Update the set, keeping only elements found in either set, but not in both.

print(drinks)

print()

# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Update set1 using symmetric_difference_update
set1.symmetric_difference_update(set2)

# Print updated set1
print(set1)  # Output: {1, 2, 5, 6}
