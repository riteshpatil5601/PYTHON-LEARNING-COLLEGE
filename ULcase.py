def count_case_letters(text):
    upper_count = 0
    lower_count = 0
    for char in text:
        if "A" <= char <= "Z":
            upper_count += 1
        elif "a" <= char <= "z":
            lower_count += 1
    return upper_count, lower_count
original_str = input("Enter a string: ")
uppercase_result, lowercase_result = count_case_letters(original_str)
print("Uppercase letters:", uppercase_result)
print("Lowercase letters:", lowercase_result)