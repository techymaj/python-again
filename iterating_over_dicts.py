from dict_intro import top_5_football_clubs

for key, teams in top_5_football_clubs.items():
    for k, v in teams.items():
        print(f"{k}:" f"{v}")
    print()

# .items in python3 is more efficient
