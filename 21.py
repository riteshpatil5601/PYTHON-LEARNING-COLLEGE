password = input("Enter a password: ")

has_min_length = False
has_upper = False
has_lower = False
has_digit = False
has_special = False

length_count = 0
for char in password:
    length_count += 1

if length_count >= 8:
    has_min_length = True

for char in password:
    if "A" <= char <= "Z":
        has_upper = True
    elif "a" <= char <= "z":
        has_lower = True
    elif "0" <= char <= "9":
        has_digit = True
    else:
        has_special = True
if (
    has_min_length
    and has_upper
    and has_lower
    and has_digit
    and has_special
):
    print("Password is valid!")
else:
    print(
        "Password is invalid! It must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
    )