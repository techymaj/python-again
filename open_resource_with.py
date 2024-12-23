with open("/Users/mbuto/Downloads/Jabberwocky.txt", "r") as jabber:
    data_readline = jabber.readline().rstrip() # reads the first line
print(data_readline)


chars = "'Twas ev"
no_chars = data_readline.strip(chars) # strip any leading or trailing characters that are in chars

print(no_chars)
print(80 * "*")

# twas_removed = data_readline.lstrip("'swaT")
# toves_removed = data_readline.rstrip("vesto")

twas_removed = data_readline.removeprefix("'swaT")
toves_removed = data_readline.removesuffix("vesto")

print(twas_removed)
print(toves_removed)
