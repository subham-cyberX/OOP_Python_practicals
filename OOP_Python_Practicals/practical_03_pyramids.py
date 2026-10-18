
n = int(input("Enter the number of rows: "))

print("\nPyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("\nReverse Pyramid:")
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
