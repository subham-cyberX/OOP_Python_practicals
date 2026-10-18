
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half the values on separate lines
mid = len(t1) // 2

print("First half:", t1[:mid])
print("Second half:", t1[mid:])

# b. Create a tuple of even numbers
even_tuple = tuple(x for x in t1 if x % 2 == 0)
print("Even numbers tuple:", even_tuple)

# c. Concatenate t2 with t1
t2 = (11, 13, 15)
combined = t1 + t2
print("Concatenated tuple:", combined)

# d. Find maximum and minimum values
print("Maximum value:", max(combined))
print("Minimum value:", min(combined))
