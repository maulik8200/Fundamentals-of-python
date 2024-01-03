def count_characters(string):
    char_frequency = {}

    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    for char, frequency in char_frequency.items():
        print(f"Character '{char}' occurs {frequency} times in the string.")

input_string = input("Enter a string: ")
count_characters(input_string)
