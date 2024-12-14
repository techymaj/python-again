age = 30
print("My age is %d" %age)

years = "years"
months = "months"

print("My age is %d %s, %d %s" %(age, years, 6, months))

for i in range(1, 11):
    if i % 2 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        pass
