class Animal:

    def __init__(self, name):
        self.age = 2
        self.name = name
        self.alive = True


    def how_old(self, age):
        pass

    def get_name(self) -> str:
        if self.age > 1:
            return self.name


dog = Animal("Rex")
print(f"{dog.name} is {'alive' if dog.alive else 'dead' }")
print(dog.get_name())
