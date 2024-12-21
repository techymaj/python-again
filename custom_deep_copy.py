def deepcopy_custom(dictionary: dict) -> dict:
    """
    Performs a deep copy of the dictionary

    :param dictionary: The dictionary to deeply copy
    :return: A new object reference to the dictionary
    """

    new_dict = {
        key: value for key, value in dictionary.items()
    }

    return new_dict


animals = {
    "lion": 20,
    "tigers": 11,
    "cheetahs": 3,
}

new_animals = deepcopy_custom(animals)
animals["lion"] = 33

print(f"From original dictionary: {animals}")
print(f"The deep copy: {new_animals}")
