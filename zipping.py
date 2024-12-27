albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
keys = ["album", "artist", "year"]

# zipped = zip(*albums, keys)
#
# for row in zipped:
#     print(row)

for row in albums:
    zipped = zip(keys, row,)
    # zipped_print = [zipper for zipper in zipped]
    # print(zipped_print)
    print(*zipped)
    # for thing in zipped:
    #     print(thing)
