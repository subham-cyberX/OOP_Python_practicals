
import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2
        )

    def __str__(self):
        return f"Point2D({self.x}, {self.y})"


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2
        )

    def __str__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"


p1 = Point3D(1, 2, 3)
p2 = Point3D(4, 6, 3)

print("First point:", p1)
print("Second point:", p2)
print("Distance between points:", p1.distance(p2))
