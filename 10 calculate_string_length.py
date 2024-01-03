def calculate_string_length(input_string):
    length = 0

    if input_string:
        for char in input_string:
            length += 1
    else:
        print("The input string is empty.")

    return length

user_input = input("Enter a string: ")
result = calculate_string_length(user_input)
print("Length of the string:", result)
