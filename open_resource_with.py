with open("/Users/mbuto/Downloads/Jabberwocky.txt", "r") as jabber:
    data_readline = jabber.readline().rstrip() # reads the first line
print(data_readline)


chars = "'Twas ev"
no_chars = data_readline.strip(chars) # strip any leading or trailing characters that are in chars

print(no_chars)
