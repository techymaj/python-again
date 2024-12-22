jabber = open("/Users/mbuto/Downloads/Jabberwocky.txt", "r")

for line in jabber:
    stripped = line.strip()
    print(stripped)

jabber.close()  # you can run out of file handles if you don't close
