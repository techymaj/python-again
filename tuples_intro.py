albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,),
    ("Bad Company", "Bad Company", 1974,),
    ("Nightflight", "Budgie", 1981,),
    ("More Mayhem", "Emilia May", 2011,),
    ("Ride the Lightning", "Metallica", 1984,),
]

for number, album in enumerate(albums):
    title, artist, year = (tag.upper() if isinstance(tag, str) else tag for tag in album)
    print(
        f"Album: #{number + 1}\n "
        f"Artist: {artist}\n "
        f"Title: {title}\n "
        f"Year: {year}\n"
    )
