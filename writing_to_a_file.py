with open("write_to_me.txt", "w") as lets:
    lets.write("To God be the glory")


with open("write_to_me.txt", "a") as text:
    two = 2
    text.write(f"{two}")

with open("write_to_me.txt", "a") as text:
    print(f"\n{12}", file=text)


with open("write_to_me.txt") as text:
    print(text.read())
