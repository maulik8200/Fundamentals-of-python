def count_substring_occurrences(main_string, substring):
    count = 0
    
    if substring != "":
        for i in range(len(main_string)):
            if main_string[i:i+len(substring)] == substring:
                count += 1
    
    return count

main_string = "ababababab"
substring = "ab"

result = count_substring_occurrences(main_string, substring)
print(f"The substring '{substring}' appears {result} times in the main string.")
