class Circle:
    def __init__(self, radius):
        self._radius = radius  # Use a private attribute for internal storage

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    def del_radius(self):
        print("Radius deleted")
        del self._radius

    # Creating a property
    radius = property(get_radius, set_radius, del_radius, "The radius of the circle")

# Usage
circle = Circle(5)
print(circle.radius)  # Calls get_radius()
circle.radius = 10    # Calls set_radius()
del circle.radius      # Calls del_radius()
