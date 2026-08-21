def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text
original_str = input("Enter a string: ")
result = reverse_string(original_str)
print("Reversed string:", result)