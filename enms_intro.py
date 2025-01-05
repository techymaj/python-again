from enum import Enum

class Color(Enum):
    RED = 1 # auto() to automatically assign values
    GREEN = 2
    BLUE = 1 # Alias for RED. values must be unique otherwise it's an alias


for color in Color:
    print(color)
