
country_codes: dict[str, int] = {
    "Tanzania": 255,
    "Rwanda": 250,
    "Burundi": 257,
    "South Sudan": 211,
    "Somalia": 252,
}

uganda = country_codes.setdefault("uganda", 256)
print(f"Country code: {uganda}")

print(country_codes)

kenya = country_codes.setdefault("kenya", 250)
print(f"Country code: {kenya}")

print(country_codes)
