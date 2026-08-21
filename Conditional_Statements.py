li= [-2, 0, 3]

print("if:")
for s in li:
	if s > 0:
		print(s, "->", "positive")

print("\nif_else:")
for s in li:
	if s % 2 == 0:
		print(s, "->", "even")
	else:
		print(s, "->", "odd")

print("\nelif:")
for s in li:
	if s < 0:
		print(s, "->", "negative")
	elif s == 0:
		print(s, "->", "zero")
	else:
		print(s, "->", "positive")

