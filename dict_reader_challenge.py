import csv
import json

data_to_read = "country_info.txt"

dicts = {}

with open(data_to_read, encoding="utf-8", newline="") as challenge:
    first_3 = ""
    for line in range(3):
        first_3 += challenge.readline()
    country_dialect = csv.Sniffer().sniff(first_3)
    challenge.seek(0)

    reader = csv.DictReader(challenge, dialect=country_dialect)

    for row in reader:
        if "Country" in row:
            cty = row["Country"]
        dicts.update({cty: row})


print(dicts)

with open("country.json", "w", encoding="Utf-8") as cty_json:
    json.dump(dicts, cty_json)
