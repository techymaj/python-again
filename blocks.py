age = 18

if 18 > age > 10:
    pass

theDay = "Monday"
monday = theDay # Python does not guarantee that strings are always stored at the same memory location
# theDay = "Friday"
# print(monday)
temperature = 42
sunny = False

if theDay is monday and temperature > 40 and not sunny: # is not negates is
    print("Don't go swimming")

if theDay == monday and temperature > 40 and not sunny: # == preferred
    print("Don't go swimming")
