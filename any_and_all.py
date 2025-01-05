well = [1, 22, 3, 4, ""]

print(
    any(x == 2 for x in well)
)

print(
    all(isinstance(x, int) for x in well)
)

spring = "i am a well spring"
for char in spring:
    print(char)

print(
    any(x.isupper() for x in spring)
)
