
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
        return f"Point({self.x}, {self.y})"


p1 = Point2D(2, 3)
p2 = Point2D(5, 7)

print("First point:", p1)
print("Second point:", p2)
print("Distance between points:", p1.distance(p2))
