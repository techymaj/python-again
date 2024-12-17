menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for i in range(len(meal) - 1, -1, -1):
        if meal[i] == "spam":
            del meal[i]
    print(meal)

print("*" * 80)

# syntax: [expression for item in iterable if condition]
# apply this expression for each item in the iterable that matches the condition
for meal in menu:
    filtered_meal = [item for item in meal if item != "spam"]
    print(filtered_meal)
