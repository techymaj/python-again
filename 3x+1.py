import math

# Iterative implementation of the Collatz Conjecture
def collatz_conjecture_iterative(start: float) -> None:
    recursion_depth = 0
    pick = start

    while recursion_depth < 1100:  # Limit iterations to avoid infinite loops
        recursion_depth += 1
        if pick % 2 == 0:
            next_num = pick // 2
            print(f"{pick} is even. Next number is {next_num}")
        else:
            next_num = (pick * 3) + 1
            print(f"{pick} is odd. Next number is {next_num}")

        pick = next_num

        # If we reach 1, stop the loop (Collatz conjecture assumption)
        if pick == 1:
            print(f"Collatz sequence completed in {recursion_depth} steps.")
            break


for number in range(1024):
    ridiculous_number = math.pow(2, number)
    print("*" * 80)
    print(f"Computing for 2 to the power {number}")
    collatz_conjecture_iterative(ridiculous_number)
