sentence = input("Enter a sentence: ")
target_word = input("Enter the word to count: ")
word_count = 0
current_word = ""
for char in sentence + " ":
    if char != " ":
        current_word += char
    else:
        if current_word == target_word:
            word_count += 1
        current_word = ""
print(f'The word "{target_word}" appears {word_count} time(s).')