import turtle
import random

colors = ["Green", "Red", "Blue"]

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

for s in range(72):
    draw_squares(100, 90)
    turtle.left(5)
    turtle.color(colors[random.randint(0, 2)])

turtle.done()
