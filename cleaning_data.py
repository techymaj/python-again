data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for plant in data:
    if "Shrub" in plant:
        shrubs.append(plant)
    elif "Flower" in plant:
        flowers.append(plant)
else:
    data_copy = data[:] # backup data
    clean_data = []
    for plant in data:
        if "Flower" in plant or "Shrub" in plant:
            splits = plant.split(" - ")
            clean_data.append(splits[0])

    print(clean_data)
