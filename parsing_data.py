from color_codes import print_ic, BLUE, MAGENTA, RED

filename = "country_info.txt"

with open(filename) as country_info:
    list_to_parse = []
    for row in country_info:
        stripped = row.strip()
        splits = stripped.split("|")
        list_to_parse.append(splits)

dict_keys = dict.fromkeys(list_to_parse[0])
countries_dict = {}

for value in list_to_parse[1:]:
    country, capital, cc, cc3, iac, timezone, currency = value
    dict_keys["Country"] = country.casefold()
    dict_keys["Capital"] = capital
    dict_keys["CC"] = cc
    dict_keys["CC3"] = cc3
    dict_keys["IAC"] = iac
    dict_keys["TimeZone"] = timezone
    dict_keys["Currency"] = currency

    country_dict = {
        k: v for k, v in dict_keys.items()
    }

    countries_dict.update({country.casefold(): country_dict})


while True:
    entered_country = input("Enter country name, (Qq) to exit: ").casefold()

    if entered_country == "Q".casefold(): break

    if entered_country in countries_dict:
        _, city, _, _, _, _, _ = countries_dict[entered_country].values()
        print_ic(f"{entered_country.upper()}", BLUE)
        print("\texists. Its capital city is:", end="")
        print_ic(f"{city}\n", MAGENTA)
    else:
        print_ic("I've never heard of that country in my life\n", RED)
