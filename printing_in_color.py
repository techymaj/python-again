from color_codes import *

def print_in_color(*effects: "A list of styles", text: str, reset: str = RESET) -> None:
    """
    Prints a given text in the color specified by `effect`.

    :param effects: A list of the various styles to apply. e.g
        `BLUE, BOLD, UNDERLINE`
    :param text: The text to apply the color to.
    :param reset: Resets the effect to the terminal default.
    """
    combined_effects = ''.join(effects)
    print(f"{combined_effects}", f"{text}", f"{reset}")

print_in_color(BLUE, text="Blue is the warmest color")
print("What about ism....")
print_in_color(RED, UNDERLINE, BOLD, text="RED DAWN!!!")
print_in_color(CYAN, text="Kiwaani")
