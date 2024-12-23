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

entered_country = input("Enter country name: ").casefold()

if entered_country in countries_dict:
    _, city, _, _, _, _, _ = countries_dict[entered_country].values()
    print(f"{entered_country} exists. Its capital city is: {city}")
else:
    print("I've never heard of that country in my life")
