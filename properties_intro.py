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
    radius_prop = property(fget=get_radius, fset=set_radius, fdel=del_radius, doc="The radius of the circle")

# Usage
circle = Circle(5)
print(circle.radius_prop)  # Calls get_radius()
circle.radius_prop = 10    # Calls set_radius()
del circle.radius_prop      # Calls del_radius()
