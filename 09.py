def print_first_and_last(text):
    if len(text) > 0:
        first_char = text[0]
        last_char = ""
        count = 0
        for char in text:
            last_char = char
            count += 1
        print("First character:", first_char)
        print("Last character:", last_char)
    else:
        print("The string is empty.")
original_str = input("Enter a string: ")
print_first_and_last(original_str)