from typing import override


class Species:
    @staticmethod
    def species():
        print("Is a species")


class Animal:

    @staticmethod
    def walk():
        print("Animals walk")


class Dog(Animal, Species):

    def __init__(self, name):
        self._name = name

    @override
    def walk(self):
        # self.walk()  # recursion error. method calling itself
        # Animal.walk()
        super(Dog, self).walk()  # calling super methods
        super().walk()  # calling super methods. preferred
        print(f"{self._name} walks")

    def eat(self, speed, style):
        print(f"{self._name} eats very {speed} {style}")


dog = Dog("Rex")
dog.walk()
dog.species()
dog.eat("fast", "chewing")
