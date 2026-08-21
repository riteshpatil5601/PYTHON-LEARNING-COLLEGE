text = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for char in text:
  if char == " ":
    spaces += 1

  elif char >= "0" and char <= "9":
    digits += 1

  elif (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
    c = char.lower()
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
      vowels += 1
    else:
      consonants += 1

  else:
    special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)