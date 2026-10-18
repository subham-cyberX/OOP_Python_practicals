
from collections import Counter

# Read the file
with open("input.txt", "r") as file:
    text = file.read()

# a. Count characters, words and lines
characters = len(text)
words = text.split()
lines = text.splitlines()

print("Total characters:", characters)
print("Total words:", len(words))
print("Total lines:", len(lines))

# b. Frequency of each character
frequency = Counter(text)

print("\nCharacter frequency:")
for char, count in sorted(frequency.items()):
    if char == "\n":
        print("Newline:", count)
    elif char == " ":
        print("Space:", count)
    else:
        print(repr(char) + ":", count)

# c. Print words in reverse order
print("\nWords in reverse order:")
print(" ".join(words[::-1]))

# d. Copy even and odd lines into separate files
with open("input.txt", "r") as file:
    all_lines = file.readlines()

with open("File1", "w") as even_file, \
     open("File2", "w") as odd_file:

    for line_number, line in enumerate(all_lines, start=1):
        if line_number % 2 == 0:
            even_file.write(line)
        else:
            odd_file.write(line)

print("\nEven lines copied to File1.")
print("Odd lines copied to File2.")
