
text = input("Enter a string: ")

# a. Find frequency of a character
ch = input("Enter character to find frequency: ")
print("Frequency:", text.count(ch))

# b. Replace a character
old = input("Enter character to replace: ")
new = input("Enter replacement character: ")
print("After replacement:", text.replace(old, new))

# c. Remove first occurrence of a character
ch = input("Enter character to remove first occurrence: ")
print("After removing first occurrence:", text.replace(ch, "", 1))

# d. Remove all occurrences of a character
ch = input("Enter character to remove all occurrences: ")
print("After removing all occurrences:", text.replace(ch, ""))
