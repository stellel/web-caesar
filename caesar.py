import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
def rotate_character(char, rot):
	rotated = ""
	rot = int(rot)
	if char in lower:
		rotated = lower[(alphabet_position(char) + rot) % 26]

	else:
		
		rotated = upper[(alphabet_position(char) + rot) % 26]

	return rotated

def alphabet_position(letter):

	if letter in lower:
		position = lower.index(letter)

	else:
		position = upper.index(letter)

	return position

def encrypt(text, rot):
	encrypted = ""
	for char in text:
		if char.isalpha():
			encrypted += rotate_character(char, rot)
		else:
			encrypted += char

	return encrypted