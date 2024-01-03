def is_vowel(letter):
    letter = letter.lower()

    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return True
    else:
        return False

user_input = input("Enter a letter: ")

if len(user_input) == 1:
    if is_vowel(user_input):
        print(f"{user_input} is a vowel.")
    else:
        print(f"{user_input} is not a vowel.")
else:
    print("Please enter a single letter.")
