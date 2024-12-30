# Example 1: Creating a bytearray from an iterable of integers
data = [65, 66, 67, 68]  # ASCII values for 'A', 'B', 'C', 'D'
byte_array = bytearray(data)

print(byte_array)  # Output: bytearray(b'ABCD')
print(type(byte_array))  # Output: <class 'bytearray'>

# Example 2: Modifying a bytearray
byte_array[1] = 69  # Change 'B' to 'E' (ASCII 69)
print(byte_array)  # Output: bytearray(b'AECD')

# Example 3: Creating a bytearray from a string
string = "Hello"
encoded_array = bytearray(string, "utf-8")  # Specify encoding

print(encoded_array)  # Output: bytearray(b'Hello')

# Example 4: Appending to a bytearray
encoded_array.append(33)  # Add '!' (ASCII 33)
print(encoded_array)  # Output: bytearray(b'Hello!')
