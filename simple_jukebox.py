from nested_indexing import albums

SONGS_LIST_INDEX = 3
CHOSEN_TRACK_INDEX = 1

def album_tracks(tracks):
    for track, (track_number, song_title) in enumerate(tracks):
        print(track_number, song_title, sep=" - ")
        if track == len(tracks) - 1:
            play = int(input("Choose a song to play: ")) - 1
            if play not in range(len(tracks)):
                print("Invalid choice - taking you back to album list")
                break
            else:
                playing = tracks[play][CHOSEN_TRACK_INDEX]
                print(f"\nNow playing: {playing}")


def now_playing():
    print("***JUKEBOX***")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1} - {title}")
        if index == len(albums) - 1:
            chosen_album = int(input("Choose an album: ")) - 1
            tracks = albums[chosen_album][SONGS_LIST_INDEX]
            print(f"\nChosen album: {title}")
            album_tracks(tracks)
    print("-" * 50)


while True:
    now_playing()
    another_song = input("Play another song? Y/n ")
    if another_song == "Y".casefold():
        continue
    else:
        break
