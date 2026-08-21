def remove_spaces(text):
    result_text = ""
    for char in text:
        if char != " ":
            result_text += char
    return result_text
original_str = input("Enter a string: ")
result = remove_spaces(original_str)

print("String without spaces:", result)