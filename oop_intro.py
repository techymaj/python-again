class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = True


dog = Animal("Rex")
print(f"{dog.name} is {'alive' if dog.alive else 'dead' }")
