# Python integers are arbitrary-precision and do not have a fixed bit-width
# You have to explicitly tell the interpreter that you are dealing with signed ints

two = 0b00000010

print(two)

inverted = 0b11111101
twos_complement = (inverted + 0b01) & 0xFF  # Ensure 8-bit result

# Convert to signed value
if twos_complement & 0b10000000:  # Check if MSB is 1
    twos_complement -= 0b100000000  # Subtract 2^8 to get the negative value

print(twos_complement)  # Should print -2
