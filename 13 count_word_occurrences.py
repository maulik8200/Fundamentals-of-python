def count_word_occurrences(sentence):
    words = sentence.split()

    word_counts = {}

    for word in words:
        cleaned_word = word.strip(".,?!").lower()

        if cleaned_word in word_counts:
            word_counts[cleaned_word] += 1
        else:
            word_counts[cleaned_word] = 1

    return word_counts

input_sentence = input("Enter a sentence: ")

word_occurrences = count_word_occurrences(input_sentence)

print("Word occurrences in the sentence:")
for word, count in word_occurrences.items():
    print(f"{word}: {count}")
