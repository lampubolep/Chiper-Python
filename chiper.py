def encrypt(text, s):
	result = ""

	for i in range(len(text)):
		char = text[i]

		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		else:
			result += chr((ord(char) + s-97) % 26 + 97)
	print("", end='')
	return result

print ("Enter text to encrypt")
text = str(input())
print ("Enter shift character (int)")
s = int(input())

print ("================")
print ("A =", encrypt("A", s))
print ("Shift : ", str(s))
print ("Text : ", text)
print ("Chiper: ", encrypt(text,s))
