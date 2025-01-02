class Animal:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        pass

    @name.setter
    def name(self, value):
        self._name = value

    @name.getter
    def name(self):
        return self._name


dog = Animal("Rex")
dog.name = "Simba"
print(dog.name)
