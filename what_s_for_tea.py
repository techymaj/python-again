from color_codes import *

pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}

# recipes_list = [recipe for recipe, collection in recipes.items()]
#
# print("Choose your recipe: ")
# print("-" * 25)
# for index, recipe in enumerate(recipes_list):
#     print(index + 1, recipe, sep=" - ")

# dictionary comprehension
display_dict = {
    str(index + 1): meal for index, meal in enumerate(recipes)
}
print_ic(display_dict, BLUE, REVERSE)

meals_list: list = []
for keys, meals in recipes.items():
    meals_list.append(
        (meal for meal in meals)
    )

print(meals_list)

for i in meals_list:
    print(list(i))  # Consume the generator object

print("*" * 160)

new_meals_list: list[list[str]] = [
    [meal for meal in meals] for _, meals in recipes.items()
]

for nml in new_meals_list:
    print(nml)
