top_5_football_clubs:dict[str, dict[int, str]] = {
    "EPL": {
        1: "Arsenal",
        2: "Liverpool",
        3: "Chelsea",
        4: "Nottingham Forest",
        5: "Manchester City",
    },
    "La Liga": {
        1: "Real Madrid",
        2: "Barcelona",
        3: "Atletico Madrid",
        4: "Valencia",
        5: "Sevilla",
    },
    "Serie A": {
        1: "Juventus",
        2: "AC Milan",
        3: "Inter Milan",
        4: "AS Roma",
        5: "Lazio",
    },
    "Bundesliga": {
        1: "Bayern Munich",
        2: "Borussia Dortmund",
        3: "Werder Bremen",
        4: "Schalke 04",
        5: "Bayer Leverkusen",
    },
    "Ligue 1": {
        1: "Paris Saint-Germain",
        2: "Monaco",
        3: "Lyon",
        4: "Marseille",
        5: "Saint-Etienne",
    },
}

if __name__ == "__main__":
    print(top_5_football_clubs["EPL"][1])  # Read value based on key

    new_comer: str = "Newcastle United"
    top_5_football_clubs["EPL"][5] = new_comer  # update key with new value

    print(top_5_football_clubs["EPL"].get(5))  # retrieve value based on key
    print(top_5_football_clubs["EPL"])

    ligue_1: dict[int, str] = top_5_football_clubs.get("Ligue 1")
    print(ligue_1)

    popped: str = ligue_1.pop(3)  # delete item and return the value
    print(popped)

    print(ligue_1)

    ligue_1.update({3: "Lyon"})  # create new entry

    print(ligue_1)
