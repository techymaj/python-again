from color_codes import *

numbers = 1, 2, 3, 4, 5

print(numbers)
print(*numbers)

print_ic("I am what I am", BLUE, BOLD, )
print_ic("I do what I want", MAGENTA, BOLD, REVERSE, )
print_ic("But I can't hide", CYAN, BOLD, REVERSE, )
print_ic("And I won't go", YELLOW, BOLD, REVERSE, )
print_ic("I won't leave", RED, BOLD, REVERSE)
print_ic("I can't breathe", WHITE, BOLD, REVERSE)
print_ic("Until you're resting here with me", CYAN, BOLD, REVERSE)
print_ic("Well, what about me?", BG_GREEN, BLACK, ITALIC, DIM)
