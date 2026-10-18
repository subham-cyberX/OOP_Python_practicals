
digit_names = {
    '0': 'ZERO',
    '1': 'ONE',
    '2': 'TWO',
    '3': 'THREE',
    '4': 'FOUR',
    '5': 'FIVE',
    '6': 'SIX',
    '7': 'SEVEN',
    '8': 'EIGHT',
    '9': 'NINE'
}

ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")

elif ch.isalpha():
    print("The character is a letter.")

    if ch.isupper():
        print("It is an uppercase letter.")
    else:
        print("It is a lowercase letter.")

elif ch.isdigit():
    print("The character is a numeric digit.")
    if ch in digit_names:
        print("Digit name:", digit_names[ch])
    else:
        print("Digit name is not available.")

else:
    print("The character is a special character.")
