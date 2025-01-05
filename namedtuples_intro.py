from collections import namedtuple

Adult = namedtuple(
    "Adult",
    "name, age, sex"
)

people = [
    Adult("John", 33, "M"),
    Adult("Jane", 20, "F"),
    Adult("Mike", 31, "M"),
]

for person in people:
    print(
        f"Name: {person.name}",
        f"Age: {person.age}",
        f"Sex: {person.sex}",
        sep="\n"
    )
    print("*" * 80)

updated_person_1 = people[0]._replace(sex="Male")
print(updated_person_1)
