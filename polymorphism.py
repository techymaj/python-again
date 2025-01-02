from typing import override


class Thing:
    @staticmethod
    def move():
        print("Move")


class Dog(Thing):
    @staticmethod
    @override
    def move():
        print("Run")


class Plant(Thing):
    @staticmethod
    @override
    def move():
        print("Weave")


rex = Dog
rex.move()

rose = Plant
rose.move()
