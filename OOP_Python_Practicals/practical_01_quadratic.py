# The equation is:
# \[
# ax^2+bx+c=0
# \]

import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("This is not a quadratic equation.")
else:
    discriminant = b**2 - 4*a*c

    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

    print("First root:", root1)
    print("Second root:", root2)
