import sys
import math

# choice = int(input("Pick a number: "))
sys.setrecursionlimit(10000)
recursion_depth = 0

def collatz_conjecture(pick: float) -> None:
    global recursion_depth
    recursion_depth = recursion_depth + 1
    if recursion_depth == 9999:
        return
    if pick % 2 == 0:
        next_num = pick // 2
        print(f"{pick} is even. Next number is {next_num}")
    else:
        next_num = (pick * 3) + 1
        print(f"{pick} is odd. Next number is {next_num}")

    return collatz_conjecture(next_num)

ridiculous_number = math.pow(2, 2000)
print(ridiculous_number)
collatz_conjecture(ridiculous_number)
