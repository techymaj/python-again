number_list = [1, 2, 3, 4, 5, 6, 7, 8, "9", "x"]

starter = 0
for num in number_list:
    try:
        if int(num).is_integer():
            starter += int(num)
        else:
            continue
    except ValueError as not_a_number:
        print(f"{not_a_number} skipped")
else:
    print(starter)
    print(f"shorter? {'Invalid' if num == 'x' else sum(number_list)}")


elements = [None, None, ""]

if any(elements):
    copy_data = elements.copy()
    print("Copy successful")
    print(f"copied data: {copy_data}")
else:
    print("That's an empty list")
