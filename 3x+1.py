choice = int(input("Pick a number: "))
recursion_depth = 0

def collatz_conjecture(pick: int) -> None:
    global recursion_depth
    recursion_depth = recursion_depth + 1
    if recursion_depth == 900:
        return
    if pick % 2 == 0:
        next_num = pick // 2
        print(f"{pick} is even. Next number is {next_num}")
    else:
        next_num = (pick * 3) + 1
        print(f"{pick} is odd. Next number is {next_num}")

    return collatz_conjecture(next_num)


collatz_conjecture(choice)
