from color_codes import *

def print_in_color(effect: str, text: str, reset: str = RESET) -> None:
    """
    Prints a given text in the color specified by `effect`

    :param effect: The color to print in
    :param text: The text to apply the color to
    :param reset: Resets the effect to the terminal default
    """
    print(f"{effect}", f"{text}", f"{reset}")

print_in_color(BLUE, "Blue is the warmest color")
print("What about ism....")
print_in_color(RED, "RED DAWN!!!")
print_in_color(CYAN, "Kiwaani")
