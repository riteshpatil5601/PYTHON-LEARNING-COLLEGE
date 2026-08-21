def reverse_sentence():
    user_input = input("Enter a sentence: ")
    words = user_input.split()
    reversed_words = words[::-1]
    output_str = " ".join(reversed_words)
    print("Output:", output_str)

reverse_sentence()