
def find_occurrences(string, substring):
    indices = []

    if substring == "":
        return indices

    start = 0

    while True:
        index = string.find(substring, start)

        if index == -1:
            break

        indices.append(index)
        start = index + 1

    return indices if indices else -1


text = input("Enter the first string: ")
sub = input("Enter the second string: ")

result = find_occurrences(text, sub)
print("Result:", result)
