from math import radians, cos
import turtle
import random

colors = ["Magenta", "Cyan", "Orange", "Yellow", "Purple", "Turquoise", "Fuchsia", "Green", "Blue", "Coral"]


def draw_squares(length, angle) -> None:
    """
    Draw a square of length, `length`
    Args:
        length: The length of the square
        angle: The change in direction

    Returns: None

    """
    for side in range(4):
        turtle.forward(length)
        turtle.right(angle)


def encircled_square(length: int) -> None:
    """
    Draws a square of length, `length`, then encloses it in a circle
    Args:
        length:

    Returns: Nothing

    """
    draw_squares(length, 90)
    angle = radians(45)
    radius = length * cos(angle)
    turtle.right(135)
    turtle.circle(radius)
    turtle.left(135)
    print(dir())
    print(locals())  # shows the namespace dictionary


# encircled_square(150)
turtle.speed("fast")
turtle.Screen().tracer(0)  # Disable turtle animation
for s in range(72):
    encircled_square(100)
    turtle.left(5)
    turtle.color(colors[random.randint(0, 9)])

turtle.Screen().update()
turtle.done()
encircled_square(4)
# print(dir())
#
# g = globals()
# print(g["draw_squares"])
#
# print()
# print(dir(__builtins__))
# print("len" in dir(__builtins__))
