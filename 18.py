# Taking input from the user
original_str = input("Enter a string: ")

result_str = ""

for char in original_str:
    # Check if the character is already in the result string
    is_duplicate = False
    for res_char in result_str:
        if char == res_char:
            is_duplicate = True
            break
            
    # If it's not a duplicate, add it to maintain original order
    if not is_duplicate:
        result_str += char

# Displaying the output
print("String after removing duplicates:", result_str)