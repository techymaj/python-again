with open("write_to_me.txt", "w") as lets:
    lets.write("To God be the glory")


with open("write_to_me.txt") as text:
    print(text.read(6))
