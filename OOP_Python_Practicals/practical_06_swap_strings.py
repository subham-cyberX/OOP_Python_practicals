
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
n = int(input("Enter the number of characters to swap: "))

if n < 0 or n > len(str1) or n > len(str2):
    print("Invalid value of n.")
else:
    result1 = str2[:n] + str1[n:]
    result2 = str1[:n] + str2[n:]

    print("First string after swapping:", result1)
    print("Second string after swapping:", result2)
