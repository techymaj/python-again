with open("/Users/mbuto/Downloads/Jabberwocky.txt", "r") as jabber:
    data_readlines = jabber.readlines() # reads all lines including new-lines

    jabber.seek(0) # reset pointer
    data_readline = jabber.readline() # reads the first line including new-lines

    jabber.seek(0) # reset pointer
    data_read = jabber.read() # reads the entire file

    print(data_readlines)
    print("*" * 120)
    print(data_readline)
    print("*" * 120)
    print(data_read)
    print("*" * 120)
