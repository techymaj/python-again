from nested_indexing import albums

while True:
    print("***JUKEBOX***")
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
