def is_palindrome(text):
    cleaned_text = "".join(text.split()).lower()
    reversed_text = ""
    for char in cleaned_text:
        reversed_text = char + reversed_text
    return cleaned_text == reversed_text
original_str = input("Enter a string: ")

if is_palindrome(original_str):
    print(f'"{original_str}" is a palindrome.')
else:
    print(f'"{original_str}" is not a palindrome.')