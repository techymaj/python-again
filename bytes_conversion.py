# names = ["Alice\n Ama\n Wilfried\n Giselle\n Jehoshaphat"]
# bytes_conversion = bytes(names[0], "utf-8")
#
# print(bytes_conversion, type(bytes_conversion))
#
#
# for name in names:
#     print(name)

numbers = [1 , 2, 43, 244, 255]
byte_conversion = bytes(numbers)

print(byte_conversion, type(byte_conversion))

for num in byte_conversion:
    print(num)
