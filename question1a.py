def letters(s):
	ss = []
	for ch in s:
		if ch.isalpha():
			print(ch)
			ss.append(ch.lower())
	return ss

print(letters("1 and 2 and 3"))