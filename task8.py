def is_anagram(string1,string2):
	if len(string1)==len(string2):
		if sorted(string1)==sorted(string2):
			return True
	return False


result = is_anagram("cinema","iceman")
print(result)
