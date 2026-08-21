def find_longest_word(text):
    current_word = ""
    longest_word = ""
    current_length = 0
    longest_length = 0

    for char in text:
        if char != " ":
            current_word += char
            current_length += 1
        else:
            if current_length > longest_length:
                longest_length = current_length
                longest_word = current_word
            # Reset for the next word
            current_word = ""
            current_length = 0

    if current_length > longest_length:
        longest_word = current_word

    return longest_word
# Taking input from the user
original_str = input("Enter a sentence: ")
result = find_longest_word(original_str)
print("Longest word:", result)