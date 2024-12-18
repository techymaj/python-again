albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

while True:
    for index, album in enumerate(albums):
        title, artist, year, songs = album
        print(f"{index + 1} - {title}")
        if index == len(albums) - 1:
            option = int(input("Choose an album: ")) - 1
            tracks = albums[option][3]
            print(f"\nChosen album: {title}")
            for track, record in enumerate(tracks):
                track_number, song_title = record
                print(track_number, song_title, sep=" - ")
                if track == len(tracks) - 1:
                    play = int(input("Choose a song to play: ")) - 1
                    playing = tracks[play][1]
                    print(f"\nPlaying: {playing}")
    print("-" * 50)
    another_song = input("Play another song? Y/n ")
    if another_song == "Y".casefold():
        continue
    else:
        break
