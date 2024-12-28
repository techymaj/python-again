# from array import array
#
# char_array = array('w', 'hello')
# print(char_array)  # Output: array('w', 'hello')

hexa = 0x54, 0x49, 0x4d
name = "".join(chr(h) for h in hexa)
print(name)

# equation = bytes((123, 121, 144, 255))
# equation = b'{y\x90\xff' # bytes literal
equation = b'\xcf\x80r\xc2\xb2' # bytes literal
print(equation) # byte object
print(type(equation))
print(len(equation))

for b in equation:
    print(b, end=", ")

print()

print(equation.decode("utf-8"))
