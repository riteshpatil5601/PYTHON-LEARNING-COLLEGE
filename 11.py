def count_words(text):
    word_count = 0
    in_word = False
    for char in text:
        if char != " ":
            if not in_word:
                word_count += 1
                in_word = True
        else:
            in_word = False

    return word_count

original_str = input("Enter a sentence: ")
result = count_words(original_str)
print("Total number of words:", result)