def decrypt(text, s):
	result = ""
	
	for i in range(len(text)):
		char = text[i]

		if (char.isupper()):
			result += chr((ord(char) + 65-s) % 26 + 65)
		elif (char.isspace() == True):
			result += chr(ord(" "))
		else:
			result += chr((ord(char) + 97-s) % 26 + 97)
	print("", end='')
	return result

print ("Enter text to decrypt")
text = str(input())
print ("Enter shift character (int)")
s = int(input())

print ("==============")
print ("A =", decrypt("A", s))
print ("Shift : ", str(s))
print ("Text : ", text)
print ("Uncipher: ", decrypt(text,s))
