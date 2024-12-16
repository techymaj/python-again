options = [
    "Arsenal",
    "Chelsea",
    "Manchester United",
    "Manchester City",
    "Liverpool",
    "Aston Villa",
    "Real Madrid",
    "Ipswich Town"]

for i, option in enumerate(options):
    print(f"{i + 1} - {option}")

print("\nWhich of the above clubs is not in the EPL? ")

while True:
    selected = int(input()) - 1
    if selected == 6:
        print(f"Correct. The answer is {options[selected]}")
        break
    else:
        print(f"It's not {options[selected]}. Try again")
