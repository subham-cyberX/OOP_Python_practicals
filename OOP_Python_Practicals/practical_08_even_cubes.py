
# Input a list containing different types of elements
items = eval(input("Enter a list: "))

# a. Using for loop
cubes_loop = []

for item in items:
    if type(item) is int and item % 2 == 0:
        cubes_loop.append(item ** 3)

print("Cubes using for loop:", cubes_loop)

# b. Using list comprehension
cubes_comprehension = [
    item ** 3 for item in items
    if type(item) is int and item % 2 == 0
]

print("Cubes using list comprehension:", cubes_comprehension)
