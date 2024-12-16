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
for item in data:
    if "Shrub" in item:
        shrubs.append(item)
    elif "Flower" in item:
        flowers.append(item)
else:
    data_copy = data[:] # backup data
    clean_data = []
    for item in data:
        if "Flower" in item or "Shrub" in item:
            splits = item.split(" - ")
            clean_data.append(splits[0])

    print(clean_data)
