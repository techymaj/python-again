from color_codes import *

numbers = 1, 2, 3, 4, 5

print(numbers)
print(*numbers)

print_in_color("I am what I am", BLUE, BOLD,)
print_in_color("I do what I want", MAGENTA, BOLD, REVERSE,)
print_in_color("But I can't hide", CYAN, BOLD, REVERSE,)
print_in_color("And I won't go", YELLOW, BOLD, REVERSE,)
print_in_color("I won't leave", RED, BOLD, REVERSE)
print_in_color("I can't breathe", WHITE, BOLD, REVERSE)
print_in_color("Until you're resting here with me", CYAN, BOLD, REVERSE)
print_in_color("Well, what about me?", BG_GREEN, BLACK, ITALIC, DIM)
